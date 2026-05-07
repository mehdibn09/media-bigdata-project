import json
from pathlib import Path

SILVER_FILE = Path('data/local/silver/articles_silver.json')


def main():
    articles = json.loads(SILVER_FILE.read_text(encoding='utf-8')) if SILVER_FILE.exists() else []
    total = len(articles)
    checks = {
        'total_articles': total,
        'articles_sans_titre': sum(1 for a in articles if not a.get('titre')),
        'dates_manquantes': sum(1 for a in articles if not a.get('date_publication')),
        'contenu_trop_court': sum(1 for a in articles if len((a.get('contenu') or '').split()) < 20),
        'urls_manquantes': sum(1 for a in articles if not a.get('url')),
    }
    checks['taux_completude_titre'] = round((total - checks['articles_sans_titre']) / total * 100, 2) if total else 0
    Path('data/local/quality').mkdir(parents=True, exist_ok=True)
    Path('data/local/quality/report.json').write_text(json.dumps(checks, indent=2, ensure_ascii=False), encoding='utf-8')
    print(checks)


if __name__ == '__main__':
    main()
