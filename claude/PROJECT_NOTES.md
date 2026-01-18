# nickybu.blog - Project Notes

## Overview
Personal website and blog built with Hugo using the PaperModX theme, deployed to GitHub Pages.

- **URL:** https://www.nickybu.blog
- **Main Branch:** develop
- **Theme:** PaperModX (git submodule)

## Directory Structure

```
├── .github/workflows/     # GitHub Actions CI/CD
├── assets/css/            # Custom CSS
├── content/               # All content
│   ├── _index.md          # Homepage
│   ├── about.md, search.md, archives.md
│   └── garden/            # Main content section
│       ├── 35mm/          # Film photography gallery
│       ├── bookshelf.md   # Reading list
│       └── now.md         # Now page
├── data/                  # Data files (JSON, CSV)
├── layouts/               # Custom layouts & shortcodes
├── scripts/               # Automation scripts
└── config.yml             # Main configuration
```

## Key Config Settings

- **Primary section:** garden
- **Theme features:** TOC (right side), InstantClick, ImageZoom
- **Analytics:** Custom oishii.js
- **Markdown:** Goldmark with unsafe HTML allowed
- **Code highlighting:** Dracula theme

## Custom Layouts

- `layouts/_default/single.html` - Main article template
- `layouts/garden/35mm/list.html` - Photo gallery
- `layouts/shortcodes/currently-reading-list.html` - Book list from data file
- `layouts/shortcodes/raw-html.html` - Inline HTML

## Data Files

- `data/currently_reading.json` - Books (auto-updated by Goodreads scraper)
- `data/movies-to-watch.csv` - IMDB watchlist export

## Adding New Pages

1. Create `content/pagename.md` with frontmatter
2. For custom layout: add `layout: layoutname` to frontmatter
3. Create layout at `layouts/_default/layoutname.html`
4. Add to menu in config.yml if needed

## Build

- **Local:** `hugo server -D` or `./build.sh`
- **CI/CD:** GitHub Actions builds on push to develop, deploys to GitHub Pages
- **Hugo version:** 0.148.2
