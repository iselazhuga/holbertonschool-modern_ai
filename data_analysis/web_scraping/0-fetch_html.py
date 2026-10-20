#!/usr/bin/env python3
"""Fetch the HTML of a web page."""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a page and return its HTML as text.

    Raises an exception for any HTTP status code of 400 or more.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
