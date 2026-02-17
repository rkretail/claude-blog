# Blog Quality Scoring Checklist

Score each blog post against this checklist. Used by `/blog analyze`.

## Content Quality (25 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| No paragraph > 100 words | 8 | Hard limit, no exceptions |
| Target 40-55 words per paragraph | 5 | Most paragraphs in range |
| Sentences max 15-20 words | 4 | Occasional longer OK |
| Question-format headings | 4 | 60-70% of H2s are questions |
| Flesch Reading Ease 60-70 | 4 | Readable by general audience |

## Answer-First Formatting (20 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| Every H2 opens with stat | 10 | First paragraph has a specific number + source |
| Opening paragraphs 40-60 words | 5 | No section opener exceeds 60 words |
| Direct answer in first sentence | 5 | Reader gets the answer before explanation |

## Statistics & Citations (20 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| Zero fabricated statistics | 8 | Every number has a named source |
| Tier 1-3 sources only | 5 | No SEO tool blogs, affiliate sites, low-authority |
| Inline attribution format | 4 | `([Source Name](url))` or `([Source Name](url), year)` |
| 8+ unique statistics | 3 | Minimum 8 distinct data points |

## Visual Elements (15 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| 2-4 SVG charts present | 5 | Charts use real data with source attribution |
| Chart type diversity | 3 | No two charts use the same type |
| 3-5 images with alt text | 4 | Relevant, descriptive alt text, from Pixabay/Unsplash |
| Visuals well-distributed | 3 | Not clustered — spread across the post |

## Schema & Structure (10 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| FAQ schema present | 4 | 3-5 FAQ items with 40-60 word answers |
| Clean heading hierarchy | 3 | H1 → H2 → H3, no skipped levels |
| BlogPosting schema | 2 | dateModified matches lastUpdated |
| Meta description quality | 1 | 150-160 chars, fact-dense, includes statistic |

## Freshness & Trust (10 points)

| Check | Points | Pass Criteria |
|-------|--------|---------------|
| lastUpdated within 30 days | 4 | Or dateModified in schema |
| Max 1 brand mention | 3 | Only in author context |
| Author has E-E-A-T bio | 2 | Credentials, not a sales pitch |
| Original publish date preserved | 1 | date field unchanged |

## Total: 100 points

### Scoring Bands

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Excellent | Publish as-is |
| 75-89 | Good | Minor tweaks needed |
| 60-74 | Needs Work | Significant improvements required |
| < 60 | Poor | Full rewrite recommended |

## Priority Classification

When reporting issues, classify by priority:

### Critical (Must Fix Before Publishing)
- Fabricated statistics (zero tolerance)
- Broken heading hierarchy (H1 → H3 skip)
- Paragraphs > 100 words
- No source attribution on claims

### High Priority
- Missing answer-first formatting on H2 sections
- No FAQ section/schema
- Fewer than 3 sourced statistics
- Missing meta description or lastUpdated

### Medium Priority
- Fewer than 2 charts
- Fewer than 3 images
- Tier 4-5 sources present
- Self-promotion > 1 mention

### Low Priority
- Paragraph length slightly above 55 words (but under 100)
- Non-question H2 headings above 40%
- Missing chart type diversity
- Images without alt text

## Quick Automated Checks

These can be detected programmatically:
1. Word count per paragraph (split on double newlines)
2. Heading hierarchy (regex for `^#{1,6} `)
3. Image count (regex for `!\[` or `<img`)
4. Chart count (regex for `<svg` or `<figure`)
5. FAQ presence (search for "FAQ" or "Frequently Asked")
6. Citation format (regex for `\([^)]+\(http`)
7. lastUpdated presence (frontmatter check)
8. Meta description length (frontmatter check)
9. Self-promotion patterns (brand name frequency)
10. Unsourced statistics (numbers without attribution nearby)
