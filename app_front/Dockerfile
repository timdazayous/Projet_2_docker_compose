FROM python:3.10-slim

# On installe uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Définir le répertoire de travail
WORKDIR /app

# Copier le code local vers le conteneur
COPY . /app/

# Installer les dépendances de streamlit via uv
RUN uv pip install --system streamlit requests pandas

# Exposer le port par défaut de Streamlit
EXPOSE 8501

# Commande pour lancer Streamlit
CMD ["streamlit", "run", "app_front/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
