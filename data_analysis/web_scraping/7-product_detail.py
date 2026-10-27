#!/usr/bin/env python3
"""Scrape the detail page of a single product with Selenium."""
import time
from selenium import webdriver

CSS = "css selector"


def make_driver():
    """Return a headless Chrome driver in a 1920x1080 window."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def scrape_product_detail(url, delay=2.0):
    """Return the title, price, description and rating of one product.

    Opens the product page, waits delay seconds, then reads the second
    h4 of the caption as the title and counts the stars in the ratings.
    """
    driver = make_driver()
    try:
        driver.get(url)
        time.sleep(delay)
        headings = driver.find_elements(CSS, ".caption h4")
        price = driver.find_element(CSS, "h4.price")
        desc = driver.find_element(CSS, "p.description")
        stars = driver.find_elements(CSS, ".ratings .ws-icon-star")
        return {
            "title": headings[1].text.strip(),
            "price": price.text.strip(),
            "description": desc.text.strip(),
            "rating": len(stars),
        }
    finally:
        driver.quit()
