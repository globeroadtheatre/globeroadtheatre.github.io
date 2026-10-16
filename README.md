# Globe Road Theatre — website launch kit

A bespoke, static website made for Globe Road Theatre. No WordPress, website-builder plan, cookie banner, analytics account, paid hosting, or build tooling required.

**Artistic positioning:** The Global, Made Local. / International stories that weave culture and community on stage and off.

## What is included

- `index.html` — homepage and artistic positioning
- `about.html` — company ethos, practice and Artistic Lead Mark Diaz
- `productions.html` — work overview
- `cyclops.html` — 2026 production and credits
- `right-to-arm-bears.html` — honest, clearly marked work-in-development page
- `collaborate.html` — introductions and enquiries
- `404.html` — friendly not-found page (not indexable)
- `styles.css`, `script.js` — lightweight, responsive presentation
- `assets/` — original CSS-style graphics, social image, favicon and touch icon
- `robots.txt`, `.nojekyll`, `site.webmanifest` — site delivery files
- `tools/finalize_seo.py` — one-time helper to add the correct public URL after it is known

## Publish on GitHub Pages (free)

**1.** Log in to GitHub under the account that should own the theatre website. Copy its exact username. If the username is `globeroadtheatre`, the simplest repository name is `globeroadtheatre.github.io`.

**2.** On GitHub, choose **New repository**. Name it `YOURUSERNAME.github.io` — substituting your exact account name. Select **Public**; leave the optional **Add a README file** box unchecked; then choose **Create repository**.

**3.** Extract the ZIP locally. Open the extracted folder. On the empty repository page choose **uploading an existing file** (or **Add file → Upload files**), and upload the **contents** of this folder — not the ZIP and not a nested parent folder. The file `index.html` MUST be directly at the top of the repository, beside `styles.css`. The `assets/` folder must also be uploaded with its images. Click **Commit changes**.

**4.** Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then `main` and `/(root)`. Click **Save**. Wait a few minutes and refresh Pages settings to find **Visit site**.

**5.** Your address will be `https://YOURUSERNAME.github.io/`. Test homepage and internal pages on a phone and computer. If the Pages section displays an error, look at the **Actions** tab for the deployment error message.

> Alternative: if the repository is named `globe-road-theatre` rather than `YOURUSERNAME.github.io`, the site URL will usually be `https://YOURUSERNAME.github.io/globe-road-theatre/`. Internal links in this package are relative and work in either arrangement. Prefer the username-based repository for the shortest public URL.

## Finish technical SEO (once your live URL is known)

The page titles, descriptions, accessible headings, UK location targeting, internal links, natural language search terms and `PerformingGroup` structured data are already in place. **Absolute canonical and social image URLs, and an XML sitemap, cannot be finalized responsibly until the website's precise public URL is known.**

After publishing, share your real URL with ChatGPT and request a finalized SEO-ready package. Or run this one-time command on a computer with Python 3:

```bash
python3 tools/finalize_seo.py https://YOURUSERNAME.github.io/
```

Re-upload the updated HTML files, `robots.txt`, and new `sitemap.xml`. Then register the actual public URL at [Google Search Console](https://search.google.com/search-console/about) and submit the sitemap (e.g., `https://YOURUSERNAME.github.io/sitemap.xml`). **Indexing and ranking are not instantaneous or guaranteed.**

If you buy a `.co.uk` or `.uk` domain, configure it in **Settings → Pages → Custom domain**, follow GitHub's DNS instructions, enable HTTPS, and then re-run the SEO helper with the final custom-domain URL.

## Adding real photography later

This version intentionally uses authored graphical artwork rather than fake or unlicensed show photography. You can launch now.

Recommended future photos:

1. A strong horizontal hero image of *The Cyclops of East London*, showing performance with an audience or public space.
2. Two or three production photographs for the Cyclops page, with photographer credit.
3. A natural, professional photograph of Mark Diaz for the Artistic Lead section.
4. Workshop or rehearsal images showing an ensemble at work.

Use photographer-approved files with permission for web publication. Export as JPEG or WebP, ideally at around 1600 px wide and under ~350 KB for full-width photos where practical. Filenames should be descriptive (`cyclops-east-london-pub-theatre.webp`) and meaningful alternative text should describe the actual scene. Keep the original photographer credit visible.

## Key editorial things to confirm before publication

- Cast and creative credits for *The Cyclops of East London* reflect the company-provided working record; double-check spellings and permissions.
- The company Instagram account is linked as the current public enquiry contact. Replace/add a professional company email once one is available.
- *Right to Arm Bears* is marked **in development** and no future performance dates are invented.
- Mark Diaz's selected other directing work is in his biography, not misrepresented as Globe Road Theatre productions.
- Make sure you have rights to any future photographs you add.

## Ongoing maintenance

Edit the text in the relevant `.html` file and commit changes on GitHub. The site automatically republishes from `main`. Because there is no CMS, image upload and text edits happen through the GitHub web editor or desktop app.

© Globe Road Theatre. Developed as a lightweight independent website.
