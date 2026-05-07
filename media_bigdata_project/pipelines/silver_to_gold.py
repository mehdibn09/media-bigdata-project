import json
from collections import Counter, defaultdict
from pathlib import Path
import pandas as pd

SILVER_FILE = Path('data/local/silver/articles_silver.json')
GOLD_DIR = Path('data/local/gold')
GOLD_DIR.mkdir(parents=True, exist_ok=True)
STOPWORDS = {'the', 'and', 'for', 'with', 'dans', 'les', 'des', 'une', 'sur', 'que', 'qui', 'من', 'في', 'على'}


def keywords(text, n=10):
    words = [w.lower().strip('.,;:!?()[]"') for w in (text or '').split()]
    words = [w for w in words if len(w) > 3 and w not in STOPWORDS]
    return [w for w, _ in Counter(words).most_common(n)]


def main():
    articles = json.loads(SILVER_FILE.read_text(encoding='utf-8')) if SILVER_FILE.exists() else []
    for a in articles:
        a['mots_cles'] = ', '.join(keywords((a.get('titre') or '') + ' ' + (a.get('contenu') or '')))
    df = pd.DataFrame(articles)
    if df.empty:
        print('Aucune donnée Silver')
        return
    df.to_csv(GOLD_DIR / 'articles_gold.csv', index=False)
    df.groupby('source').size().reset_index(name='nombre_articles').to_csv(GOLD_DIR / 'articles_par_source.csv', index=False)
    df.groupby('categorie').size().reset_index(name='nombre_articles').to_csv(GOLD_DIR / 'articles_par_categorie.csv', index=False)
    df['date_collecte_jour'] = pd.to_datetime(df['date_collecte']).dt.date
    df.groupby('date_collecte_jour').size().reset_index(name='nombre_articles').to_csv(GOLD_DIR / 'articles_par_jour.csv', index=False)
    all_keywords = []
    for kw in df['mots_cles'].dropna():
        all_keywords.extend([x.strip() for x in kw.split(',') if x.strip()])
    pd.DataFrame(Counter(all_keywords).most_common(30), columns=['mot_cle', 'frequence']).to_csv(GOLD_DIR / 'top_mots_cles.csv', index=False)
    print('Gold créé')


if __name__ == '__main__':
    main()
