import streamlit as st
import requests
import os

st.title("Saisie de données")

# L'URL de l'API est récupérée depuis les variables d'environnement
# En dev local avec Docker, ce sera http://api:8000
API_URL = os.getenv("API_URL", "http://localhost:8000")

with st.form("insert_form"):
    st.subheader("Nouvel enregistrement")
    nom = st.text_input("Nom :")
    age = st.number_input("Âge :", min_value=0, max_value=120, step=1)
    ville = st.text_input("Ville :")
    
    submitted = st.form_submit_button("Envoyer à l'API")
    
    if submitted:
        if not nom or not ville:
            st.error("Veuillez remplir tous les champs texte.")
        else:
            payload = {
                "nom": nom,
                "age": age,
                "ville": ville
            }
            try:
                # Appel POST à l'API FastAPI
                response = requests.post(f"{API_URL}/data", json=payload)
                if response.status_code == 201:
                    st.success("Données sauvegardées avec succès !")
                else:
                    st.error(f"Erreur de l'API : {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error(f"Impossible de se connecter à l'API sur {API_URL}. L'API est-elle lancée ?")
