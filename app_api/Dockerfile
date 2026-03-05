FROM python:3.10-slim

# On installe uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet (pyproject.toml, uv.lock s'il existe)
# On copie tout pour l'instant depuis app_api
COPY . /app/

# Installer les dépendances globales dans le conteneur sans créer d'environnement virtuel
RUN uv pip install --system fastapi uvicorn sqlalchemy psycopg2-binary pydantic httpx requests pandas

# Exposer le port de FastAPI
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "app_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
