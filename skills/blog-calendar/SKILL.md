---
name: blog-calendar
description: >
  Generate editorial calendars for blogs with topic clusters, publishing
  schedules, freshness update plans, seasonal opportunities, and content
  type mix. Plans monthly or quarterly calendars optimized for SEO topic
  authority and AI citation freshness requirements (30-day update cycles).
  Use when user says "editorial calendar", "content calendar", "blog calendar",
  "publishing schedule", "blog plan", "content plan", "what should I write".
allowed-tools:
  - Read
  - Write
  - Bash
  - Grep
  - Glob
  - WebFetch
  - WebSearch
---

# Blog Calendar -- Editorial Planning

Generates editorial calendars with topic clusters, publishing cadence,
freshness update schedules, and seasonal hooks. Optimized for building
topical authority (Google) and maintaining citation freshness (AI platforms).

## Workflow

### Step 1: Understand the Blog

Gather context:
1. **Niche/industry** — What is the blog about?
2. **Existing content** — Scan for existing blog posts (Glob for *.md, *.mdx, *.html)
3. **Publishing cadence** — How often can they publish? (default: 2x/week)
4. **Timeframe** — Monthly or quarterly calendar?
5. **Business goals** — What should the blog drive? (traffic, leads, authority)

### Step 2: Topic Cluster Design

Design 3-5 topic clusters (pillar + supporting content):

```
Cluster: [Pillar Topic]
├── Pillar Page: [Comprehensive guide — 3,000+ words]
├── Supporting: [Subtopic 1 — 2,000 words]
├── Supporting: [Subtopic 2 — 2,000 words]
├── Supporting: [Subtopic 3 — 1,500 words]
├── Comparison: [X vs Y — 1,500 words]
└── FAQ: [Common questions — 1,500 words]
```

Each cluster should:
- Target a primary keyword theme
- Cover the topic comprehensively for topical authority
- Include varied content types (guides, comparisons, how-tos, listicles)
- Support internal linking between cluster pages

### Step 3: Freshness Update Schedule

AI platforms heavily favor fresh content (76% of top citations updated within 30 days).

Plan update cycles:
- **High-priority posts** (traffic drivers): Update every 30 days
- **Medium-priority posts**: Update every 90 days
- **Low-priority posts**: Update annually
- **Evergreen posts**: Update when data changes

### Step 4: Seasonal & Trending Hooks

Research seasonal opportunities:
1. **Industry events** — Conferences, product launches, algorithm updates
2. **Seasonal trends** — Google Trends for topic + month
3. **Annual reports** — When do major studies release new data?
4. **Algorithm updates** — Google core updates (typically 3-4 per year)

### Step 5: Generate the Calendar

#### Monthly Calendar Format

```
# Editorial Calendar: [Month Year]

## Publishing Cadence: [N] posts/week

### Week 1: [Date Range]
| Day | Type | Title | Cluster | Target Keyword | Status |
|-----|------|-------|---------|---------------|--------|
| Mon | New | [Title] | [Cluster] | [keyword] | Draft |
| Thu | Update | [Existing post] | [Cluster] | [keyword] | Refresh |

### Week 2: [Date Range]
| Day | Type | Title | Cluster | Target Keyword | Status |
|-----|------|-------|---------|---------------|--------|
| Mon | New | [Title] | [Cluster] | [keyword] | Brief |
| Thu | New | [Title] | [Cluster] | [keyword] | Brief |

### Week 3: [Date Range]
[...]

### Week 4: [Date Range]
[...]

## Content Mix This Month
- New posts: [N]
- Freshness updates: [N]
- Content types: [guides, comparisons, how-tos, listicles, ...]

## Freshness Update Queue
| Post | Last Updated | Priority | Scheduled |
|------|-------------|----------|-----------|
| [slug] | [date] | High | Week 2 |
| [slug] | [date] | Medium | Week 4 |

## Seasonal Hooks
- [Event/trend and how to leverage it]
```

#### Quarterly Calendar Format

```
# Quarterly Editorial Plan: Q[N] [Year]

## Content Strategy
- Topic clusters: [N] active
- New posts planned: [N]
- Freshness updates planned: [N]
- Total content actions: [N]

## Month 1: [Month]
### Focus: [Primary cluster or theme]
| Week | Type | Title | Cluster | Keyword |
|------|------|-------|---------|---------|
| W1 | New | ... | ... | ... |
| W1 | Update | ... | ... | ... |
| W2 | New | ... | ... | ... |
[...]

## Month 2: [Month]
### Focus: [Primary cluster or theme]
[...]

## Month 3: [Month]
### Focus: [Primary cluster or theme]
[...]

## Quarterly Goals
- [ ] Publish [N] new posts
- [ ] Update [N] existing posts for freshness
- [ ] Complete [Cluster] pillar + [N] supporting pages
- [ ] Achieve [metric target]

## Distribution Plan
- Reddit: Post insights to [subreddit list] (authentic participation)
- YouTube: Create companion videos for pillar pages
- Social: Share key statistics and charts from posts
- Email: Newsletter featuring [N] top posts per month
```

### Step 6: Save & Next Steps

Save the calendar and suggest:
1. Start with `/blog brief <first-topic>` to create the first content brief
2. Use `/blog write` to generate articles from briefs
3. Use `/blog rewrite` for freshness updates on existing content
4. Re-run `/blog calendar` next month/quarter for the next plan
