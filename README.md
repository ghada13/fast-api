# fast-api
Ce projet consiste à développer une API RESTful simple avec FastAPI, conteneuriser l'application à l'aide de Docker, fournir un environnement de développement et de test local via Docker Compose, déployer l'application sur un cluster Kubernetes à l'aide de Helm Charts, et automatiser le pipeline de déploiement CI/CD avec GitHub Actions.

Objectifs techniques :
Développement de l’API :

-Implémentation d’une API RESTful avec FastAPI, incluant les opérations CRUD (Create, Read, Update, Delete).

-Validation des données avec Pydantic et documentation auto-générée via Swagger UI.

Conteneurisation :

-Création d’un Dockerfile optimisé pour construire une image légère de l’application.

-Utilisation de bonnes pratiques de conteneurisation (multi-stage builds, .dockerignore, etc.).

Environnement local :

-Mise en place d’un fichier docker-compose.yml pour faciliter l'exécution locale avec des services annexes (ex. : base de données PostgreSQL).

Déploiement Kubernetes :

-Création de fichiers Helm Chart (templates deployment.yaml, service.yaml, values.yaml, etc.) pour le déploiement modulaire sur Kubernetes.

-Paramétrage des variables d’environnement et des ressources (CPU, mémoire, etc.).

CI/CD avec GitHub Actions :

-Automatisation des étapes de build, test, push de l'image Docker, et déploiement sur un cluster Kubernetes.

-Intégration de contrôles de qualité de code (lint, tests unitaires) dans le pipeline.

Technologies utilisées :
*FastAPI / Python

*Docker & Docker Compose

*Kubernetes

*Helm

GitHub Actions

PostgreSQL (optionnel pour la persistance)

Swagger (OpenAPI)

Git & GitHub

Compétences démontrées :
Développement d’API modernes avec Python

Conteneurisation d’applications et gestion des dépendances

Orchestration de microservices avec Kubernetes

Utilisation d’outils DevOps (CI/CD, Docker, Helm)

Structuration de projets cloud-native
