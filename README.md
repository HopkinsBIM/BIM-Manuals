# Handoff: HA BIM Standards Library

## Overview
A documentation site for Hopkins Architects Dubai's BIM standards: one searchable index plus 13 manual-style pages (Revit setup, naming, LOD, collaboration, clash coordination, IT housekeeping); 15 cards in total, 2 still to be written. This is a content/documentation project, not an app. Continue it in Claude Code by editing the source files and re-hosting.

## About the files
`source/*.dc.html` are the working HTML pages (high-fidelity, final styling and content). They are runnable as-is in a browser alongside `source/support.js` and `source/uploads/`. They are not a framework app; keep extending them in this format, or migrate to a static-site generator if preferred. Read `CLAUDE.md` first: it holds the style and consistency rules.

## Fidelity
High-fidelity. Colours, type, spacing and copy are final.

## Pages
| Card order | Page (file) | Category | Version | Date |
|---|---|---|---|---|
| 1 | HA Starting A New Revit Model | BIM / Revit | 1.0 | Nov 2025 |
| 2 | HA Datum and Grid Naming | BIM / Revit | 3.0 | Nov 2024 |
| 3 | HA Sheet and Model Structure | BIM / Revit | 1.0 | June 2026 |
| 4 | HA Naming Conventions | BIM / Document Control | 3.0 | Nov 2024 |
| 5 | HA Areas and Colour Schemes | BIM / Revit | 1.0 | Jun 2026 |
| 6 | HA Rooms and Room Data Sheets | BIM / Revit | 1.0 | Jun 2026 |
| 7 | Revit Best Practices (card: Lessons Learnt) | BIM / Revit | 1.0 | June 2026 |
| 8 | HA LOD Definitions | BIM / Project Delivery | 1.0 | Jun 2026 |
| 9 | HA Bluebeam Studio Guide | BIM / Design Coordination | 1.0 | Jun 2025 |
| 10 | BEP template (card only, `file: null`) | BIM / Project Delivery | — | — |
| 11 | HA ACC Guide (DC Validation – OCR in Autodesk Forma) | BIM / Document Control | 1.0 | Jul 2026 |
| 12 | HA Clearing Disk Space | BIM / IT | 1.0 | July 2026 |
| 13 | HA Model Collaboration | BIM / Design Coordination | 1.0 | Jul 2026 |
| 14 | HA Clash Coordination Matrix | BIM / Design Coordination | 1.0 | Jul 2026 |
| 15 | CAD Layer Standards (card only, `file: null`) | CAD Standards | — | — |

Card order and categories above match the `docs` array in `BIM Library.dc.html` (updated Oct 2026). The `file:` links in the array point to `./Name.html`; the sources are `Name.dc.html`, so they resolve only once the pages are bundled or renamed for hosting.

The `docs` array in `BIM Library.dc.html` remains the authoritative source for order and metadata.

## Shared page structure
1. **Cover** (min-height 100vh, bg `#1B3558`, blueprint grid SVG at 7% opacity, decorative rings top-right): logo top-left (`uploads/Hopkins Architects Right Aligned_White.png`), category eyebrow (`#7EB8E8`, 11px caps), H1 (Montserrat 800, 44px, white), subtitle (`#A8C8E8`, 16px), meta row (Prepared By / Date / Version History), 2-row Version History table, bottom strip with firm line.
2. **Body** (`max-width 8.5in`, white, padding ~0.75in): boxed section banners (Montserrat 800, 13.5px caps, bg `#E0E3EC`, border `#9AA3B8`), numbered steps, callouts, tables, annotated images.
3. **Footer** line: "Hopkins Architects Dubai Limited · BIM Standards Library".

## Index page behaviour
- Search box filters cards live across title, description, tags and the page's `content` keyword string.
- Category dropdown filters by category; colours from `catColors()`.
- Card shows category pill, title, description, version, date, and opens the page via its `file` path.
- Tweak props are declared on the component's `data-props`.

## Design tokens
Navy `#1B3558` · Blue `#2568B8` · Light blue `#7EB8E8` · Cover subtitle `#A8C8E8` · Page bg `#DDE4ED` · Body text `#2A3142` · Row border `#E8EBF0` · Card border `#D6DDE8` · Alt row `#F8F9FB`/`#F4F7FB`.
Info `#EBF4FF`/`#B8D4F0` · Caution `#FEF6E7`/`#F0D48A` (text `#7A4A10`) · Success `#E8F5EC`/`#A3D9B1` · Danger `#C52E24` on `#FDEAEA` · Category colours: Revit `#1B3558`, Doc Control `#7B3FAA`, Design Coordination `#0E7490`, Project Delivery `#1F7A3B`, IT `#5A6B7C`, CAD `#C52E24`.
Type: Montserrat 400–800 headings/labels, Source Sans 3 body 15px/1.7.

## Assets
`source/uploads/` holds only images referenced by the pages: Hopkins logo, Revit screenshots (user-supplied), annotated model images for Sheet & Model Structure (Scenarios A/B), LOD progression images (wall, steel, HVAC). `source_documents/` holds the original PDFs/DOCX/XLSX the pages were built from. The clash page links `./Clash_Coordination_Matrix.xlsx` for download; that file lives in `source/` and must stay beside the page when hosting.

## Policy notice (all pages)
Every cover (above the footer strip) and the index header carry: "With effect from 15 Oct 2026 All new projects shall be initiated in Revit 2026 unless there is Client requirement to use older versions." Keep it on any new page.

## Known items for follow-up
- Rename/copy `BIM Library.dc.html` to `index.html` at the site root.
- Keep `Clash_Coordination_Matrix.xlsx` beside the clash page for the download link.
- LOD and Sheet & Model Structure pages are heavy (large images); consider compressing.
- Hosting: SharePoint needs custom scripting allowed to render HTML; alternatively Netlify + Cloudflare Access restricted to `@hopkins.ae`.
- Discussed but not done: password/email gating.
