 HEAD
# scraping.py com scraping dos 7 sites

import requests
from bs4 import BeautifulSoup

def get_latest_headline():
    try:
        resp = requests.get("https://g1.globo.com")
        soup = BeautifulSoup(resp.content, "html.parser")
        headline = soup.find("a", {"class": "feed-post-link"})
        return headline.text.strip() if headline else "Sem manchetes encontradas"
    except:
        return "Erro ao buscar manchete"

