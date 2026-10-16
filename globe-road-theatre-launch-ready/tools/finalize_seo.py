#!/usr/bin/env python3
"""Fill in canonical links, social image URLs, sitemap and robots after the actual site URL is known.
Run: python3 tools/finalize_seo.py https://YOURUSERNAME.github.io/
Or:  python3 tools/finalize_seo.py https://www.your-domain.co.uk/
"""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from datetime import date
from html import escape
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'about.html', 'productions.html', 'cyclops.html', 'right-to-arm-bears.html', 'collaborate.html']
START = '<!-- SITE-URL-METADATA:START -->'
END = '<!-- SITE-URL-METADATA:END -->'


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 tools/finalize_seo.py https://example.com/')
    base = sys.argv[1].strip().rstrip('/') + '/'
    u = urlsplit(base)
    if u.scheme != 'https' or not u.netloc or u.query or u.fragment:
        raise SystemExit('Please provide the final public HTTPS site URL ending in /')
    for name in PAGES:
        file = ROOT / name
        html = file.read_text(encoding='utf-8')
        if START in html and END in html:
            a=html.index(START);b=html.index(END,a)+len(END)
            html=html[:a]+html[b:]
        url = base if name == 'index.html' else base + name
        metadata = (
            '\n'+START+'\n'
            f'<link rel="canonical" href="{escape(url,quote=True)}">\n'
            f'<meta property="og:url" content="{escape(url,quote=True)}">\n'
            f'<meta property="og:image" content="{escape(base+"assets/social-preview.png",quote=True)}">\n'
            '<meta property="og:image:width" content="1200">\n'
            '<meta property="og:image:height" content="630">\n'
            '<meta property="og:image:alt" content="Globe Road Theatre — The Global, Made Local">\n'
            f'<meta name="twitter:image" content="{escape(base+"assets/social-preview.png",quote=True)}">\n'
            +END+'\n'
        )
        html=html.replace('</head>',metadata+'</head>')
        file.write_text(html,encoding='utf-8')
    today=date.today().isoformat()
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for name in PAGES:
        url=base if name=='index.html' else base+name
        xml+='  <url><loc>'+escape(url)+'</loc><lastmod>'+today+'</lastmod></url>\n'
    xml+='</urlset>\n'
    (ROOT/'sitemap.xml').write_text(xml,encoding='utf-8')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n',encoding='utf-8')
    print(f'Configured {len(PAGES)} pages for {base}, plus sitemap.xml and robots.txt')

if __name__=='__main__':main()
