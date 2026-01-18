from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import os
import time

def convert_author_name(name):
    """Convert 'Surname, Firstname' format to 'Firstname Lastname'"""
    if ',' in name:
        parts = name.split(',', 1)  # Split into max 2 parts
        return f"{parts[1].strip()} {parts[0].strip()}"
    return name

def scrape_goodreads_shelf(shelf: str):
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        url = f"https://www.goodreads.com/review/list/75434680-nicky?shelf={shelf}"
        driver.get(url)
        
        # Wait for the table to load
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bookalike')))
        
        # Let the JavaScript load completely
        time.sleep(2)
        
        books = []
        rows = driver.find_elements(By.CLASS_NAME, 'bookalike')
        
        for row in rows:
            try:
                title_element = row.find_element(By.CLASS_NAME, 'title')
                title = title_element.find_element(By.TAG_NAME, 'a').text.strip()
                author_element = row.find_element(By.CLASS_NAME, 'author')
                author = author_element.find_element(By.TAG_NAME, 'a').text.strip()
                author = convert_author_name(author)
                books.append({
                    'title': title,
                    'author': author
                })
            except Exception as e:
                print(f"Error processing row: {e}")
                continue

        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Save to JSON with pretty printing
        with open('data/currently_reading.json', 'w', encoding='utf-8') as f:
            json.dump({"books": books}, f, ensure_ascii=False, indent=2)
            
        return books

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
        
    finally:
        driver.quit()

if __name__ == "__main__":
    books = scrape_goodreads_shelf('currently-reading')
    if books:
        print("\nBooks found:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found or an error occurred.")
