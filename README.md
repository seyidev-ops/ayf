# Adamu Yola Foundation website (v2, October 2026 redesign)

Shared styles: `assets/site.css`. Interactions (theme toggle, menus, gallery, form): `assets/site.js`. Brand files and favicons: `assets/brand/`. Event photos: `assets/photos/` (see PHOTO_ARCHIVE_STATUS.md).

---

## Earlier v1 notes

**Domain:** https://adamuyolafoundation.org  
**Build:** static HTML, CSS and vanilla JS; no npm installs, build step, database, or secret API keys.  
**Release date:** first repository commit 18 October 2026; this revision fixes nested GitHub Pages routes. Live DNS and GitHub Pages configuration require independent verification.

## Included
- Homepage, About, five dedicated programme pages, programme index, sourced news, Get involved, Contact, Privacy and a custom 404 page.
- Responsive mobile navigation, keyboard skip link, accessible labels and contrast-aware Day / Night / System appearance selector that saves the selected mode locally.
- Page-specific title, description, canonical, Open Graph, Twitter Card, structured JSON-LD, favicon, share image, robots.txt, sitemap.xml, web manifest, CNAME and nojekyll for GitHub Pages.
- Contact enquiry uses **mailto**, opening the visitor’s default email app. **No submission is stored or sent by the website.**
- Original editorial abstract SVG programme illustrations (not actual event photographs) to avoid presenting stock imagery as documentary evidence.

## Preview locally
Run `python -m http.server 8000` inside this folder, then open `http://localhost:8000`. **Do not open as file://**, because root-relative routes need a web server.

## Hosting / DNS
This project is compatible with GitHub Pages. Upload the **contents of this folder** to the published repository root and select deploy from `main` / root in Settings → Pages. Keep `CNAME` with `adamuyolafoundation.org`.

For the apex domain (`@`), GitHub Pages commonly uses A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. A `www` CNAME can point to `<your-GitHub-username>.github.io`. **Verify the addresses against current GitHub documentation before DNS changes.** Set the custom domain in GitHub Pages and enable **Enforce HTTPS** once the certificate is issued. Avoid changing NS records to GitHub; nameservers remain with the DNS provider.

## Pre-publication checks (required)
1. Verify approved foundation name and old historical name. The site uses Adamu Yola Foundation and describes Adamu Yola Ture Foundation as a historical name. Letterhead says `AYT FOUNDATION`, IT/NO `117968`; registration and legal name are **not** asserted on the public pages.
2. Verify contact: **No. 46, Billiri Street, Shongo Estate, Gombe State, Nigeria**, **+234 812 063 8440**, **adamuytfoundation@gmail.com** (from Oct 2026 foundation letterhead).
3. Get official approved brand logo. **The text AYF monogram and decorative favicon are provisional identity treatments, not authenticated organisational logos.** Swap before public launch if required.
4. Confirm the mission, vision, values, board members and approved founder biography. None are fabricated.
5. Obtain original foundation programme photographs and rights/permissions. Existing SVG drawings are illustrative.
6. Verify scholarship dates, training courses/intakes, medical outreach scope, donation processes, and school Cup rules/launch timetable. The site does **not** present open registrations or payment links without evidence.
7. Review privacy and safeguarding obligations before adding forms for children, health records or donations.
8. The Foundation Facebook URL provided earlier contains a space and was not validated, so Facebook is omitted; Instagram and LinkedIn are linked.
9. Confirm whether supporting earlier historical milestone articles remain reachable; update old-website links if retired.

## Editing instructions
- Pages are HTML files. Shared styles: `assets/styles.css`; interactive controls: `assets/main.js`.
- Copy changes to a programme should be made in its corresponding `programs/<slug>.html` and, when applicable, in the homepage/index cards.
- If you move to a CMS later, this codebase can be converted to templates/content collections.
- To revise the editorial research, see `CONTENT_AUDIT.md`.

## GitHub Pages project-subpath fix
All local href/src links must remain relative so both `seyidev-ops.github.io/ayf/` and `adamuyolafoundation.org/` work. Do not convert paths back to `/assets/...` or `/programs/...`. Social preview images and apple-touch icons are included in `assets/`.