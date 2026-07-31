import streamlit as st
import pandas as pd
import requests
API_URL = "http://127.0.0.1:8000/predict"

#CONFIGURACION GLOBLA
st.set_page_config(
    layout="wide", #ESPACIADO
    page_title="Análisis de Sector Inmobiliario",
    page_icon=("img\logo.png")
)

#SIDER ---------------------------------------------------------------------------------------
st.sidebar.title("FILTROS")

cities = ["Guayaquil","Quito","Manta"]

with st.sidebar:
    ciudad_escojida = st.multiselect(
        label="Ciudades",
        options=cities,
        placeholder="Escoja la ciudad"
        )
    
    
    
#DATFRAME LOAD ---------------------------------------------------------------------------------------

df = pd.read_csv("houses.csv")

if ciudad_escojida:
     df= df[df["CITY"].isin(ciudad_escojida)]
    
total_propiedades = len(df)

precio_promedio = df["PRICE_USD"].mean()

median_price = df["PRICE_USD"].median()

area_promedio = df["CONSTRUCTION_AREA_SQM"].mean()

max_price = int(df["PRICE_USD"].max())

#SIDER BAR 2 -------------------------------------------------------

with st.sidebar:
    min_val,max_val = st.slider(
        label="Rango de precios",
        min_value=0,
        max_value=max_price,
        value= (0, max_price),
        step=10000
        )
    
df = df[
    (df["PRICE_USD"] >= min_val) &
    (df["PRICE_USD"] <= max_val)
]
    
#PAGE

st.title("Análisis de Sector Inmobilario")

st.header("Predicción de Precio de Vivienda")

col1, col2 = st.columns(2)

with col1:
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

with col2:
    area_m2 = st.number_input(
        "Área de construcción (m²)",
        min_value=20,
        max_value=1000,
        value=200
    )

    ciudad = st.selectbox(
        "Ciudad",
        ["Quito", "Guayaquil", "Manta"]
    )

col1, col2, col3, col4 = st.columns(4) #Columnas realizadas

with col1:
    st.metric(
        label="Total de propiedades",
        value=total_propiedades
    )
    
    with col2:
        st.metric(
        label="Precio Promedio",
        value=f"${total_propiedades:.2f}"
    )
        
    with col3:
        st.metric(
        label="Mediana de precio",
        value=f"${median_price:.2f}"
    )
        
    with col4:
        st.metric(
        label="Area promedio",
        value=f"{area_promedio:.2f}"
    )
           
#MAPA

col_map, col_df, = st.columns(2) #Columnas realizadas

# df = pd.DataFrame(
#     {
#         "latitude": [-2.19616],
#         "longitude": [-79.88621]
#     }
# )


with col_map:
    st.map(df)

with col_df:
    st.dataframe(
        df,
        hide_index= False,
        column_config={
            "ID": None,
            "CITY": "Ciudad",
            "PRICE_USD": st.column_config.NumberColumn(
                label = "Precio",
                format="$ %d"
            ),
            "LINK": st.column_config.LinkColumn(
                label="Vinculo",
                display_text="Ver Imagen",
            ) 
        }
    )
    