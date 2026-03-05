import streamlit as st

st.set_page_config(
    page_title="Orchestration & Micro-services",
    page_icon="🐳",
    layout="wide"
)

st.title("Projet 2 : Orchestration, Sécurité et CD")

st.markdown("""
### Architecture Micro-services

Bienvenue sur le Frontend de l'application !
Cette interface communique avec une API FastAPI qui elle-même discute avec une base de données PostgreSQL.

* 👈 Utilisez le menu latéral pour naviguer.
* **Page Saisie** : Pour envoyer de nouvelles données à l'API.
* **Page Affichage** : Pour consulter les données stockées dans la base.
""")
