#!/usr/bin/env python3
"""
Blog Quality Analyzer

Analyzes blog post files for quality metrics: word counts, paragraph lengths,
heading structure, image count, chart count, citation detection, and more.
Returns structured JSON output for use by the blog-analyze sub-skill.

Usage:
    python analyze_blog.py <file_path>
    python analyze_blog.py <file_path> --output report.json
    python analyze_blog.py <directory> --batch
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def extract_frontmatter(content: str) -> dict[str, Any]:
    """Extract YAML frontmatter from markdown/MDX content."""
    frontmatter = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        for line in fm_text.split('\n'):
            if ':' in line:
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if value:
                    frontmatter[key] = value
    return frontmatter


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from content."""
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, count=1, flags=re.DOTALL)


def analyze_headings(content: str) -> dict[str, Any]:
    """Analyze heading structure."""
    headings = []
    for match in re.finditer(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE):
        level = len(match.group(1))
        text = match.group(2).strip()
        is_question = text.rstrip().endswith('?')
        headings.append({
            'level': level,
            'text': text,
            'is_question': is_question,
        })

    h1_count = sum(1 for h in headings if h['level'] == 1)
    h2_count = sum(1 for h in headings if h['level'] == 2)
    h2_questions = sum(1 for h in headings if h['level'] == 2 and h['is_question'])
    question_ratio = h2_questions / h2_count if h2_count > 0 else 0

    # Check for hierarchy skips
    hierarchy_clean = True
    prev_level = 0
    for h in headings:
        if h['level'] > prev_level + 1 and prev_level > 0:
            hierarchy_clean = False
        prev_level = h['level']

    return {
        'headings': headings,
        'h1_count': h1_count,
        'h2_count': h2_count,
        'h2_question_count': h2_questions,
        'h2_question_ratio': round(question_ratio, 2),
        'hierarchy_clean': hierarchy_clean,
        'total': len(headings),
    }


def analyze_paragraphs(content: str) -> dict[str, Any]:
    """Analyze paragraph lengths."""
    # Remove code blocks
    cleaned = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Remove HTML/JSX blocks
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    # Remove headings
    cleaned = re.sub(r'^#{1,6}\s+.*$', '', cleaned, flags=re.MULTILINE)
    # Remove images
    cleaned = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned)

    # Split into paragraphs (double newline separated)
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', cleaned) if p.strip()]

    word_counts = []
    over_100 = 0
    in_range = 0  # 40-55 words

    for p in paragraphs:
        words = len(p.split())
        if words < 5:  # Skip very short fragments
            continue
        word_counts.append(words)
        if words > 100:
            over_100 += 1
        if 40 <= words <= 55:
            in_range += 1

    total = len(word_counts)
    avg = sum(word_counts) / total if total else 0
    in_range_ratio = in_range / total if total else 0

    return {
        'total_paragraphs': total,
        'avg_word_count': round(avg, 1),
        'over_100_words': over_100,
        'in_40_55_range': in_range,
        'in_range_ratio': round(in_range_ratio, 2),
        'max_word_count': max(word_counts) if word_counts else 0,
        'total_word_count': sum(word_counts),
    }


def analyze_images(content: str) -> dict[str, Any]:
    """Count images and check alt text."""
    # Markdown images
    md_images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    # HTML images
    html_images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', content)

    images = []
    for alt, src in md_images:
        images.append({
            'src': src,
            'has_alt': bool(alt.strip()),
            'alt_length': len(alt.strip()),
            'source': 'pixabay' if 'pixabay' in src else
                      'unsplash' if 'unsplash' in src else
                      'pexels' if 'pexels' in src else 'other',
        })

    for src in html_images:
        images.append({
            'src': src,
            'has_alt': True,  # Can't easily extract from regex
            'source': 'pixabay' if 'pixabay' in src else
                      'unsplash' if 'unsplash' in src else
                      'pexels' if 'pexels' in src else 'other',
        })

    with_alt = sum(1 for img in images if img['has_alt'])

    return {
        'count': len(images),
        'with_alt_text': with_alt,
        'without_alt_text': len(images) - with_alt,
        'sources': {s: sum(1 for i in images if i['source'] == s) for s in set(i['source'] for i in images)},
    }


def analyze_charts(content: str) -> dict[str, Any]:
    """Count SVG charts and check for type diversity."""
    svg_count = len(re.findall(r'<svg\b', content, re.IGNORECASE))
    figure_count = len(re.findall(r'<figure\b', content, re.IGNORECASE))

    return {
        'svg_count': svg_count,
        'figure_count': figure_count,
        'chart_count': max(svg_count, figure_count),
    }


def analyze_citations(content: str) -> dict[str, Any]:
    """Analyze statistics and their citations."""
    # Find statistics patterns (numbers with %)
    stat_patterns = re.findall(r'\d+\.?\d*%', content)

    # Find inline citations ([Source](url))
    citations = re.findall(r'\[([^\]]+)\]\(https?://[^)]+\)', content)

    # Find parenthetical citations (Source Name, year)
    paren_citations = re.findall(r'\(([^)]*(?:20\d{2})[^)]*)\)', content)

    # Rough count of sourced vs unsourced stats
    sourced_stats = 0
    unsourced_stats = 0
    for stat in stat_patterns:
        # Check if there's a citation within 200 chars after the stat
        pos = content.find(stat)
        if pos >= 0:
            context = content[pos:pos + 200]
            if re.search(r'\[.+\]\(https?://', context) or re.search(r'\([^)]*20\d{2}[^)]*\)', context):
                sourced_stats += 1
            else:
                unsourced_stats += 1

    return {
        'total_statistics': len(stat_patterns),
        'sourced_statistics': sourced_stats,
        'unsourced_statistics': unsourced_stats,
        'inline_citations': len(citations),
        'unique_sources': len(set(c.lower() for c in citations)),
    }


def analyze_faq(content: str) -> dict[str, Any]:
    """Check for FAQ section and schema."""
    has_faq_section = bool(re.search(r'(?i)#{1,3}\s*(?:FAQ|Frequently Asked)', content))
    has_faq_schema = bool(re.search(r'(?i)FAQSchema|FAQPage|faqpage', content))

    # Count FAQ items
    faq_items = 0
    if has_faq_section:
        faq_match = re.search(r'(?i)#{1,3}\s*(?:FAQ|Frequently Asked).*', content, re.DOTALL)
        if faq_match:
            faq_text = faq_match.group()
            faq_items = len(re.findall(r'^#{3,4}\s+.+\?', faq_text, re.MULTILINE))

    return {
        'has_faq_section': has_faq_section,
        'has_faq_schema': has_faq_schema,
        'faq_item_count': faq_items,
    }


def analyze_freshness(frontmatter: dict[str, Any]) -> dict[str, Any]:
    """Check freshness signals."""
    return {
        'has_date': 'date' in frontmatter,
        'has_last_updated': 'lastUpdated' in frontmatter or 'last_updated' in frontmatter,
        'date': frontmatter.get('date', ''),
        'last_updated': frontmatter.get('lastUpdated', frontmatter.get('last_updated', '')),
    }


def analyze_self_promotion(content: str, brand_name: str = '') -> dict[str, Any]:
    """Check self-promotion levels."""
    promo_patterns = [
        r'(?i)at \w+,\s+we',
        r'(?i)our (?:team|company|product|platform|solution)',
        r'(?i)we (?:offer|provide|deliver|help|specialize)',
    ]

    promo_count = sum(len(re.findall(p, content)) for p in promo_patterns)

    return {
        'self_promotion_patterns': promo_count,
        'exceeds_limit': promo_count > 1,
    }


