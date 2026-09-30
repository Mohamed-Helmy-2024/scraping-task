
import csv
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_FILE = "books.csv"


def scrape_page(page_number):
    url = BASE_URL.format(page_number)
    soup = BeautifulSoup(requests.get(url, timeout=15).text, "html.parser")
    books = []

    for product in soup.select("article.product_pod"):
        link = product.select_one("h3 a")
        rating = ["One", "Two", "Three", "Four", "Five"].index(product.select_one("p.star-rating")["class"][1]) + 1
        books.append({
            "title": link["title"].strip(),
            "price": float(re.sub(r"[^0-9.]", "", product.select_one("p.price_color").get_text(strip=True))),
            "rating": rating,
            "in_stock": "in stock" in product.select_one("p.instock.availability").get_text(" ", strip=True).lower(),
            "url": urljoin(url, link["href"]),
        })

    return books


def main():
    rows = [book for page in range(1, 6) for book in scrape_page(page)]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "rating", "in_stock", "url"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} books to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()