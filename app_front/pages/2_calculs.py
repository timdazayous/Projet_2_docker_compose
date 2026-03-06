import streamlit as st
import requests
import os

# Configuration de l'URL de l'API
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Calculatrice API", page_icon="🧮")

st.title("🧮 Calculatrice via API")
st.write("Cette page utilise le module `maths` de l'API pour effectuer des calculs.")

# --- SECTION ADDITION / SOUSTRACTION ---
st.header("➕ Addition & ➖ Soustraction")
col1, col2 = st.columns(2)

with col1:
    num_a = st.number_input("Nombre A", value=0.0, key="add_a")
with col2:
    num_b = st.number_input("Nombre B", value=0.0, key="add_b")

c1, c2 = st.columns(2)
with c1:
    if st.button("Calculer l'Addition"):
        try:
            response = requests.post(f"{API_URL}/math/add", json={"a": num_a, "b": num_b})
            if response.status_code == 200:
                result = response.json()["result"]
                st.success(f"Résultat : {num_a} + {num_b} = {result}")
            else:
                st.error("Erreur lors du calcul.")
        except Exception as e:
            st.error(f"Erreur de connexion à l'API : {e}")

with c2:
    if st.button("Calculer la Soustraction"):
        try:
            response = requests.post(f"{API_URL}/math/sub", json={"a": num_a, "b": num_b})
            if response.status_code == 200:
                result = response.json()["result"]
                st.success(f"Résultat : {num_a} - {num_b} = {result}")
            else:
                st.error("Erreur lors du calcul.")
        except Exception as e:
            st.error(f"Erreur de connexion à l'API : {e}")

st.divider()

# --- SECTION CARRÉ ---
st.header("sup2; Calcul du Carré")
num_sq = st.number_input("Nombre à élever au carré", value=0.0)

if st.button("Calculer le Carré"):
    try:
        response = requests.post(f"{API_URL}/math/square", json={"a": num_sq})
        if response.status_code == 200:
            result = response.json()["result"]
            st.success(f"Résultat : {num_sq}² = {result}")
        else:
            st.error("Erreur lors du calcul.")
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")

st.divider()
st.info("💡 Note : Ces calculs sont effectués côté serveur par l'API FastAPI en utilisant le module `mon_module.py`.")
