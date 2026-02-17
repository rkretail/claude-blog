# Visual Media Integration -- Images, Charts & Cover Images

## Cover Images & OG Images

Every blog post should have a cover image for social sharing and blog listings.

### Option 1: Photo Cover (Pixabay/Unsplash/Pexels)

Search for a wide, high-quality image relevant to the topic:
1. Pixabay: `site:pixabay.com [topic] wide banner`
2. Unsplash: `site:unsplash.com [topic] wide`
3. Pexels: `site:pexels.com [topic] wide banner`

**Sizing requirements:**
| Use Case | Dimensions | Aspect Ratio |
|----------|-----------|--------------|
| Blog hero/cover | 1200x630 or 1920x1080 | 1.91:1 or 16:9 |
| Open Graph (OG) | 1200x630 | 1.91:1 (required) |
| Twitter card | 1200x628 | ~1.91:1 |

Unsplash resize: `?w=1200&h=630&fit=crop&q=80`
Pixabay/Pexels: use original if wide enough, or crop.

### Option 2: Generated SVG Cover (via /svg)

For branded or data-driven covers, generate via `/svg`:
- Text-on-gradient with title and key statistic
- Dark-mode compatible (use `currentColor` where possible)
- Include blog name/author subtle branding
- ViewBox: `0 0 1200 630` for OG compatibility

### Frontmatter Fields

```yaml
---
title: "..."
description: "..."
coverImage: "https://cdn.pixabay.com/photo/.../cover.jpg"
coverImageAlt: "Descriptive sentence about the cover image"
ogImage: "https://cdn.pixabay.com/photo/.../cover.jpg"  # Same as cover or custom OG
date: "YYYY-MM-DD"
---
```

- `coverImage`: displayed as hero at the top of the post
- `ogImage`: used for social sharing previews (Open Graph / Twitter Card)
- If only one image, use the same URL for both fields
- Alt text is required for the cover image

### When to Use Each Option

| Scenario | Recommendation |
|----------|---------------|
| General topic | Photo cover from Pixabay/Unsplash/Pexels |
| Data-heavy article | Generated SVG with key stat highlight |
| Brand-focused | Generated SVG with brand colors |
| Tutorial/how-to | Screenshot or relevant photo |

---

## Image Sourcing

### Pixabay (Preferred)
- **License**: Pixabay Content License — free for commercial use, no attribution required
- **URL**: https://pixabay.com
- **Hotlinking**: Allowed via CDN URLs

**Finding images:**
1. WebSearch: `site:pixabay.com [topic keywords]`
2. Visit the image page to get the direct CDN URL
3. Direct URL pattern: `https://cdn.pixabay.com/photo/YYYY/MM/DD/HH/MM/filename.jpg`
4. Verify: `curl -sI "<url>" | head -1` — must return HTTP 200

**Sizing**: Append query params for optimization:
- Blog hero: original size (typically 1920px wide)
- Inline images: use as-is (most are 1280px+)

### Unsplash (Alternative)
- **License**: Unsplash License — free for commercial use, no attribution required
- **URL**: https://unsplash.com
- **Hotlinking**: Required — must use their CDN

**Finding images:**
1. WebSearch: `site:unsplash.com [topic keywords]`
2. Extract photo ID from URL (e.g., `photo-1234567890123-abcdef`)
3. Build direct URL: `https://images.unsplash.com/photo-<id>?w=1200&h=630&fit=crop&q=80`
4. Verify: `curl -sI "<url>" | head -1` — must return HTTP 200

### Pexels (Fallback)
- **License**: Pexels License — free for commercial use, no attribution required
- **URL**: https://pexels.com
- **Finding**: WebSearch `site:pexels.com [topic keywords]`

### Image Usage Rules

| Rule | Requirement |
|------|-------------|
| Alt text | Required on ALL images — full descriptive sentence |
| Placement | After H2 headings, before body text |
| Distribution | Spread evenly — never cluster images |
| Count | 3-5 images per 2,000-word post |
| Relevance | Must relate to adjacent content |
| Format | WebP preferred, JPEG acceptable |

### Alt Text Guidelines
- Full descriptive sentence including topic keywords naturally
- Describe what the image shows AND its relevance to the content
- 10-125 characters
- No keyword stuffing — natural language only

Good: `Marketing team analyzing AI search traffic data on a dashboard showing citation metrics`
Bad: `SEO AI marketing blog optimization image`

### Embedding Images

**Standard Markdown:**
```markdown
![Descriptive alt text sentence](https://cdn.pixabay.com/photo/.../image.jpg)
```

**MDX (Next.js):**
```mdx
![Descriptive alt text sentence](https://cdn.pixabay.com/photo/.../image.jpg)
```

For Next.js projects, verify `next.config.ts` includes the image domain:
```typescript
images: {
  remotePatterns: [
    { protocol: 'https', hostname: 'cdn.pixabay.com' },
    { protocol: 'https', hostname: 'images.unsplash.com' },
    { protocol: 'https', hostname: 'images.pexels.com' },
  ],
}
```

