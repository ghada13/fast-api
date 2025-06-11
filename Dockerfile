# Étape 1 : Choisir une image de base
FROM python:3.10-slim

# Étape 2 : Créer un dossier de travail
WORKDIR /app

# Étape 3 : Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : Copier le code de l'app dans le conteneur
COPY app/ ./app

# Étape 5 : Lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

