# HA BIM Standards Library

Internal Hopkins Architects Dubai documentation library: an index page (`BIM Library.dc.html`) with searchable cards linking to 14 standards pages.

## Project rules
- Source of truth: `source/*.dc.html`. Each file is a self-contained "Design Component" (template + a `<script type="text/x-dc">` logic class) that runs in the browser via `source/support.js`. Do not edit `support.js`.
- Inline styles only. No CSS classes or external stylesheets. `<helmet>` holds only fonts, `@keyframes`, body resets.
- Palette: navy `#1B3558`, blue `#2568B8`, light blue `#7EB8E8`, page bg `#DDE4ED`, body text `#2A3142`. Callouts: info `#EBF4FF/#B8D4F0`, caution `#FEF6E7/#F0D48A`, success `#E8F5EC/#A3D9B1`, danger `#FDEAEA`.
- Fonts: Montserrat (headings), Source Sans 3 (body), via Google Fonts.
- A brand restyle (Hopkins brand skill) was tried and deliberately reverted. Do not reapply unless asked.
- Version numbers are numeric only (1.0, 3.0). Never "Ver A" / "Rev C".
- Standard Revit version is **Revit 2026** unless a client specifies otherwise.
- Every page cover has: title, prepared by, date, "Version History" field, and a 2-row Version History table (current + one previous, green "Current" dot). Position is identical across pages.
- When a document changes, keep the cover version, the version-history table and the index card (`version`, `date`, `title`, `description`, `content`) consistent.
- Text the user supplied is kept verbatim.

## Index (`BIM Library.dc.html`)
- Cards live in the `docs` array in the logic class. Card order is fixed by the user, grouped by category: BIM / Revit, BIM / Document Control, BIM / Design Coordination, BIM / Project Delivery, BIM / IT, CAD Standards.
- Category filter dropdown (`catOptions`) and colours (`catColors`) must only list categories that have cards.
- Search matches title, description, tags and the `content` keyword string for each page (full-content search).
- `file` paths are relative (`./Name.html`). `index.html` must sit at the repo/site root.

## Hosting
Target: SharePoint (hopkins.ae only) or GitHub Pages / Netlify. For static hosting, serve `source/` as-is (`.dc.html` + `support.js` + `uploads/`), or produce flat standalone `.html` files. Standalone bundling was done with a Claude Design tool; in Claude Code, either serve the `.dc.html` files directly or inline assets with a bundler of your choice. Rename `BIM Library.dc.html` to `index.html` for hosting and update `file:` links if you rename pages.
