# Parte 1 - Importar librerías 
import streamlit as st                                              # Librería para Streamlit
import pandas as pd
import numpy as np 

# Parte 2 - Configuraciones iniciales
st.set_page_config(                                                 # Nombre a la página
    page_title = "Monitoreo Industrial",
    layout = "wide" 
)

st.title("Sistema de Monitoreo Industrial")                         # Titulo de la página.
st.write("Bienvenido al Sistema de Monitoreo en Tiempo Real")       # Texto de la página.
st.header("Panel Principal")                                        # Encabezado de la página.
st.subheader("Datos del sensor")                                    # Subencabezado de la página.
st.text("Información del área de monitoreo")                        # Descripción de la página.
st.markdown("*Texto con formato Markdown*")                       # Texto en negritas.

# Widgets básicos
temperatura = st.slider("Temperatura",                              # Slider con título de Temperatura con valor min, max e inicial.
min_value = 0, max_value = 100, value = 25)

col1, col2 = st.columns(2)
with col1:
    st.metric("Temperatura", f"{temperatura}°C", delta = "1.2°C" )  
with col2:
    st.metric("Presion", "1013 hPa", delta = "-2hPa")