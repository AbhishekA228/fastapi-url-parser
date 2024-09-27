import requests
from bs4 import BeautifulSoup

# Function to extract body text from a given URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    body_text = soup.get_text()
    return body_text

# Function to chunk the text into smaller pieces
def chunk_text(text, chunk_size=512):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
