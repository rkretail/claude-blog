---
name: blog-rewrite
description: >
  Rewrite and optimize existing blog posts for Google rankings (Authenticity
  Update, E-E-A-T) and AI citations (GEO/AEO). Replaces fabricated statistics
  with sourced data, applies answer-first formatting, adds Pixabay/Unsplash
  images, generates SVG charts via /svg skill, injects FAQ schema, and updates
  freshness signals. Works with any blog format (MDX, markdown, HTML).
  Use when user says "rewrite blog", "optimize blog", "update blog",
  "improve blog", "fix blog", "refresh blog post", "blog optimization".
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

# Blog Rewriter -- Optimize Existing Posts

Rewrites and optimizes existing blog posts for dual ranking: Google search
and AI citation platforms. Preserves the author's voice while applying the
6 pillars of optimization.

## Workflow

### Phase 1: Audit (Read-Only)

1. **Read the blog post** — Detect format (MDX, markdown, HTML)
2. **Run the quality checklist** against `references/quality-scoring.md`:
   - Count fabricated vs sourced statistics
   - Check answer-first formatting (H2 → stat in first sentence?)
   - Count images and charts (type diversity?)
   - Measure paragraph lengths (any > 100 words?)
   - Check heading hierarchy (H1 → H2 → H3, no skips?)
   - Look for FAQ schema
   - Check freshness signals (lastUpdated, dateModified)
   - Assess self-promotion level
   - Evaluate citation tier quality
3. **Calculate current score** (0-100)
4. **Present audit summary** with specific findings and score
5. **Enter plan mode** — Present section-by-section optimization plan

Wait for user approval before proceeding.

### Phase 2: Research

1. **Identify the blog's core topic** from existing content
2. **Find replacement statistics** for any fabricated/unsourced data:
   - Search: `[topic] study 2025 2026 data statistics`
   - Target tier 1-3 sources only
3. **Find images** if post has fewer than 3:
   - Pixabay: `site:pixabay.com [topic keywords]`
   - Unsplash: `site:unsplash.com [topic keywords]`
   - Verify each URL returns HTTP 200
4. **Plan charts** if post has fewer than 2:
   - Identify data suitable for visualization
   - Select diverse chart types

### Phase 3: Chart Generation (If Needed)

Generate charts via `/svg-chart` if the post needs more visual elements.
See `references/visual-media.md` for requirements.

### Phase 4: Content Rewrite

Apply changes in this order:

#### 4a. Preserve What Works
- Keep the author's voice and unique perspective
- Preserve original insights and first-hand experience
- Keep existing quality images and charts
- Maintain internal links

#### 4b. Fix Frontmatter
- Add `lastUpdated: "YYYY-MM-DD"` (today's date)
- Keep original `date` unchanged
- Fix meta description: fact-dense, 150-160 chars, includes 1 statistic
- Add `coverImage` + `coverImageAlt` + `ogImage` if missing
  - Search Pixabay/Unsplash/Pexels for wide hero image (1200x630)
  - Or generate custom SVG via `/svg` (text-on-gradient with key stat)
- Verify tags/categories are appropriate

#### 4c. Apply Answer-First Formatting
Every H2 section MUST open with a 40-60 word paragraph containing:
- At least one specific statistic with source attribution
- A direct answer to the heading's implicit question

#### 4d. Replace Fabricated Statistics
- Search for patterns: "X% of...", "X out of Y...", unsourced claims
- Replace with real data from tier 1-3 sources
- Always include inline attribution: `([Source Name](url), year)`

#### 4e. Improve Headings
- Convert statement headings to questions where natural (60-70% target)
- Keep 2-3 statement headings for variety
- Ensure keyword appears in 2-3 headings naturally

#### 4f. Fix Paragraph Length
- Split any paragraph > 100 words
- Target 40-55 words per paragraph
- Ensure each paragraph starts with its most important sentence

#### 4g. Add Visual Elements
- Embed new images after H2 headings, spaced evenly
- Embed charts within relevant sections
- Adapt embed format to detected platform (MDX vs markdown vs HTML)

#### 4h. Add/Improve FAQ
- If no FAQ exists, add one (3-5 questions)
- If FAQ exists, ensure answers are 40-60 words with statistics
- Add FAQ schema markup appropriate to platform

#### 4i. Reduce Self-Promotion
- Max 1 brand mention (author bio context only)
- Remove "At [Company], we..." patterns
- Convert promotional sections to educational content

### Phase 5: Verification

After rewriting, verify all quality gates pass:
1. Every H2 opens with a statistic + source
2. No paragraph exceeds 100 words
3. Zero fabricated statistics
4. Heading hierarchy is clean
5. FAQ section present with schema
6. Images have descriptive alt text
7. Cover image present in frontmatter (coverImage + ogImage)
8. If MDX: build the project to verify no compilation errors

### Phase 6: Summary

```
## Blog Optimization Complete: [Title]

### Score Change
- Before: [X]/100 ([Rating])
- After: [Y]/100 ([Rating])

### Changes Made
- [X] statistics replaced with sourced data
- [X] SVG charts added (types: ...)
- [X] images added from Pixabay/Unsplash
- Answer-first formatting applied to [N] H2 sections
- FAQ schema injected with [N] questions
- lastUpdated set to [date]
- Self-promotion reduced to [N] mentions

### Visual Elements
- Charts: [count] ([types])
- Images: [count]

### Ready for
- `/blog analyze <file>` to verify final score
- Publishing / deploying
```

## Update Mode

When invoked as `/blog update <file>`, focus on freshness:
1. Update statistics to latest available data (2025-2026)
2. Add new developments since last update
3. Refresh images if older than 1 year
4. Update `lastUpdated` in frontmatter
5. Preserve the existing structure — minimize rewrites
6. Target: at least 30% content change to register as "fresh" for AI crawlers
