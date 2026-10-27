#!/usr/bin/env python3
"""Scroll an infinite-scroll page and scrape every product on it."""
import time
from selenium import webdriver

CSS = "css selector"
HEIGHT = "return document.body.scrollHeight"
BOTTOM = "window.scrollTo(0, document.body.scrollHeight);"


def make_driver():
    """Return a headless Chrome driver in a 1920x1080 window."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def scroll_to_end(driver, scroll_pause):
    """Scroll to the bottom until the page height stops growing.

    After each scroll, waits up to scroll_pause seconds for the page to
    grow and moves on as soon as it does.
    """
    last_height = driver.execute_script(HEIGHT)
    while True:
        driver.execute_script(BOTTOM)
        new_height = last_height
        deadline = time.time() + scroll_pause
        while time.time() < deadline:
            time.sleep(0.2)
            new_height = driver.execute_script(HEIGHT)
            if new_height > last_height:
                break
        if new_height == last_height:
            break
        last_height = new_height


def scroll_and_scrape(url, scroll_pause=2.0):
    """Return every unique product of an infinite-scroll page.

    Scrolls until no new products load, then reads the title, price,
    description and star count of each card. A product is skipped when
    its (title, price) pair has already been seen.
    """
    driver = make_driver()
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(CSS, "div.thumbnail")
        driver.implicitly_wait(0)
        scroll_to_end(driver, scroll_pause)
        products = []
        seen = set()
        for card in driver.find_elements(CSS, "div.thumbnail"):
            title = card.find_element(CSS, "a.title").get_attribute("title")
            price = card.find_element(CSS, "h4.price").text.strip()
            if (title, price) in seen:
                continue
            seen.add((title, price))
            desc = card.find_element(CSS, "p.description").text.strip()
            stars = card.find_elements(CSS, ".ratings .ws-icon-star")
            products.append({
                "title": title,
                "price": price,
                "description": desc,
                "rating": len(stars),
            })
        return products
    finally:
        driver.quit()
