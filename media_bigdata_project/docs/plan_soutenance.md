# Plan de soutenance

## Slide 1 : Titre
Architecture Big Data pour l'analyse des tendances médiatiques

## Slide 2 : Problématique
Les médias publient chaque jour un grand volume d'articles. Il devient difficile de suivre les tendances dominantes manuellement.

## Slide 3 : Objectifs
- Collecter automatiquement les articles
- Stocker les données dans un Data Lake
- Nettoyer et enrichir les données
- Créer des tables analytiques
- Visualiser les tendances médiatiques

## Slide 4 : Architecture globale
Sites news -> Python Scraping -> Data Lake Bronze/Silver/Gold -> PostgreSQL -> Dashboard

## Slide 5 : Technologies
Python, BeautifulSoup, Kafka, MinIO, PostgreSQL, Airflow, Docker, Metabase ou Power BI.

## Slide 6 : Architecture Médaillon
Bronze : données brutes.
Silver : données nettoyées.
Gold : données analytiques.

## Slide 7 : Qualité des données
Contrôle des titres vides, dates manquantes, contenus trop courts, doublons et complétude.

## Slide 8 : Dashboard
Indicateurs : nombre total d'articles, articles par source, évolution par jour, mots-clés fréquents.

## Slide 9 : Démonstration
Exécuter le pipeline complet avec Airflow et afficher les résultats dans PostgreSQL puis Metabase/Power BI.

## Slide 10 : Conclusion
La plateforme proposée permet une collecte, un stockage, un traitement et une analyse automatisés des articles de presse selon une architecture Big Data moderne.

## Texte oral prêt
Notre projet consiste à concevoir une plateforme Big Data capable de collecter automatiquement des articles de presse depuis plusieurs sources d'actualité. Les données sont d'abord stockées dans une zone Bronze sous forme brute, puis nettoyées dans la zone Silver, avant d'être transformées en tables analytiques dans la zone Gold. Ces résultats sont ensuite chargés dans PostgreSQL pour alimenter des tableaux de bord permettant de suivre les tendances d'actualité, les sources les plus actives et les mots-clés les plus fréquents.
