---
name: blog-write
description: >
  Write new blog articles from scratch optimized for Google rankings and AI
  citations. Generates full articles with answer-first formatting, sourced
  statistics, Pixabay/Unsplash images, SVG charts via /svg skill, FAQ schema,
  and proper heading hierarchy. Supports MDX, markdown, and HTML output.
  Use when user says "write blog", "new blog post", "create article",
  "write about", "draft blog", "generate blog post".
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - WebFetch
  - WebSearch
  - Task
---

# Blog Writer -- New Article Generation

Writes complete blog articles from a topic, brief, or outline. Every article
follows the 6 pillars of dual optimization (Google rankings + AI citations).

## Workflow

### Phase 1: Topic Understanding

1. **Clarify the topic** — If the user provides just a topic, ask:
   - Target audience (who is this for?)
   - Primary keyword / search intent
   - Desired word count (default: 2,000-2,500 words)
   - Platform/format (MDX, markdown, HTML — auto-detect if in a project)
2. **If a brief exists** — Load it and skip to Phase 2

### Phase 2: Research

Spawn a `blog-researcher` agent (or do inline research with WebSearch):

1. **Find 8-12 current statistics** (2025-2026 data preferred)
   - Search: `[topic] study 2025 2026 data statistics`
   - Prioritize tier 1-3 sources (see `references/quality-scoring.md`)
   - Record: statistic, source name, URL, date, methodology
2. **Find a cover image** (wide, high-quality, topic-relevant):
   - Search: `site:pixabay.com [topic] wide banner` (preferred)
   - Alternative: `site:unsplash.com [topic] wide`
   - Fallback: `site:pexels.com [topic] wide banner`
   - Target dimensions: 1200x630 (OG-compatible) or 1920x1080
   - Or generate a custom SVG cover via `/svg` (text-on-gradient with key stat)
   - See `references/visual-media.md` for cover image sizing details
3. **Find 3-5 inline images** from open-source platforms:
   - **Pixabay** (preferred): Search `site:pixabay.com [topic keywords]`
     - Extract image URL from page
     - Direct URLs: `https://cdn.pixabay.com/photo/YYYY/MM/DD/HH/MM/filename.jpg`
     - Verify with `curl -sI "<url>" | head -1` returns HTTP 200
   - **Unsplash** (alternative): Search `site:unsplash.com [topic keywords]`
     - Build URL: `https://images.unsplash.com/photo-<id>?w=1200&h=630&fit=crop&q=80`
   - **Pexels** (fallback): Search `site:pexels.com [topic keywords]`
4. **Plan 2-4 data visualizations** from researched statistics
   - Select diverse chart types (see `references/visual-media.md`)
   - Map data points to chart formats

### Phase 3: Outline Generation

Create a structured outline before writing:

```
# [Title as Question — Include Primary Keyword]

## Introduction (100-150 words)
- Hook with surprising statistic
- Problem/opportunity statement
- What the reader will learn

## H2: [Question Format] (300-400 words)
- Answer-first paragraph (40-60 words with stat + source)
- Supporting evidence
- [Image placement]
- Practical advice

## H2: [Question Format] (300-400 words)
- Answer-first paragraph
- [Chart: type + data description]
- Analysis and implications

## H2: [Statement for Variety] (300-400 words)
- Answer-first paragraph
- Real-world example or case study
- [Image placement]

## H2: [Question Format] (300-400 words)
- Answer-first paragraph
- [Chart: type + data description]
- Step-by-step guidance

## H2: [Question Format] (200-300 words)
- Answer-first paragraph
- Forward-looking analysis

## FAQ Section (3-5 questions, 40-60 words each answer)

## Conclusion (100-150 words)
- Key takeaways (bulleted)
- Call to action
```

Present the outline to the user for approval before writing.

### Phase 4: Chart Generation

Generate 2-4 SVG charts using `/svg-chart` skill.

For each chart, invoke `/svg-chart` with:
- Exact data values with sources
- Chart type (ensure diversity — never repeat a type)
- If platform is MDX: request JSX-compatible SVG (camelCase attributes)
- Save location: `/tmp/chart-<descriptive-name>.svg`

After generation, read the SVG and prepare for embedding.

See `references/visual-media.md` for chart type selection and styling rules.

### Phase 5: Content Writing

Write the full article following these rules:

