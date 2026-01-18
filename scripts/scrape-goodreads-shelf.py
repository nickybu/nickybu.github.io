import requests
import xml.etree.ElementTree as ET
import json
import os
import re

def clean_html(text):
    """Remove HTML tags from text"""
    return re.sub(r'<[^>]+>', '', text)

def scrape_goodreads_shelf(user_id: str, shelf: str):
    """Fetch books from Goodreads RSS feed"""
    url = f"https://www.goodreads.com/review/list_rss/{user_id}?shelf={shelf}"
    print(f"Fetching RSS feed: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        books = []

        for item in root.findall('.//item'):
            title_elem = item.find('title')
            author_elem = item.find('author_name')

            if title_elem is not None:
                title = clean_html(title_elem.text or '').strip()
                author = clean_html(author_elem.text or '').strip() if author_elem is not None else ''

                if title:
                    books.append({
                        'title': title,
                        'author': author
                    })

        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)

        # Save to JSON with pretty printing
        with open('data/currently_reading.json', 'w', encoding='utf-8') as f:
            json.dump({"books": books}, f, ensure_ascii=False, indent=2)

        return books

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return []

if __name__ == "__main__":
    books = scrape_goodreads_shelf('75434680', 'currently-reading')
    if books:
        print(f"\nFound {len(books)} books:")
        for book in books:
            print(f"  - {book['title']} by {book['author']}")
    else:
        print("No books found or an error occurred.")
