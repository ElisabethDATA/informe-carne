# LIBRERÍAS #
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go


# CONFIGURACIÓN DE LA PÁGINA #
#layout="centered" or "wide"
st.set_page_config(page_title="Consumo de Carne", layout="wide", page_icon="🥩")
st.set_option('deprecation.showPyplotGlobalUse', False)

# PÁGINA PRINCIPAL#
st.title('Consumo de carne en el mundo')
st.markdown("""
* **Objetivo:** Analizar el consumo de carne en el mundo.
* **Fuente:** [Our World in Data](https://ourworldindata.org/meat-production)
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

# CARGA DE DATOS #
@st.cache_data
def load_data(nrows):
    df = pd.read_csv('data/meat_consumption.csv', nrows=nrows)
    df.columns = [column.upper() for column in df.columns]
    return df

df = load_data(10000)

def select_location(location):
    df_location = df[df['LOCATION'] == location]
    return df_location

def select_year(year):
    df_year = df[df['TIME'] == year]
    return df_year


# VISUALIZACIÓN #
st.title('Visualización')
st.markdown("""
En esta sección se muestran las visualizaciones de los datos.
""")

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

# SIDEBAR: FILTRO POR TIPO DE CARNE #
st.sidebar.subheader('Filtrar por')
tipos = {'Carne de ternera': 'BEEF', 'Carne de cerdo': 'PIG', 'Carne de pollo (aves)': 'POULTRY', 'Carne de oveja': 'SHEEP'}
select = st.sidebar.selectbox('Tipo de carne', ['Carne de ternera', 'Carne de cerdo', 'Carne de pollo (aves)', 'Carne de oveja'])
df_select = df[df['SUBJECT'] == tipos[select]]


# SIDEBAR: FILTRO POR AÑO #
st.sidebar.subheader('Filtrar por año')
year_to_filter = st.sidebar.slider('Año', 1961, 2018, 2018)
df_year = select_year(year_to_filter)

# Crear un texto para que el usuario sepa que el dataset está cargando.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


# SIDEBAR: VISUALIZACIÓN #
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
