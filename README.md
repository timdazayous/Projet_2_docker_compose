# 🚀 Projet 2 : Orchestration, Sécurité et Livraison Continue (CD)

![CI Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/ci.yml/badge.svg)
![CD Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/cd.yml/badge.svg)
![Security Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/security.yml/badge.svg)

Bienvenue dans le dépôt du **Projet 2** ! ✨ Ce projet est le résultat d'une transformation complète : d'un script Python isolé à une **architecture micro-services** moderne, conteneurisée et automatisée.

---

## 🏗️ Architecture du Système

L'application repose sur un écosystème de trois services complémentaires :

1.  **🎨 Frontend (Streamlit)** : Interface utilisateur fluide et interactive. Elle permet de saisir des données, de consulter la base et d'effectuer des calculs complexes via l'API.
2.  **🧠 API (FastAPI)** : Le point d'entrée central de la logique métier. Elle expose des endpoints REST pour le stockage des données et les services de calcul.
3.  **💾 Database (PostgreSQL)** : Un système de gestion de base de données relationnelle robuste, assurant la persistance des informations grâce aux volumes Docker.

### 🔒 Sécurité & Réseau
*   **Cloisonnement** : Utilisation de réseaux Docker (`front-api` et `api-db`) pour limiter la visibilité des services. Le Frontend ne peut jamais "voir" la base de données directement.
*   **Hygiène** : Scan automatique via **Gitleaks** pour empêcher toute fuite de secret.
*   **Propreté** : Analyse statique du code avec **Ruff** pour un code impeccable.

---

## 🐳 Docker Compose : Dev vs Prod

Ce projet propose deux configurations distinctes pour répondre à tous les besoins :

### 🛠️ `docker-compose.yml` (Mode Développement)
*   **Build Local** : Les images sont construites à partir du code source local à chaque lancement.
*   **Agilité** : Idéal pour tester de nouvelles fonctionnalités ou debuguer.
*   **Simplicité** : Tout est autonome sur votre machine.

### 🚀 `docker-compose.prod.yml` (Mode Production)
*   **Images DockerHub** : Contrairement au mode dev, ce fichier ne construit rien. Il télécharge les images pré-construites et validées depuis DockerHub.
*   **Optimisation** : Utilise les builds officiels générés par la pipeline CD.
*   **Sécurité** : Les images sont immuables et garantissent que le code en prod est exactement celui qui a passé tous les tests.

---

## 🌟 Fonctionnalités Phares

### 📥 Gestion des Données
*   **Saisie** : Formulaire dynamique pour injecter des enregistrements.
*   **Lecture** : Visualisation propre des données PostgreSQL via l'API.

### 🧮 Interface de Calcul (Nouveau !)
Une page dédiée permettant d'utiliser les algorithmes du module `maths` :
*   **Additions & Soustractions** haute précision.
*   **Calcul de Carré** instantané.
*   *Le saviez-vous ?* Ces calculs ne sont pas faits dans le navigateur, mais délégués de manière asynchrone à l'API !

---

## 🛠️ Stack Technique

| Technologie | Rôle | ✨ Atout |
| :--- | :--- | :--- |
| **Python 3.10** | Langue maternelle | Polyvalence et rapidité |
| **FastAPI** | Framework API | Asynchrone et Typage fort |
| **Streamlit** | Frontend | Création d'UI rapide et élégante |
| **SQLAlchemy** | ORM | Abstraction de la BDD (SQLite/Postgres) |
| **PostgreSQL** | BDD Production | Fiabilité et performance |
| **Docker** | Conteneurisation | "It works on my machine" partout |
| **GitHub Actions** | Automatisation | Pipeline CI/CD complète |
| **Sphinx** | Documentation | Documentation technique pro |

---

## 🚀 Installation Express

### 🐳 Via Docker Compose (Recommandé)
```bash
# Pour le développement
docker-compose up --build

# Pour la production (nécessite les secrets configurés)
docker-compose -f docker-compose.prod.yml up
```

### 🐍 Via Python Local (uv)
```bash
uv sync
uv run uvicorn app_api.main:app --reload
uv run streamlit run app_front/main.py
```

---

## 📚 Documentation & Tests

### 📝 Documentation technique (Sphinx)
Générez et ouvrez la documentation en une seule commande :
```bash
# Build et ouverture automatique (Windows)
cd docs; uv run sphinx-build -b html source build/html; start build/html/index.html
```

### 🧪 Tests & Couverture
```bash
uv run pytest --cov=app_api --cov-report=term-missing
```

---

## 🤝 Contribution & Éthique
Consultez nos guides pour rejoindre l'aventure :
*   [📜 Code de Conduite](CODE_OF_CONDUCT.md)
*   [🛠️ Guide de Contribution](CONTRIBUTING.md)

---
Developed with ❤️ by **Tim D**
🥇 *Projet certifié Orchestration & CD*
