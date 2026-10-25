#!/usr/bin/env python3
"""Collect every quote from the JSON API of quotes.toscrape.com."""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Return the quotes of every API page as a list of dicts.

    Starts at page one and keeps going while the API reports has_next.
    """
    quotes = []
    page = 1
    has_next = True
    while has_next:
        url = "{}/api/quotes?page={}".format(base_url.rstrip("/"), page)
        data = json.loads(fetch_html(url))
        for item in data.get("quotes", []):
            author = item.get("author", {})
            if isinstance(author, dict):
                author = author.get("name")
            quotes.append({"text": item.get("text"),
                           "author": author,
                           "tags": item.get("tags", [])})
        has_next = data.get("has_next", False)
        page += 1
    return quotes
