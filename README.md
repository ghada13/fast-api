# 🚀 FastAPI Kubernetes CI/CD Project

Ce projet implémente une API RESTful avec **FastAPI**, conteneurisée avec **Docker**, déployée sur **Kubernetes** via **Helm**, et automatisée avec **GitHub Actions**.

---

## 🧰 Technologies

- FastAPI / Python
- Docker & Docker Compose
- Kubernetes
- Helm
- GitHub Actions
- PostgreSQL (optionnel)
- Swagger UI

---

## 📦 Lancer l’application en local

```bash
docker-compose up --build
Accéder à : http://localhost:8000/docs

```
🐳 Build & push de l’image Docker

```bash
docker build -t ghadajebri/fastapi-app .
docker push ghadajebri/fastapi-app
```
☸️ Déploiement Kubernetes avec Helm

```bash
helm install fastapi-app ./helm
# ou mise à jour
helm upgrade fastapi-app ./helm
```
