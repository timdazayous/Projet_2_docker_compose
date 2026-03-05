# AI README - Journal des Erreurs et Résolutions

Ce fichier sert de mémoire pour éviter de répéter les mêmes erreurs lors du développement du Projet 2.

## Problèmes Rencontrés & Solutions

### 1. `ModuleNotFoundError: No module named 'app_api'` lors des tests
- **Contexte** : Lancement de `uv run pytest app_api/tests` ou `pytest tests`
- **Cause** : Le module `app_api` n'est pas dans le `PYTHONPATH`, empêchant pytest de résoudre les imports comme `from app_api.main import app`.
- **Solution** : Création d'un `pyproject.toml` à la racine (ou mise à jour de l'existant) avec la configuration :
  ```toml
  [tool.pytest.ini_options]
  pythonpath = ["."]
  testpaths = ["tests"]
  ```

### 2. `sqlalchemy.exc.OperationalError: no such table: data_records`
- **Contexte** : Exécution des tests API (`test_api.py`) avec une base de données SQLite en mémoire (`sqlite:///:memory:`).
- **Cause** : Les tables ne sont pas créées dans la base de données de test en mémoire. L'appel à `Base.metadata.create_all(bind=engine)` dans `conftest.py` semble soit ne pas s'exécuter au bon moment, soit utiliser une `Base` qui n'a pas enregistré le modèle `DataRecord`.
- **État d'investigation actuel** : *Résolu*
- **Solution** : 
  1. Ajouter `StaticPool` de `sqlalchemy.pool` à la configuration de l'`engine` dans `conftest.py`. SQLite en mémoire (`sqlite:///:memory:`) crée une base de données entièrement nouvelle à chaque connexion. Sans `StaticPool`, la création des tables se faisait sur une connexion, et les appels de l'API se faisaient sur une connexion différente (et donc une bdd vide).
  2. Ajouter `Base.metadata.create_all(bind=engine)` dans la fonction `lifespan` de FastAPI (fichier `main.py`) plutôt qu'au niveau global dans `connect.py`, pour mieux contrôler quand la base de données réelle est initialisée.
  ```python
  from sqlalchemy.pool import StaticPool
  engine = create_engine(
      "sqlite:///:memory:",
      connect_args={"check_same_thread": False},
      poolclass=StaticPool
  )
  ```
