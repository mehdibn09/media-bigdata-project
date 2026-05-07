import json
import re
from pathlib import Path
from langdetect import detect, LangDetectException

BRONZE_DIR = Path('data/local/bronze')
SILVER_DIR = Path('data/local/silver')
SILVER_DIR.mkdir(parents=True, exist_ok=True)


def clean_html(text):
    text = re.sub(r'<[^>]+>', ' ', text or '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def detect_language(text):
    try:
        return detect(text) if text and len(text) > 20 else None
    except LangDetectException:
        return None


def transform_article(article):
    contenu = clean_html(article.get('contenu'))
    titre = clean_html(article.get('titre'))
    return {
        **article,
        'titre': titre,
        'contenu': contenu,
        'langue': detect_language(contenu or titre),
        'nb_mots': len(contenu.split()) if contenu else 0,
        'is_valid': bool(titre) and len(contenu) >= 20,
    }


def main():
    seen_urls = set()
    cleaned = []
    for file in BRONZE_DIR.glob('*.json'):
        articles = json.loads(file.read_text(encoding='utf-8'))
        for article in articles:
            url = article.get('url')
            if url in seen_urls:
                continue
            seen_urls.add(url)
            item = transform_article(article)
            if item['is_valid']:
                cleaned.append(item)
    output = SILVER_DIR / 'articles_silver.json'
    output.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Silver créé: {len(cleaned)} articles")


if __name__ == '__main__':
    main()
