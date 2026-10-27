#!/usr/bin/env python3
"""Scrape the products of a static category page with Selenium."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def make_driver():
    """Return a headless Chrome driver in a 1920x1080 window."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def scrape_products(url):
    """Return the products of a category page as a list of dicts.

    Each dict holds the title, price, description and star rating.
    """
    driver = make_driver()
    try:
        driver.implicitly_wait(10)
        driver.get(url)
        time.sleep(1)
        products = []
        for card in driver.find_elements(By.CSS_SELECTOR, ".thumbnail"):
            link = card.find_element(By.CSS_SELECTOR, "a.title")
            price = card.find_element(By.CSS_SELECTOR, "h4.price")
            desc = card.find_element(By.CSS_SELECTOR, "p.description")
            stars = card.find_element(By.CSS_SELECTOR,
                                      ".ratings p[data-rating]")
            products.append({
                "title": link.get_attribute("title"),
                "price": price.text.strip(),
                "description": desc.text.strip(),
                "rating": int(stars.get_attribute("data-rating")),
            })
        return products
    finally:
        driver.quit()


scrape_products_list = scrape_products
