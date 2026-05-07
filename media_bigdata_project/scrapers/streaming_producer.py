import json
import time
from kafka import KafkaProducer
from scraper_hespress import SOURCES, scrape_source

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')
)

while True:
    for source in SOURCES:
        for article in scrape_source(source):
            producer.send('news_articles', article)
            print('Article envoyé:', article['titre'][:80])
    producer.flush()
    time.sleep(3600)
