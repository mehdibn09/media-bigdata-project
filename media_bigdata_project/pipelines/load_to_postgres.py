from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

ENGINE = create_engine('postgresql+psycopg2://news_user:news_pass@localhost:5432/news_dw')
GOLD_DIR = Path('data/local/gold')


def load_csv(name, table):
    path = GOLD_DIR / name
    if path.exists():
        df = pd.read_csv(path)
        df.to_sql(table, ENGINE, if_exists='replace', index=False)
        print(f'{table} chargé: {len(df)} lignes')


def main():
    load_csv('articles_gold.csv', 'articles_gold')
    load_csv('articles_par_source.csv', 'articles_par_source')
    load_csv('articles_par_jour.csv', 'articles_par_jour')
    load_csv('top_mots_cles.csv', 'top_mots_cles')


if __name__ == '__main__':
    main()
