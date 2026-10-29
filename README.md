# Adamu Yola Foundation website

Static site (HTML, CSS, vanilla JS) served by GitHub Pages. No build step is needed to publish.

## Structure
- Pages: `index.html`, `about.html`, `programs/` (five programmes and Past Initiatives), `news.html`, `gallery.html`, `get-involved.html`, `contact.html`, `privacy.html`, `terms.html`, `404.html`. `stories.html` redirects to `news.html`.
- Styles: `assets/site.css`. Interactions (theme toggle, menus, gallery, contact form): `assets/site.js`.
- Brand (2026 logo): `assets/brand/` holds the layered animated mark (`mark/`), wordmarks and favicons.
- Programme badges: `assets/unity-cup-badge*.webp` (10th anniversary) and `assets/principals-cup-crest*.webp`.
- Event photos: `assets/photos/` (see `PHOTO_ARCHIVE_STATUS.md`).

## Contact details used on the site
adamuytfoundation@gmail.com, +234 812 063 8440, No. 46 Billiri Street, Shongo Estate, Gombe State.

## Editing
Keep all links relative so the site works at both `seyidev-ops.github.io/ayf/` and a custom domain. Preview locally with `python -m http.server 8000` and open `http://localhost:8000`.
