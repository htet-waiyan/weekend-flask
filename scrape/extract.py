
from typing import List
import requests
import html2text
from bs4 import BeautifulSoup

def extract_url(url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        unwanted_tags = ["footer", "header", "head", "nav"]
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        for tag_name in unwanted_tags:
            for unwanted_tag in soup.find_all(tag_name):
                unwanted_tag.extract()
        
        content = html2text.html2text(str(soup))
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error extracting content from url: {url}, error: {e}")
        return e

def scrape_urls(urls: List[str]):
    contents = []
    for url in urls:
        try:
            print(f"scraping from {url}")
            content = extract_url(url)
            contents.append(content)
        except requests.exceptions.RequestException as e:
            print(e)
            continue
        
    return contents