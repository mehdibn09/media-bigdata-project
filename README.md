# Projet Architecture de Données : Analyse Big Data des articles de presse

## 1. Objectif
Créer une plateforme Big Data capable de collecter automatiquement des articles de presse, de les stocker dans un Data Lake, de les transformer selon l'architecture Médaillon, puis de les analyser dans un Data Warehouse et un dashboard.

## 2. Architecture
Sites d'actualité -> Scraping Python -> Bronze -> Silver -> Gold -> PostgreSQL -> Metabase / Power BI

Composants :
- Python : scraping, nettoyage, transformation
- Kafka : streaming optionnel
- MinIO : Data Lake
- PostgreSQL : Data Warehouse
- Airflow : orchestration
- Metabase ou Power BI : visualisation
- Docker Compose : déploiement

## 3. Installation

### Prérequis
Installer Docker Desktop, Python, VS Code et Git.

### Lancer les services
```bash
docker compose up -d
```

Interfaces :
- MinIO : http://localhost:9001
- Airflow : http://localhost:8080
- Metabase : http://localhost:3000
- PostgreSQL : localhost:5432

Identifiants :
- MinIO : admin / admin12345
- Airflow : admin / admin
- PostgreSQL : news_user / news_pass

## 4. Exécution locale simple
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python scrapers/scraper_hespress.py
python pipelines/bronze_to_silver.py
python quality/data_quality_checks.py
python pipelines/silver_to_gold.py
python pipelines/load_to_postgres.py
```

## 5. Architecture Médaillon

### Bronze
Données brutes collectées depuis les sites d'actualité.

### Silver
Données nettoyées : HTML supprimé, doublons supprimés, langue détectée, contenu normalisé.

### Gold
Données analytiques : articles par source, articles par jour, top mots-clés.

## 6. Tables analytiques
- articles_gold
- articles_par_source
- articles_par_jour
- top_mots_cles

## 7. Soutenance
Présenter dans cet ordre : contexte, problématique, architecture, technologies, pipeline, qualité des données, dashboard, démonstration, conclusion.

## 8. Démonstration
1. Lancer docker compose.
2. Ouvrir Airflow.
3. Déclencher le DAG `news_bigdata_pipeline`.
4. Vérifier les fichiers Bronze/Silver/Gold.
5. Ouvrir PostgreSQL ou Metabase.
6. Montrer les indicateurs.
   STRUCTURE Projet:
media_bigdata_project/
├── scrapers/
│   ├── bbc/scraper_bbc.py
│   ├── cnn/scraper_cnn.py
│   └── aljazeera/scraper_aljazeera.py
├── ingestion/
│   ├── batch/batch_ingestor.py         → MinIO Bronze
│   └── streaming/kafka_producer.py / kafka_consumer.py
├── datalake/
│   ├── bronze/bronze_schema.py
│   ├── silver/silver_transform.py      → nettoyage HTML, langdetect
│   └── gold/gold_aggregations.py       → top keywords, stats par source
├── etl/pipeline.py                     → Bronze → Silver → Gold
├── orchestration/dags/
│   ├── dag_batch_pipeline.py           → @hourly, 4 tasks
│   └── dag_streaming_pipeline.py       → health check Kafka
├── warehouse/
│   ├── schema.sql                      → tables PostgreSQL
│   └── loader.py
├── quality/checks.py                   → complétude, validité
├── governance/lineage.py               → traçabilité JSONL
├── deployment/docker/
│   ├── docker-compose.yml              → MinIO, Kafka, Postgres, Airflow, Metabase
│   └── Dockerfile.scraper
├── visualization/README.md
├── docs/architecture.md
└── requirements.txt
