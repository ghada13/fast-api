# Étape 1 : Choisir une image de base
FROM python:3.10-slim

# Étape 2 : Créer un dossier pour l'app
WORKDIR /app

# Étape 3 : Copier les fichiers de l’app dans l’image
COPY . /app

# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Commande pour lancer l’app avec uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
