#!/usr/bin/env python3
"""Scrape every page of quotes.toscrape.com by following the Next links."""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic

DELAY = 0.5


def scrape_paginated(base_url):
    """Return the quotes of every page, following the Next links.

    Waits DELAY seconds between pages so the server is not overloaded.
    """
    quotes = []
    url = base_url
    while url:
        quotes.extend(scrape_basic(url))
        soup = BeautifulSoup(fetch_html(url), "html.parser")
        link = soup.select_one("li.next > a")
        if link is None:
            url = None
        else:
            url = parse.urljoin(url, link.get("href"))
            time.sleep(DELAY)
    return quotes
