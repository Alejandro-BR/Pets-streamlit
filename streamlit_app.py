import streamlit as st
import pandas as pd
import joblib
import json

st.title("Classypet")
st.write("Clasificador de mascotas, Introduzca los datos de su mascota y le diremos a qué clase pertenece.")
st.image("img/pets2.png", caption="Aplicación de mascotas")

# Carga el modelo entrenado y el json con los tipos
model = joblib.load("models/pets_model.joblib")

with open("model/category_mapping.json", "r") as f:
    category_mapping = json.load(f)