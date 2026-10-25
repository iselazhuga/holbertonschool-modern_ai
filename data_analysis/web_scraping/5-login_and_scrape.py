#!/usr/bin/env python3
"""Log in to quotes.toscrape.com and scrape the quotes behind the login."""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in with a session and return the quotes of the home page.

    Reads the CSRF token from the login form, posts the credentials and
    then scrapes the quotes page with the same session cookies.
    """
    session = requests.Session()
    response = session.get(login_url, timeout=10)
    response.raise_for_status()
    form = BeautifulSoup(response.text, "html.parser")
    token = form.find("input", {"name": "csrf_token"})["value"]
    payload = {"username": user, "password": pwd, "csrf_token": token}
    response = session.post(login_url, data=payload, timeout=10)
    response.raise_for_status()
    home = login_url.split("/login")[0] + "/"
    response = session.get(home, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for block in soup.select("div.quote"):
        text = block.select_one("span.text").get_text(strip=True)
        author = block.select_one("small.author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in block.select("a.tag")]
        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes
