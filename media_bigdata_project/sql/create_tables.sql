CREATE TABLE IF NOT EXISTS articles_gold (
    id SERIAL PRIMARY KEY,
    titre TEXT,
    auteur TEXT,
    date_publication TEXT,
    categorie TEXT,
    contenu TEXT,
    source TEXT,
    url TEXT UNIQUE,
    date_collecte TEXT,
    langue TEXT,
    nb_mots INT,
    mots_cles TEXT
);

CREATE TABLE IF NOT EXISTS articles_par_source (
    source TEXT PRIMARY KEY,
    nombre_articles INT
);

CREATE TABLE IF NOT EXISTS articles_par_jour (
    date_collecte_jour DATE PRIMARY KEY,
    nombre_articles INT
);

CREATE TABLE IF NOT EXISTS top_mots_cles (
    mot_cle TEXT PRIMARY KEY,
    frequence INT
);
