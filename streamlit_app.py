import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Precio de Viviendas",
    page_icon="🏡",
    layout="centered"
)
st.title("🏡 Precio de Viviendas")
st.write(
    "Ingrese las características de la vivienda y el sistema estimará su precio utilizando un modelo de Machine Learning."
)
st.divider()

st.subheader("Datos de la Vivienda")

bedrooms = st.number_input(
    "Habitaciones",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Baños",
    min_value=1,
    max_value=10,
    value=2
)

parking_spots = st.number_input(
    "Parqueaderos",
    min_value=0,
    max_value=10,
    value=2
)

area_m2 = st.number_input(
    "Área de construcción (m²)",
    min_value=20,
    max_value=1000,
    value=200
)

ciudad = st.selectbox(
    "Ciudad",
    [
        "Quito",
        "Guayaquil",
        "Manta"
    ]
)
if ciudad == "Quito":
    city_quito = 1
    city_guayaquil = 0
    city_manta = 0
    lat = -0.18
    lon = -78.48

elif ciudad == "Guayaquil":
    city_quito = 0
    city_guayaquil = 1
    city_manta = 0
    lat = -2.17
    lon = -79.92

else:
    city_quito = 0
    city_guayaquil = 0
    city_manta = 1
    lat = -0.95
    lon = -80.73
    
if st.button("🔮 Predecir Precio"):

    datos = {
        "area_m2": area_m2,
        "bathrooms": bathrooms,
        "bedrooms": bedrooms,
        "city_guayaquil": city_guayaquil,
        "city_manta": city_manta,
        "city_quito": city_quito,
        "lat": lat,
        "lon": lon,
        "parking_spots": parking_spots
    }

    try:
        respuesta = requests.post(
            API_URL,
            json=datos
            )

        if respuesta.status_code == 200:

            resultado = respuesta.json()

            st.success("✅ Predicción realizada correctamente")

            st.subheader("Resultado de la Predicción")

            st.metric(
                label="💰 Precio estimado de la vivienda",
                value=f"USD {resultado['precio_usd']:,.2f}"
            )

            st.info(f"🤖 Modelo utilizado: {resultado['modelo']}")

        else:
            st.error("Error al realizar la predicción.")

    except Exception as e:
        st.error(f"No fue posible conectar con la API.\n\n{e}")