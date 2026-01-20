# 🐾 Classypet - Streamlit App

Aplicación web desarrollada con **Streamlit** que permite clasificar mascotas a partir de sus características físicas utilizando un modelo de **Machine Learning**.

[🔗 **App en línea**]()

## 🧠 Modelo

La aplicación utiliza un modelo entrenado previamente:

```
models/pets_model.joblib
```

Además, emplea un archivo JSON con los valores categóricos utilizados durante el entrenamiento:

```
data/category_mapping.json
```

### Variables de entrada

| Variable     | Tipo       | Descripción                         |
| ------------ | ---------- | ----------------------------------- |
| `weight_kg`  | Numérica   | Peso de la mascota en kilogramos    |
| `height_cm`  | Numérica   | Altura de la mascota en centímetros |
| `eye_color`  | Categórica | Color de ojos                       |
| `fur_length` | Categórica | Largo del pelo                      |

Las variables categóricas se transforman automáticamente a codificación binaria (one-hot encoding).

## 🐳 Ejecutar con Docker

### 1. Construir y levantar el contenedor

```bash
docker-compose up --build
```

### 2. Abrir en el navegador

```
http://localhost:8501
```

## ✍️ Créditos

**Alejandro Barrionuevo Rosado**
Máster de FP en Inteligencia Artificial y Big Data - CPIFP Alan Turing
