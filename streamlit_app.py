import streamlit as st
import pandas as pd
import joblib
import json

st.title("Classypet")
st.write("Clasificador de mascotas, Introduzca los datos de su mascota y le diremos a qué clase pertenece.")
st.image("img/pets2.png", caption="Aplicación de mascotas")

# Carga el modelo entrenado y el json con los tipos
model = joblib.load("models/pets_model.joblib")

with open("data/category_mapping.json", "r") as f:
    category_mapping = json.load(f)

eyer_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

weight = st.number_input("Peso (kg)", min_value=0.0, max_value=100.0, value=1.0)
height = st.number_input("Altura (cm)", min_value=0.0, max_value=100.0, value=10.0)
eyer_color = st.selectbox("Color de ojos", ("Azul", "Marrón", "Gris", "Verde"))

fur_length = st.selectbox("Largo del pelo", ("Largo", "Medio", "Corto"))

# st.write(weight)
# st.write(height)
# st.write(eyer_color)
# st.write(fur_length)

# Mapea la seleccion de color de ojos y largo de pelo al español
eyer_color_map = {"Marrón": "brown", "Azul": "blue", "Gris": "gray", "Verde": "green"}
fur_length_map = {"Largo": "long", "Medio": "medium", "Corto": "short"}

selected_eye_color = eyer_color_map[eyer_color]
selected_fur_length = fur_length_map[fur_length]

# Genera las columnas binarias para eye_color y fur_length
eyer_color_binary = [(color == selected_eye_color) for color in eyer_color_values]
fur_length_binary = [(length == selected_fur_length) for length in fur_length_values]

# Genera las columnas binarias para eye_color y fur_length
eye_color_binary = [(color == selected_eye_color) for color in eyer_color_values]
fur_length_binary = [(length == selected_fur_length) for length in fur_length_values]

input_data = [weight, height] + eye_color_binary + fur_length_binary

columns = (
    ["weight_kg", "height_cm"]
    + [f"eye_color_{color}" for color in eyer_color_values]
    + [f"fur_length_{length}" for length in fur_length_values]
)

input_df = pd.DataFrame([input_data], columns=columns)
    

# input_df

# Realiza la prediccion
if st.button("Clasifica mascota"):
    prediction = model.predict(input_df)[0]
    prediction_map = {"dog": "perro", "cat": "Gato", "rabbit": "conejo"}
    st.success(f"La mascota es un {prediction_map[prediction]}", icon="✅")
