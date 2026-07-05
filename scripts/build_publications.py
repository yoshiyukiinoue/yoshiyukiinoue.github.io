#!/usr/bin/env python3
"""SciX (ADS) 公開ライブラリ → リンク付き論文リスト(Markdown)生成

- 個別論文ページは作らず、/publication/ に年ごとのフラットなリストを生成
- トップページの <!-- RECENT_PUBS:START/END --> マーカー間を直近5本で更新
使い方:
    export ADS_DEV_KEY=xxxx
    python3 scripts/build_publications.py
"""
import json
import os
import re
import sys
import urllib.request

API = "https://api.adsabs.harvard.edu/v1"
LIB_ALL = "r0HdPWXHQKOV8kUwuZDq5Q"  # 全論文ライブラリ
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_AUTHORS = 5
BOLD_NAME = "Inoue"  # この姓を太字にする


def api_get(path):
    req = urllib.request.Request(
        f"{API}{path}",
        headers={"Authorization": f"Bearer {os.environ['ADS_DEV_KEY']}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def fetch_docs():
    bibcodes = api_get(f"/biblib/libraries/{LIB_ALL}?rows=2000")["documents"]
    fl = "bibcode,title,author,year,pub,volume,page,doi,identifier"
    req = urllib.request.Request(
        f"{API}/search/bigquery?q=*:*&fl={fl}&rows=2000&sort=date+desc",
        data=("bibcode\n" + "\n".join(bibcodes)).encode(),
        headers={"Authorization": f"Bearer {os.environ['ADS_DEV_KEY']}",
                 "Content-Type": "big-query/csv"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)["response"]["docs"]


def short_authors(authors):
    """'Lastname, F. M.' のリストを短縮表記に。Inoue は太字。"""
    def fmt(a):
        parts = a.split(", ")
        last = parts[0]
        ini = " ".join(w[0] + "." for w in parts[1].split()) if len(parts) > 1 else ""
        s = f"{last}, {ini}".strip().rstrip(",")
        return f"**{s}**" if last == BOLD_NAME else s
    out = [fmt(a) for a in authors[:MAX_AUTHORS]]
    if len(authors) > MAX_AUTHORS:
        out.append("et al.")
    return ", ".join(out)


def find_arxiv(identifiers):
    for i in identifiers or []:
        m = re.match(r"^arXiv:(.+)$", i)
        if m:
            return m.group(1)
    return None


def entry_md(d):
    title = (d.get("title") or ["(no title)"])[0]
    title = re.sub(r"<[^>]+>", "", title)  # strip raw HTML (e.g. ADS erratum links)
    authors = short_authors(d.get("author") or [])
    year = d.get("year", "")
    pub = d.get("pub", "")
    vol = d.get("volume")
    page = (d.get("page") or [None])[0]
    ref = f"*{pub}*" if pub else ""
    if vol:
        ref += f" {vol}"
    if page:
        ref += f", {page}"
    links = [f"[ADS](https://ui.adsabs.harvard.edu/abs/{d['bibcode']})"]
    arxiv = find_arxiv(d.get("identifier"))
    if arxiv:
        links.append(f"[arXiv](https://arxiv.org/abs/{arxiv})")
    doi = (d.get("doi") or [None])[0]
    if doi:
        links.append(f"[DOI](https://doi.org/{doi})")
    return f"- {authors} ({year}). {title}. {ref}. {' / '.join(links)}"


def page_md(docs, lang):
    title = "論文" if lang == "ja" else "Publications"
    note = ("リストは SciX (ADS) 公開ライブラリから自動生成されています。"
            if lang == "ja" else
            "This list is auto-generated from our public SciX (ADS) library.")
    data_note = ("論文で公開している数値データは [データ公開](../downloads/) ページにまとめています。"
                 if lang == "ja" else
                 "Numerical data from our papers are available on the [Downloads](../downloads/) page.")
    lib = f"https://scixplorer.org/public-libraries/{LIB_ALL}"
    lines = ["---", f"title: {title}", "---", "",
             f"{note} [SciX]({lib})", "", data_note, ""]
    cur = None
    for d in docs:
        y = d.get("year", "????")
        if y != cur:
            lines += ["", f"## {y}", ""]
            cur = y
        lines.append(entry_md(d))
    lines.append("")
    return "\n".join(lines)


def update_homepage(docs, path, n=5):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^(\s*)<!-- RECENT_PUBS:START -->.*?^(\s*)<!-- RECENT_PUBS:END -->",
                  text, re.S | re.M)
    if not m:
        print(f"  skip(マーカーなし): {path}")
        return
    indent = m.group(1)
    body = "\n".join(indent + entry_md(d) for d in docs[:n])
    new = (f"{indent}<!-- RECENT_PUBS:START -->\n{body}\n"
           f"{indent}<!-- RECENT_PUBS:END -->")
    open(path, "w", encoding="utf-8").write(text[:m.start()] + new + text[m.end():])
    print(f"  updated: {path}")


def main():
    docs = fetch_docs()
    print(f"{len(docs)} publications fetched")
    for lang in ("ja", "en"):
        out = os.path.join(SITE, "content", lang, "publication", "index.md")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page_md(docs, lang))
        print(f"  wrote: {out}")
        update_homepage(docs, os.path.join(SITE, "content", lang, "_index.md"))


if __name__ == "__main__":
    main()
