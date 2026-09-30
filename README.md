
## ***Five Lines — Part 3***

- The scraping worked as expected, with the main attention needed around parsing and normalizing price, rating, and stock values.

- I kept the implementation simple and readable while ensuring the output matched the required CSV format.

- If the site started blocking requests after 50 requests, I would reduce the request rate and add randomized delays between requests.

- I would also add retries with exponential backoff, request timeouts, and a `requests.Session()` to handle temporary failures more reliably.

- For a larger production scraper, I would add caching, structured logging, monitoring, and respect the site's crawling policies.
"# scraping-task" 
