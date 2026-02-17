# GEO/AEO Optimization -- AI Citation Strategies

## Core GEO Research

### Princeton GEO Paper (KDD 2024)
GEO methods boost AI visibility by up to 40%.

| Technique | Improvement |
|-----------|-------------|
| Citing authoritative sources | +115.1% visibility (5th-ranked sites) |
| Quotation addition | +37% |
| Statistics addition | +22% |
| Answer-first formatting | +340% (Seenos) |
| FAQ schema | +28% (Search Engine Land) |

Traditional keyword stuffing performs **worse than baseline** in generative engines.

### Kevin Indig's AI Search Pipeline (Jan 5, 2026)
Three critical stages:

1. **Retrieval**: Which pages enter the candidate set
   - Server response time under 200ms TTFB
   - Metadata relevance
   - Content must be in HTML (not behind JS)
2. **Citation**: Which sources get mentioned
   - Content freshness dominates (70%+ cited pages updated within 12 months)
   - Content within 3 months performs best
3. **Trust**: Which citations users click
   - Brand recognition
   - Source authority

## Content Format Impact on Citations

| Format | Impact | Source |
|--------|--------|--------|
| Listicles | 50% of top AI citations | Onely |
| Tables/structured data | 2.5x more citations | Onely |
| Long-form (2,000+ words) | 3x more citations | Onely |
| Answer-first formatting | +340% improvement | Seenos |
| FAQ schema | +28% increase | Search Engine Land |
| Content with statistics | +40% higher citation rates | Onely |

## Content Freshness Requirements

- 76.4% of ChatGPT's most-cited pages updated within 30 days (Digitaloft)
- URLs cited in AI results are 25.7% fresher than traditional search
- Content < 3 months old is 3x more likely to get cited
- **Action**: Update critical content quarterly with at least 30% changes

## Off-Site Signals (Dominate AI Visibility)

### Ahrefs Study (Dec 2025, 75,000 brands)

| Factor | Correlation with AI Visibility |
|--------|-------------------------------|
| YouTube mentions | 0.737 (strongest) |
| Branded web mentions | 0.656-0.709 |
| Domain Rating | 0.266-0.326 |
| Backlinks | 0.218 (dramatically weaker than expected) |

### Platform-Specific Citation Rates

**YouTube**:
- Citations in AI Overviews up 414% (Q1 2025, BrightEdge)
- How-to videos up 651%
- Visual demos up 592%
- 200x more cited than any other video platform
- Optimization: keywords in titles/transcripts, Q&A-style, 10+ min, public transcripts

**Reddit**:
- Citations surged 1.30% → 7.15% (450% growth)
- Google's $60M annual API deal
- 2.2-21% of AI Overview citations by query type
- Strategy: Authentic participation in 3-5 subreddits BEFORE any promotional content

**Review Platforms (B2B)**:
- G2 accounts for 22-23% of review-platform citations
- 33% of review citations come from G2
- Multi-platform presence: 4.6-6.3 citations vs 1.8 without (2.6-3.5x multiplier)

**Wikipedia/Wikidata**:
- 22% of AI training data
- 7.8% of all ChatGPT citations
- Used as "credibility tiebreaker" when sources conflict

### Budget Allocation
Recommended: **40% owned content / 60% earned media**
(Most companies allocate 90/10 — this is wrong for GEO)

88-92% of AI citations come from off-site signals, not on-page optimization alone.

## AI Crawler Technical Requirements

| Crawler | JavaScript Rendering |
|---------|---------------------|
| GPTBot (OpenAI) | No |
| ChatGPT-User | No |
| ClaudeBot | No |
| PerplexityBot | No |
| Googlebot | Yes |
| Google-Extended | Yes |

**Critical**: Content behind JavaScript is invisible to ChatGPT, Claude, Perplexity.
Use SSR, SSG, or ISR. Test by disabling JS and reloading.

### Performance Requirements for AI Retrieval
- Server response time under 200ms TTFB (Kevin Indig pipeline)
- Maximum 600ms TTFB before AI crawlers time out and skip the page
- Crawlers implement 3-5 second hard timeouts (Getpassionfruit)
- Core Web Vitals are a constraint, not a growth lever — good CWV doesn't reliably
  outperform, but severe LCP failure creates disadvantage (Search Engine Land, 107,352 pages)
- 46% of AI agent visits begin in reading mode (text-only, no JS/CSS)
- Slow pages are excluded from AI citation candidate pools entirely
- Vercel analysis of 500+ million GPTBot fetches found zero evidence of JS execution

### robots.txt for AI Visibility
```
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
```

### llms.txt Standard
Markdown file at site root helping LLMs understand content at inference time.
Keep under 10KB, plain URLs with brief comments.

## Attribution Crisis (Strauss et al., June 2025)

- 24% of ChatGPT (GPT-4o) responses generated without fetching any online content
- 34% of Gemini responses skip web retrieval entirely
- 92% of Gemini answers provide no clickable citations
- Perplexity visits ~10 pages per query but cites only 3-4

**Implication**: Optimizing for retrieval is critical — content must enter the
candidate set before citation is possible.

## GEO Case Study Results

| Company | Results | Timeframe |
|---------|---------|-----------|
| Go Fish Digital | +43% AI traffic, +83% conversions, 25x conversion rate | 3 months |
| Netpeak USA | +120% revenue, +693% AI visits | Ongoing |
| Nine Peaks Media | 36% visibility improvement, first ChatGPT citations | Ongoing |
| ABM Agency/Chemours | 82% ChatGPT mention rate, $90M+ pipeline | Ongoing |
| Smart Rent | 32% SQL increase, 40% faster pipeline | Ongoing |

## Entity-First SEO

Every page should unambiguously represent ONE canonical entity.
Google Knowledge Graph: 800B facts about 8B entities.

Entity building timeline (3-6 months):
1. Create entity map with Wikidata Q-IDs
2. Establish Wikipedia/Wikidata presence
3. Build entity consistency across all platforms (exact same name)
4. Practice "controlled co-occurrence" via third-party mentions
5. Earn external citations from recognized publications
