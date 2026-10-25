#!/usr/bin/env python3
"""Scrape the quotes on the first page of quotes.toscrape.com."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Return the quotes on a page as a list of dicts.

    Each dict holds the quote text, its author and its list of tags.
    """
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    quotes = []
    for block in soup.select("div.quote"):
        text = block.select_one("span.text").get_text(strip=True)
        author = block.select_one("small.author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.select("a.tag")]
        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes
