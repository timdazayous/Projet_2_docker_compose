import streamlit as st
import requests
import os
import pandas as pd

st.title("Affichage des données")

API_URL = os.getenv("API_URL", "http://localhost:8000")

if st.button("Rafraîchir les données"):
    try:
        response = requests.get(f"{API_URL}/data")
        if response.status_code == 200:
            data = response.json()
            if data:
                # Conversion json en DataFrame pour un bel affichage
                df = pd.DataFrame(data)
                # On enlève la colonne id si on veut
                if "id" in df.columns:
                    df = df.drop(columns=["id"])
                
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Aucune donnée trouvée dans la base de données.")
        else:
            st.error(f"Erreur de l'API : {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error(f"Impossible de se connecter à l'API sur {API_URL}.")