**HTML:**
```html
<figure>
  <img src="https://cdn.pixabay.com/photo/.../image.jpg"
       alt="Descriptive alt text sentence"
       width="1200" height="630" loading="lazy">
  <figcaption>Photo via Pixabay</figcaption>
</figure>
```

---

## SVG Chart Integration via /svg Skill

Generate data visualizations using the `/svg` or `/svg-chart` skill.

### Chart Type Selection Guide

| Data Pattern | Best Chart Type |
|-------------|-----------------|
| Before/after comparison | Grouped bar chart |
| Ranked factors / correlations | Lollipop chart |
| Parts of whole / market share | Donut chart |
| Trend over time | Line chart |
| Percentage improvement | Horizontal bar chart |
| Distribution / range | Area chart |
| Multi-dimensional scoring | Radar chart |

**Diversity is mandatory** — never use the same chart type twice in one post.
Target 2-4 charts per 2,000-word post.

### Dark-Mode Compatible Styling

All charts must work on both dark and light backgrounds:

```
Text elements:     fill="currentColor"
Grid lines:        stroke="currentColor" opacity="0.08"
Axis lines:        stroke="currentColor" opacity="0.3"
Background:        transparent (no fill on root SVG)
Subtitle text:     fill="currentColor" opacity="0.45"
Source text:        fill="currentColor" opacity="0.35"
Label text:         fill="currentColor" opacity="0.8"
```

### Color Palette (works on dark and light)

| Color | Hex | Use Case |
|-------|-----|----------|
| Orange | `#f97316` | Primary / highest value |
| Sky Blue | `#38bdf8` | Secondary / comparison |
| Purple | `#a78bfa` | Tertiary / special category |
| Green | `#22c55e` | Quaternary / positive indicator |

For text inside colored elements: `fill="white"` with `fontWeight="800"`.

### Standard SVG Shell

```xml
<svg
  viewBox="0 0 560 380"
  style="max-width: 100%; height: auto; font-family: 'Inter', system-ui, sans-serif"
  role="img"
  aria-label="Chart description with key data point"
>
  <title>Chart Title</title>
  <desc>Description for screen readers with all key data points and source</desc>

  <!-- Chart content -->

  <text x="280" y="372" text-anchor="middle" font-size="10" fill="currentColor" opacity="0.35">
    Source: Source Name (Year)
  </text>
</svg>
```

### JSX/MDX Shell (camelCase attributes)

```jsx
<svg
  viewBox="0 0 560 380"
  style={{maxWidth: '100%', height: 'auto', fontFamily: "'Inter', system-ui, sans-serif"}}
  role="img"
  aria-label="Chart description"
>
  <title>Chart Title</title>
  <desc>Description for screen readers</desc>

  {/* Chart content */}

  <text x="280" y="372" textAnchor="middle" fontSize="10" fill="currentColor" opacity="0.35">
    Source: Source Name (Year)
  </text>
</svg>
```

### JSX Attribute Conversion (Required for MDX)

| HTML | JSX |
|------|-----|
| `stroke-width` | `strokeWidth` |
| `stroke-dasharray` | `strokeDasharray` |
| `stroke-linecap` | `strokeLinecap` |
| `text-anchor` | `textAnchor` |
| `font-size` | `fontSize` |
| `font-weight` | `fontWeight` |
| `font-family` | `fontFamily` |
| `class` | `className` |
| `style="..."` | `style={{...}}` |

### Embedding Charts

**Standard HTML:**
```html
<figure>
  <svg viewBox="0 0 560 380" ...>...</svg>
  <figcaption>Source: Source Name, Year</figcaption>
</figure>
```

**MDX:**
```mdx
<figure className="chart-container" style={{margin: '2.5rem 0', textAlign: 'center', padding: '1.5rem', borderRadius: '12px'}}>
  <svg viewBox="0 0 560 380" ...>...</svg>
</figure>
```

### Invoking /svg-chart

When generating charts, provide:
1. **Exact data values** with sources
2. **Chart type** (ensure diversity)
3. **Dark-mode styling requirements** (copy from above)
4. **Platform format**: standard SVG or JSX-compatible
5. **Save location**: `/tmp/chart-<descriptive-name>.svg`

After generation:
1. Read the generated SVG file
2. Verify `currentColor` usage (no hardcoded text colors)
3. Verify no white/light backgrounds
4. If MDX: verify camelCase attributes
5. Embed in content within figure wrapper

### Common Pitfalls

| Mistake | Impact | Fix |
|---------|--------|-----|
| `fill="#111827"` on text | Invisible on dark mode | Use `fill="currentColor"` |
| `rect fill="white"` background | Bright flash on dark mode | Remove or use transparent |
| `stroke-width` in MDX | Compilation error | Use `strokeWidth` |
| `class` in MDX | Compilation error | Use `className` |
| Same chart type twice | Visual monotony | Enforce chart diversity |
| No `role="img"` | Accessibility failure | Always include |
| No source attribution | Trust issue | Always cite data source |
