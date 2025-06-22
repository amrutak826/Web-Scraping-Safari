# Web Scraping Safari

This project scrapes the top 5 trending GitHub repositories and saves their names and links into a CSV file using Python.

## 💡 Solution, Approach & Challenges

In this project, we built a Python-based web scraper to extract the top 5 trending repositories from GitHub’s [Trending page](https://github.com/trending). Using the `requests` library, we fetched the HTML content of the page, and with `BeautifulSoup`, we parsed and navigated the HTML to locate repository names and their corresponding links. The relevant data was then structured and exported to a CSV file with two columns: `Repository Name` and `Link`. This ensures a clean, organized dataset that can be reused or analyzed further.

One key challenge was adapting the scraper to the current structure of GitHub’s HTML, which occasionally changes. Initially, attempts to extract data using outdated tags like `repo.h1.a` led to `AttributeError`s, as those elements were no longer part of the page structure. To resolve this, we used a more resilient approach by targeting the `<h2>` tag and locating its anchor child. This highlighted the importance of writing adaptable, fault-tolerant scraping code that gracefully handles minor frontend changes.

## ✨ Notable Features & Highlights

- **Top 5 Trending Repositories**: The scraper intelligently limits output to the top 5 results, avoiding data overload while showcasing the most relevant repositories.
- **Automated CSV Generation**: Data is saved in a structured CSV format, making it easy to import into Excel, databases, or visualization tools.
- **Modular and Reusable**: With minimal dependencies (`requests`, `beautifulsoup4`), the code can be reused for other scraping tasks or extended to extract more metadata like stars or languages.

## How to Run
```bash
pip install -r requirements.txt
python scrape_trending.py
```
