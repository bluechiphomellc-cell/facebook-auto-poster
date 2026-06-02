#!/usr/bin/env python3
"""Generate blog post HTML files from a list of post data + markdown content.

One-shot generator. Run locally when adding posts:
    python3 generate_posts.py

Outputs files into blog/posts/. The daily GitHub Actions cron then handles
publishing them as their dates arrive via build_blog.py.
"""

import datetime
import html
import re
from pathlib import Path

POSTS_DIR = Path(__file__).parent / "blog" / "posts"


# ── Markdown converter (tiny, just what we use) ──────────────────────────────

def md_to_html(md):
    lines = md.strip().split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
            i += 1
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
            i += 1
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:].rstrip())}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
        elif re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i].rstrip()))}</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
        else:
            buf = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "-")) and not re.match(r"^\d+\. ", lines[i]):
                buf.append(lines[i].rstrip())
                i += 1
            out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n            ".join(out)


def inline(text):
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


# ── HTML template ────────────────────────────────────────────────────────────

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-TTQ743NJ');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18052201570"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','AW-18052201570');</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Facebook Auto Poster</title>
    <meta name="description" content="{excerpt}">
    <meta name="article:published_time" content="{date}">
    <meta name="read-time" content="{read_time}">
    <link rel="canonical" href="https://facebook-auto-poster.com/blog/posts/{slug}.html">
    <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{excerpt}">
    <meta property="og:image" content="https://facebook-auto-poster.com/assets/og-image.jpg">
    <meta property="og:url" content="https://facebook-auto-poster.com/blog/posts/{slug}.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Facebook Auto Poster">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{excerpt}">
    <meta name="twitter:image" content="https://facebook-auto-poster.com/assets/og-image.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "description": "{excerpt}",
      "image": "https://facebook-auto-poster.com/assets/og-image.jpg",
      "datePublished": "{date}",
      "dateModified": "{date}",
      "author": {{ "@type": "Person", "name": "Brandon", "url": "https://facebook-auto-poster.com/about.html" }},
      "publisher": {{ "@type": "Organization", "name": "Lakeside Management Group LLC", "logo": {{ "@type": "ImageObject", "url": "https://facebook-auto-poster.com/assets/logo.png" }} }},
      "mainEntityOfPage": {{ "@type": "WebPage", "@id": "https://facebook-auto-poster.com/blog/posts/{slug}.html" }}
    }}
    </script>
    <link rel="stylesheet" href="/assets/blog-post.css">
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TTQ743NJ" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <nav class="nav">
        <div class="nav-inner">
            <a href="/" class="nav-logo"><img src="/assets/logo.png" alt="Facebook Auto Poster"></a>
            <div class="nav-links" id="navLinks">
                <a href="/">Home</a>
                <a href="/about.html">About</a>
                <a href="/instructions.html">Instructions</a>
                <a href="/blog/" class="active">Blog</a>
                <a href="/download.html">Download</a>
                <div class="nav-cta"><a href="https://autoposter.lemonsqueezy.com/checkout/buy/e6ca31f6-2cf8-4eab-8cc9-350197666564" class="nav-cta-btn">Get Started</a></div>
            </div>
            <div class="nav-mobile-toggle" onclick="document.getElementById('navLinks').classList.toggle('open')"><span></span><span></span><span></span></div>
        </div>
    </nav>
    <article>
        <div class="article-header">
            <div class="breadcrumb"><a href="/blog/">Blog</a> &nbsp;/&nbsp; {category}</div>
            <h1>{title}</h1>
            <div class="article-meta">{date_display} &middot; {read_time}</div>
        </div>
        <div class="article-body">
            {content_html}
        </div>
        <div class="article-cta">
            <h3>{cta_title}</h3>
            <p>{cta_body}</p>
            <a href="/download.html" class="article-cta-btn">Start Free Trial</a>
        </div>
    </article>
    <footer class="footer">
        <div class="footer-inner">
            <span class="footer-copy">&copy; 2026 Lakeside Management Group LLC. All rights reserved.</span>
            <div class="footer-links">
                <a href="/privacy.html">Privacy Policy</a>
                <a href="/terms.html">Terms of Service</a>
                <a href="/refund.html">Refund Policy</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""


def generate(post):
    date_obj = datetime.date.fromisoformat(post["date"])
    content_html = md_to_html(post["content"])
    rendered = TEMPLATE.format(
        slug=post["slug"],
        title=post["title"],
        excerpt=post["excerpt"],
        date=post["date"],
        date_display=date_obj.strftime("%B %-d, %Y"),
        read_time=post.get("read_time", "6 min read"),
        category=post.get("category", "Guide"),
        content_html=content_html,
        cta_title=post.get("cta_title", "Spend less time scheduling"),
        cta_body=post.get("cta_body", "Facebook Auto Poster schedules across all your pages in one batch. 7-day free trial."),
    )
    (POSTS_DIR / f"{post['slug']}.html").write_text(rendered)


def run(posts):
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for p in posts:
        generate(p)
        print(f"Generated: {p['slug']}.html ({p['date']})")