def calculate_score(analysis: dict[str, Any]) -> dict[str, Any]:
    """Calculate the 0-100 quality score."""
    scores = {}

    # Content Quality (25 points)
    cq = 0
    paras = analysis['paragraphs']
    if paras['over_100_words'] == 0:
        cq += 8
    if paras['in_range_ratio'] >= 0.5:
        cq += 5
    elif paras['in_range_ratio'] >= 0.3:
        cq += 3
    cq += 4  # Sentence length (can't easily measure without NLP)
    headings = analysis['headings']
    if headings['h2_question_ratio'] >= 0.6:
        cq += 4
    elif headings['h2_question_ratio'] >= 0.4:
        cq += 2
    scores['content_quality'] = min(cq, 25)

    # Answer-First Formatting (20 points) — approximate
    af = 0
    # This requires deeper analysis; give partial credit based on structure
    if headings['h2_count'] >= 4:
        af += 5
    if headings['hierarchy_clean']:
        af += 5
    citations = analysis['citations']
    if citations['sourced_statistics'] >= 4:
        af += 10
    elif citations['sourced_statistics'] >= 2:
        af += 5
    scores['answer_first'] = min(af, 20)

    # Statistics & Citations (20 points)
    sc = 0
    if citations['unsourced_statistics'] == 0 and citations['total_statistics'] > 0:
        sc += 8
    elif citations['unsourced_statistics'] <= 2:
        sc += 4
    if citations['unique_sources'] >= 5:
        sc += 5
    elif citations['unique_sources'] >= 3:
        sc += 3
    if citations['inline_citations'] >= 5:
        sc += 4
    elif citations['inline_citations'] >= 2:
        sc += 2
    if citations['total_statistics'] >= 8:
        sc += 3
    elif citations['total_statistics'] >= 4:
        sc += 1
    scores['statistics_citations'] = min(sc, 20)

    # Visual Elements (15 points)
    ve = 0
    charts = analysis['charts']
    images = analysis['images']
    if 2 <= charts['chart_count'] <= 4:
        ve += 5
    elif charts['chart_count'] >= 1:
        ve += 2
    ve += 3  # Chart diversity (can't detect types from count alone)
    if 3 <= images['count'] <= 5:
        ve += 4
    elif images['count'] >= 1:
        ve += 2
    if images['count'] + charts['chart_count'] >= 4:
        ve += 3
    elif images['count'] + charts['chart_count'] >= 2:
        ve += 1
    scores['visual_elements'] = min(ve, 15)

    # Schema & Structure (10 points)
    ss = 0
    faq = analysis['faq']
    if faq['has_faq_schema']:
        ss += 4
    elif faq['has_faq_section']:
        ss += 2
    if headings['hierarchy_clean']:
        ss += 3
    if headings['h1_count'] == 1:
        ss += 1
    fm = analysis['frontmatter']
    desc = fm.get('description', '')
    if 150 <= len(desc) <= 160:
        ss += 2
    elif desc:
        ss += 1
    scores['schema_structure'] = min(ss, 10)

    # Freshness & Trust (10 points)
    ft = 0
    freshness = analysis['freshness']
    if freshness['has_last_updated']:
        ft += 4
    promo = analysis['self_promotion']
    if not promo['exceeds_limit']:
        ft += 3
    ft += 2  # Author E-E-A-T (can't detect from text alone)
    if freshness['has_date']:
        ft += 1
    scores['freshness_trust'] = min(ft, 10)

    total = sum(scores.values())

    if total >= 90:
        rating = 'Excellent'
    elif total >= 75:
        rating = 'Good'
    elif total >= 60:
        rating = 'Needs Work'
    else:
        rating = 'Poor'

    return {
        'total': total,
        'rating': rating,
        'categories': scores,
    }


def analyze_file(file_path: str) -> dict[str, Any]:
    """Analyze a single blog file."""
    path = Path(file_path)
    if not path.exists():
        return {'error': f'File not found: {file_path}'}

    content = path.read_text(encoding='utf-8')
    frontmatter = extract_frontmatter(content)
    body = strip_frontmatter(content)

    analysis = {
        'file': str(path),
        'format': path.suffix,
        'frontmatter': frontmatter,
        'headings': analyze_headings(body),
        'paragraphs': analyze_paragraphs(body),
        'images': analyze_images(content),
        'charts': analyze_charts(content),
        'citations': analyze_citations(body),
        'faq': analyze_faq(body),
        'freshness': analyze_freshness(frontmatter),
        'self_promotion': analyze_self_promotion(body),
    }

    analysis['score'] = calculate_score(analysis)

    return analysis


def main(args: argparse.Namespace) -> dict[str, Any]:
    """Main execution function."""
    path = Path(args.input)

    if path.is_dir() and args.batch:
        results = []
        for ext in ['*.md', '*.mdx', '*.html']:
            for f in path.glob(ext):
                results.append(analyze_file(str(f)))
        return {'batch': True, 'count': len(results), 'results': results}
    elif path.is_file():
        return analyze_file(str(path))
    else:
        return {'error': f'Path not found or not a file: {args.input}'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze blog post quality')
    parser.add_argument('input', help='Blog file path or directory (with --batch)')
    parser.add_argument('--output', '-o', help='Output file path (JSON)')
    parser.add_argument('--batch', action='store_true', help='Analyze all blog files in directory')
    args = parser.parse_args()

    try:
        result = main(args)
        output = json.dumps(result, indent=2)

        if args.output:
            Path(args.output).write_text(output)
            print(f'Report saved to {args.output}')
        else:
            print(output)
    except Exception as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)
