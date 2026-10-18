# Publication and domain checklist

Target: **https://adamuyolafoundation.org** (canonical, without `www`). The website archive is a complete static site and is **not yet hosted**.

## 1. Put the files on a host

For GitHub Pages:
1. Create or choose a GitHub repository and upload all files from this ZIP into the **repository root**, not an additional `ayf-site/` folder.
2. Open **Repository → Settings → Pages**, choose Deploy from a branch, then select `main` and `/ (root)`.
3. Enter `adamuyolafoundation.org` as the Custom domain. The included `CNAME` already contains the domain.
4. Wait for GitHub Pages to publish, then turn on **Enforce HTTPS** when it becomes available.

Other static web hosts may work too; adapt DNS and rewrite behavior to your provider.

## 2. Configure DNS at the registrar or DNS provider

Do not switch the domain's authoritative nameservers to GitHub; GitHub Pages does **not** supply domain registration nameservers. Keep your DNS hosting provider and add records there.

| Type | Host/Name | Value |
|------|-----------|-------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `<YOUR-GITHUB-USER>.github.io` |

Replace the placeholder with the **actual repository owner** (username or organisation). Remove conflicting apex A/AAAA/ALIAS records and any conflicting `www` CNAME only after understanding the existing service. GitHub also documents supported IPv6 AAAA records.

Source: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

DNS changes can take time; secure HTTPS only after DNS resolves and the certificate is ready.

## 3. SEO activation

- Canonical tags, Open Graph preview, per-page titles/descriptions, `sitemap.xml`, `robots.txt`, and NGO/WebSite schema are already set for `adamuyolafoundation.org`.
- After publication, open `https://adamuyolafoundation.org/sitemap.xml` and `https://adamuyolafoundation.org/robots.txt` and verify both load.
- Add/verify the domain property in **Google Search Console**, then submit `https://adamuyolafoundation.org/sitemap.xml`.
- If Bing discovery is important, submit the sitemap in Bing Webmaster Tools as well.
- Consider a 301 redirect from **aytfoundation.org** only if you control that domain, the content/canonical identity is approved, and you can configure its current host or registrar correctly.
- Do not turn on analytics or visitor tracking without an actual owner account, a measurement plan and an updated privacy notice.

## 4. Content approval

Confirm the foundation's official name/logo, contact information, registration details, mission/vision, schools competition status, programme intake status and photo rights before a public launch. Refer to `CONTENT_AUDIT.md`.

## 5. Smoke test after deploy

Check all internal pages, mobile menu, Day/Night/System switch, SEO tags, external historical source links, email hand-off, certificate, and pages at both `www` and non-`www` domains. Where the enquiry form is used, the visitor must finish sending the drafted message in their own email app.