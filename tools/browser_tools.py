import json
import os

import requests
from crewai.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools():

  @staticmethod
  @tool("Scrape and summarize website content")
  def scrape_and_summarize_website(website: str) -> str:
    """Scrape and summarize website content.
    
    Args:
        website: The URL of the website to scrape
        
    Returns:
        str: The scraped and summarized content from the website
    """
    try:
        url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
        payload = json.dumps({"url": website})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        
        if len(content) > 2000:
            return content[:2000] + "... (content truncated)"
        return content
    except Exception as e:
        return f"Error scraping website: {str(e)}"