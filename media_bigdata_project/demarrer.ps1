cd "C:\Users\Mehdi Benjelloun\Downloads\media_bigdata_project"
docker-compose up -d
.\venv\Scripts\activate

Write-Host "⏳ Attente du démarrage des services (30 secondes)..."
Start-Sleep -Seconds 30

Start-Process "http://localhost:9001"
Start-Process "http://localhost:8080"
Start-Process "http://localhost:3000"

Write-Host "✅ Tout est lancé !"
Write-Host "MinIO    → http://localhost:9001  (admin / admin12345)"
Write-Host "Airflow  → http://localhost:8080  (admin / admin)"
Write-Host "Metabase → http://localhost:3000"