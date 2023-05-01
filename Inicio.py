# LIBRERÍAS #
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go
from funciones import load_data

# CONFIGURACIÓN DE LA PÁGINA #
# layout="centered" or "wide" 🥩_
st.set_page_config(page_title="Consumo de Carne", layout="centered", page_icon="🥩")
st.set_option('deprecation.showPyplotGlobalUse', False)


# SIDEBAR #
st.sidebar.title('Menú')
st.sidebar.markdown("""
* **Visualización:** Selecciona el tipo de visualización que deseas ver.
* **Filtrar por:** Selecciona el tipo de carne que deseas ver.
* **Filtrar por año:** Selecciona el año que deseas ver.
""")
st.sidebar.markdown("""
* **Nota:** El consumo de carne se mide en kilogramos por persona al año.
""")

# PÁGINA PRINCIPAL#
with st.container():
    st.title('Consumo de carne en el mundo')
    st.markdown("""
    * **Objetivo:** Analizar el consumo de carne en el mundo.
    * **Fuente:** [Consumo mundial de carne](https://www.kaggle.com/datasets/allenkong/worldwide-meat-consumption)
    """)
    st.image('img/carne.jpg')
    st.text('Imagen de https://www.agronewscomunitatvalenciana.com/')

    st.markdown("""
    El consumo de carne es uno de los aspectos más importantes de la alimentación humana y una fuente clave de proteínas y otros nutrientes. Sin embargo, el consumo de carne a nivel mundial ha sido objeto de un intenso debate en los últimos años debido a su impacto ambiental y a los posibles riesgos para la salud.

    En este contexto, el análisis de consumo de carne a nivel mundial es una herramienta valiosa para comprender los patrones de consumo de carne y sus implicaciones en términos de salud y sostenibilidad. El análisis de datos de consumo de carne a nivel mundial también puede proporcionar información sobre las tendencias de consumo y los factores que influyen en la elección de alimentos en diferentes países.

    A través del análisis de datos, es posible identificar patrones de consumo de carne en diferentes regiones del mundo, examinar las preferencias de consumo de diferentes tipos de carne y evaluar las implicaciones del consumo de carne para la salud y el medio ambiente. También se puede analizar cómo el consumo de carne varía según el nivel de ingresos de los países, la cultura alimentaria y los factores socioeconómicos.

    En definitiva, el análisis de consumo de carne a nivel mundial puede proporcionar información valiosa para los responsables de la formulación de políticas, los investigadores y los consumidores interesados en tomar decisiones informadas sobre su alimentación y su impacto en el medio ambiente.
    """)
    st.markdown("""
    * **Autor:** [Elisabeth Pérez](https://www.linkedin.com/in/elisabethperezruiz)
    """)
    st.markdown("""
    * **Fecha:** 02/05/2023
    """)
    st.markdown("""
    * **Código:** [GitHub](https://github.com/ElisabethDATA/informe-carne)
    """)
    st.markdown("""
    * **Datos:** [GitHub](https://raw.githubusercontent.com/ElisabethDATA/informe-carne/master/data/meat_consumption.csv)
    """)
    st.markdown("""
    * **Licencia:** [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
    """)

# COSAS QUE VAMOS A USAR EN TODA LA APP #

df = load_data()

def select_location(location):
    df_location = df[df['LOCATION'] == location]
    return df_location

def select_year(year):
    df_year = df[df['TIME'] == year]
    return df_year

