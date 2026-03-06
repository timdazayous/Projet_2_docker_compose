# 🚀 Projet 2 : Orchestration, Sécurité et Livraison Continue (CD)

![CI Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/ci.yml/badge.svg)
![CD Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/cd.yml/badge.svg)
![Security Status](https://github.com/timdazayous/Projet_2_docker_compose/actions/workflows/security.yml/badge.svg)

Bienvenue dans le dépôt du **Projet 2** ! Ce projet transforme un simple script en une **architecture micro-services** robuste, sécurisée et entièrement automatisée via une pipeline CI/CD. 🛠️✨

---

## 🏗️ Architecture du Système

Le projet est découpé en trois services distincts qui collaborent harmonieusement :

*   **🎨 Frontend (Streamlit)** : Une interface web interactive pour manipuler les données.
*   **🧠 API (FastAPI)** : Le "cerveau" de l'application, gérant les calculs et les accès à la base de données.
*   **💾 Database (PostgreSQL)** : Persistance des données avec gestion des volumes Docker.

### 🔒 Sécurité & Réseau
*   **Cloisonnement** : Les réseaux Docker (`front-api` et `api-db`) isolent les services.
*   **Hygiène** : Scan de secrets automatique avec **Gitleaks**.
*   **Variables** : Gestion propre via fichiers `.env`.

---

## 🌟 Fonctionnalités

### 📥 Page 0 : Saisie de données
Formulaire intuitif pour insérer de nouveaux enregistrements (Nom, Âge, Ville) dans la base de données PostgreSQL via une requête `POST` à l'API.

### 📊 Page 1 : Consultation
Affichage dynamique des données récupérées en temps réel via une requête `GET` à l'API, présentées sous forme de tableau Pandas.

### 🧪 Tests Automatisés
Suite de tests complète avec **Pytest** couvrant la logique métier et l'intégration de l'API.

---

## 🛠️ Stack Technique

| Technologie | Rôle |
| :--- | :--- |
| **Python 3.10** | Langage principal |
| **FastAPI** | Framework API haute performance |
| **Streamlit** | Interface utilisateur (Frontend) |
| **SQLAlchemy** | ORM pour la gestion de la BDD |
| **PostgreSQL** | Base de données de production |
| **Docker & Compose** | Conteneurisation et Orchestration |
| **GitHub Actions** | Automatisation CI/CD |
| **Sphinx** | Génération de documentation technique |

---

## 🚀 Installation et Lancement

### 🐳 La méthode rapide (Docker)
Assurez-vous d'avoir Docker et Docker Compose installés, puis :
```bash
docker-compose up --build
```
L'application sera accessible sur :
*   **Frontend** : `http://localhost:8501`
*   **API** : `http://localhost:8000`

### 🐍 Méthode de développement (Local)
Utilisez le gestionnaire de paquets `uv` pour une expérience ultra-rapide :
```bash
# 1. Installer les dépendances
uv sync

# 2. Lancer l'API
uv run uvicorn app_api.main:app --reload

# 3. Lancer le frontend (dans un autre terminal)
uv run streamlit run app_front/main.py
```

---

## 📚 Documentation & Tests

### 📝 Générer la documentation Sphinx
```bash
cd docs
uv run sphinx-build -b html source build/html
```

### 🧪 Lancer les tests avec couverture
```bash
uv run pytest --cov=app_api --cov-report=term-missing
```

---

## ⚙️ Configuration CI/CD sur GitHub

Pour que le déploiement automatique vers DockerHub fonctionne, configurez les **Secrets** suivants dans votre dépôt GitHub :
1.  `DOCKERHUB_USERNAME` : Votre pseudo DockerHub.
2.  `DOCKERHUB_TOKEN` : Votre jeton d'accès personnel.

---

## 🤝 Contribution
Les contributions sont les bienvenues ! Consultez le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

Developed with ❤️ by Tim D
