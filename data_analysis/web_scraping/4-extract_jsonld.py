#!/usr/bin/env python3
"""Extract quotes from the JSON-LD blocks embedded in a web page."""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Return the Quote objects found in a page's JSON-LD as dicts.

    Reads every <script type="application/ld+json"> block, skips the
    ones that are not valid JSON and keeps the objects of type Quote.
    """
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    quotes = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except ValueError:
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict) or item.get("@type") != "Quote":
                continue
            author = item.get("author", {})
            if isinstance(author, dict):
                author = author.get("name")
            tags = item.get("keywords", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]
            quotes.append({"text": item.get("text"),
                           "author": author,
                           "tags": tags})
    return quotes
