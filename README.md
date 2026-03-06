# Projet 2 : Orchestration, Sécurité et Livraison Continue (CD)

![CI Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/ci.yml/badge.svg)
![CD Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/cd.yml/badge.svg)
![Security Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/security.yml/badge.svg)

Ce projet implémente une architecture micro-services complète, sécurisée et déployable automatiquement.

## Architecture

L'application est composée de trois services :
1. **Frontend (Streamlit)** : Interface utilisateur pour la saisie et l'affichage des données.
2. **API (FastAPI)** : Traitement des requêtes et logique métier.
3. **Database (PostgreSQL)** : Persistance des données.

## Installation et Lancement

### Localement avec Python/uv
1. Installez les dépendances : `uv sync`
2. Lancez l'API : `uv run uvicorn app_api.main:app --reload`
3. Lancez le Frontend : `uv run streamlit run app_front/main.py`

### Avec Docker Compose
```bash
docker-compose up --build
```

## Documentation
La documentation technique est générée avec Sphinx. Pour la construire :
```bash
cd docs
uv run sphinx-build -b html source build/html
```

## Licence
[MIT](LICENSE)
