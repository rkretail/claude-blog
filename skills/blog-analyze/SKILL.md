---
name: blog-analyze
description: >
  Audit and score blog posts on a 0-100 scale across 6 quality dimensions:
  content quality, answer-first formatting, statistics and citations, visual
  elements, schema and structure, freshness and trust. Generates prioritized
  recommendations (Critical/High/Medium/Low) with specific fixes. Works with
  any format (MDX, markdown, HTML, URL). Use when user says "analyze blog",
  "audit blog", "blog score", "check blog quality", "blog review",
  "rate this blog", "blog health check".
allowed-tools:
  - Read
  - Write
  - Bash
  - Grep
  - Glob
  - WebFetch
---

# Blog Analyzer -- Quality Audit & Scoring

Scores blog posts on a 0-100 scale and provides prioritized improvement
recommendations. Works with local files or published URLs.

## Input Handling

- **Local file**: Read the file directly
- **URL**: Fetch with WebFetch, extract content
- **Directory**: Scan for blog files, audit all (batch mode)

## Scoring Process

### Step 1: Content Extraction

Read the blog post and extract:
- Frontmatter (title, description, date, lastUpdated, author, tags)
- Heading structure (H1, H2, H3 with hierarchy)
- Paragraph count and word counts
- Statistics (any number claims with or without sources)
- Images (count, alt text presence)
- Charts/SVGs (count, type diversity)
- Links (internal, external, broken)
- FAQ section presence
- Schema markup

### Step 2: Score Each Category

Load `references/quality-scoring.md` for the full checklist. Score each:

#### Content Quality (25 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| No paragraph > 100 words | 8 | Hard limit, no exceptions |
| Target 40-55 words per paragraph | 5 | Most paragraphs in range |
| Sentences max 15-20 words | 4 | Occasional longer OK |
| Question-format headings | 4 | 60-70% of H2s are questions |
| Flesch Reading Ease 60-70 | 4 | Readable by general audience |

#### Answer-First Formatting (20 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| Every H2 opens with stat | 10 | First paragraph has a specific number + source |
| Opening paragraphs 40-60 words | 5 | No section opener exceeds 60 words |
| Direct answer in first sentence | 5 | Reader gets the answer before explanation |

#### Statistics & Citations (20 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| Zero fabricated statistics | 8 | Every number has a named source |
| Tier 1-3 sources only | 5 | No SEO tool blogs, affiliate sites, low-authority |
| Inline attribution format | 4 | `([Source Name](url))` or `([Source Name](url), year)` |
| 8+ unique statistics | 3 | Minimum 8 distinct data points |

#### Visual Elements (15 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| 2-4 SVG charts present | 5 | Charts use real data with source attribution |
| Chart type diversity | 3 | No two charts use the same type |
| 3-5 images with alt text | 4 | Relevant to content, descriptive alt text |
| Visuals well-distributed | 3 | Not clustered — spread across the post |

#### Schema & Structure (10 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| FAQ schema present | 4 | 3-5 FAQ items with 40-60 word answers |
| Clean heading hierarchy | 3 | H1 → H2 → H3, no skipped levels |
| BlogPosting schema renders | 2 | dateModified matches lastUpdated |
| Meta description quality | 1 | 150-160 chars, fact-dense, includes statistic |

#### Freshness & Trust (10 points)
| Check | Points | Pass Criteria |
|-------|--------|---------------|
| lastUpdated within 30 days | 4 | Or dateModified in schema |
| Max 1 brand mention | 3 | Only in author context |
| Author has E-E-A-T bio | 2 | Credentials, not a sales pitch |
| Original publish date preserved | 1 | date field unchanged |

### Step 3: Generate Report

```
## Blog Quality Report: [Title]

**Score: [X]/100** — [Rating]

### Score Breakdown
| Category | Score | Max |
|----------|-------|-----|
| Content Quality | X | 25 |
| Answer-First Formatting | X | 20 |
| Statistics & Citations | X | 20 |
| Visual Elements | X | 15 |
| Schema & Structure | X | 10 |
| Freshness & Trust | X | 10 |
| **Total** | **X** | **100** |

### Issues Found

#### Critical (Must Fix)
- [ ] [Issue with specific location and fix]

#### High Priority
- [ ] [Issue with specific location and fix]

#### Medium Priority
- [ ] [Issue with specific location and fix]

#### Low Priority
- [ ] [Issue with specific location and fix]

### Quick Stats
- Word count: [N]
- Paragraphs: [N] (X over 100 words)
- H2 sections: [N] (X with answer-first formatting)
- Statistics: [N] sourced / [N] unsourced
- Images: [N] (X with alt text)
- Charts: [N] (types: ...)
- Internal links: [N]
- External links: [N]

### Recommended Actions
1. [Most impactful fix — Critical items first]
2. [Second most impactful]
3. [Third]

Run `/blog rewrite <file>` to apply these optimizations automatically.
```

## Batch Mode

When given a directory, scan for blog files and produce a summary table:

```
## Blog Audit Summary: [N] Posts Analyzed

| File | Score | Rating | Top Issue |
|------|-------|--------|-----------|
| post-1.md | 85 | Good | Missing FAQ schema |
| post-2.md | 42 | Poor | 12 fabricated stats |
| post-3.md | 71 | Needs Work | No answer-first formatting |

### Priority Queue (Lowest Scoring First)
1. post-2.md (42) — Full rewrite needed
2. post-3.md (71) — Answer-first + stats
3. post-1.md (85) — Add FAQ schema

Run `/blog rewrite <file>` on each, starting from lowest score.
```