#### 5a. Frontmatter
```yaml
---
title: "[Question-format title with primary keyword]"
description: "[Fact-dense, 150-160 chars, includes 1 statistic]"
coverImage: "[URL from Pixabay/Unsplash/Pexels or generated SVG path]"
coverImageAlt: "[Descriptive sentence about the cover image]"
ogImage: "[Same as coverImage, or custom OG image URL]"
date: "YYYY-MM-DD"
lastUpdated: "YYYY-MM-DD"
author: "[Author name]"
tags: ["keyword1", "keyword2", "keyword3"]
---
```

If the platform uses a different field name (e.g., `image`, `hero`, `thumbnail`),
adapt to match the project's existing frontmatter convention.

#### 5b. Answer-First Formatting (Critical)
Every H2 section MUST open with a 40-60 word paragraph containing:
- At least one specific statistic with source attribution
- A direct answer to the heading's implicit question

Pattern:
```markdown
## How Does X Impact Y in 2026?

[Stat from source] ([Source Name](url), year). [Direct answer to the heading
question in 1-2 more sentences, explaining the implication and what this means
for the reader.]
```

#### 5c. Paragraph Rules
- Every paragraph: 40-55 words (never exceed 100)
- Every sentence: max 15-20 words
- Start each paragraph with the most important information
- Target Flesch Reading Ease: 60-70

#### 5d. Heading Rules
- One H1 (title only)
- H2s for main sections (60-70% as questions)
- H3s for subsections only — never skip levels
- Include primary keyword naturally in 2-3 headings

#### 5e. Image Embedding

Standard markdown:
```markdown
![Descriptive alt text — topic keywords naturally](https://cdn.pixabay.com/photo/...)
```

MDX with Next.js Image (if detected):
```mdx
![Descriptive alt text — topic keywords naturally](https://cdn.pixabay.com/photo/...)
```

- Place images after H2 headings, before body text
- Space evenly throughout the post (not clustered)
- Alt text should be a full descriptive sentence

#### 5f. Chart Embedding

Standard markdown/HTML:
```html
<figure>
  <svg viewBox="0 0 560 380" ...>...</svg>
  <figcaption>Source: [Source Name], [Year]</figcaption>
</figure>
```

MDX format:
```mdx
<figure className="chart-container" style={{margin: '2.5rem 0', textAlign: 'center', padding: '1.5rem', borderRadius: '12px'}}>
  <svg viewBox="0 0 560 380" ...>...</svg>
</figure>
```

#### 5g. Citation Format
Inline attribution (always):
```markdown
Organic CTR declined 61% with AI Overviews ([Seer Interactive](https://www.seerinteractive.com/), 2025).
```

#### 5h. FAQ Section
Add 3-5 FAQ items with 40-60 word answers. Each answer must contain a statistic.

For MDX with FAQSchema component:
```mdx
<FAQSchema faqs={[
  { question: "Question?", answer: "40-60 word answer with statistic and source." },
]} />
```

For standard markdown:
```markdown
## Frequently Asked Questions

### Question text here?

Answer with statistic and source attribution (40-60 words).
```

#### 5i. Internal Linking
- 5-10 internal links per 2,000-word post
- Link to relevant existing content naturally
- Use descriptive anchor text (not "click here")

### Phase 6: Quality Check

Before delivering, verify:
1. Every H2 opens with a statistic + source
2. No paragraph exceeds 100 words
3. All statistics have named tier 1-3 sources
4. 2-4 charts with type diversity
5. 3-5 inline images with descriptive alt text
6. Cover image present in frontmatter (coverImage + ogImage)
7. FAQ section present with 3-5 items
8. Heading hierarchy is clean (H1 → H2 → H3)
9. Meta description is 150-160 chars with a stat

### Phase 7: Delivery

Present the completed article with a summary:

```
## Blog Post Complete: [Title]

### Statistics
- [N] sourced statistics from tier 1-3 sources
- [N] unique sources cited

### Visual Elements
- Cover image: [source — Pixabay/Unsplash/Pexels or generated SVG]
- [N] inline images (Pixabay/Unsplash/Pexels)
- [N] SVG charts (types: bar, lollipop, donut, line)

### Structure
- [N] H2 sections with answer-first formatting
- [N] FAQ items with schema
- Word count: ~[N] words
- Estimated reading time: [N] min

### Next Steps
- Review and customize for your brand voice
- Add internal links to your existing content
- Run `/blog analyze <file>` to verify quality score
```
