import json
import re
from datetime import datetime
from pathlib import Path
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path('data/local/bronze')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SOURCES = [
    {'name': 'BBC', 'url': 'https://www.bbc.com/news'},
    {'name': 'Reuters', 'url': 'https://www.reuters.com/world/'},
]


def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


def scrape_source(source: dict) -> list[dict]:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(source['url'], headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    articles = []
    for link in soup.find_all('a', href=True)[:80]:
        title = clean_text(link.get_text(' '))
        href = link['href']
        if len(title) < 25:
            continue
        if href.startswith('/'):
            base = '/'.join(source['url'].split('/')[:3])
            href = base + href
        articles.append({
            'titre': title,
            'auteur': None,
            'date_publication': None,
            'categorie': None,
            'contenu': title,
            'source': source['name'],
            'url': href,
            'date_collecte': datetime.utcnow().isoformat(),
        })
    return articles


def main():
    all_articles = []
    for source in SOURCES:
        try:
            all_articles.extend(scrape_source(source))
        except Exception as exc:
            print(f"Erreur scraping {source['name']}: {exc}")
    filename = OUTPUT_DIR / f"articles_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    filename.write_text(json.dumps(all_articles, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"{len(all_articles)} articles sauvegardés dans {filename}")


if __name__ == '__main__':
    main()
