import streamlit as st
from funciones import load_data, split_measure, replace_country_code
import pandas as pd

st.set_page_config(
    page_title="Limpieza de datos",
    page_icon="🧹",
)


# LIMPIEZA DE DATOS #
st.title('Limpieza de datos')
st.markdown("""
En esta sección se muestra el proceso de limpieza de datos realizado para obtener el dataset final.
""")

# Crear un texto para que el usuario sepa que el dataset está cargando.
data_load_state = st.text('Cargando datos...')
# Iniciar carga de datos.
data = load_data()
# Notificar al usuario que los datos se han cargado correctamente.
data_load_state.text("Hecho! Los datos se han cargado correctamente.")

st.subheader('Datos crudos')
st.markdown("""
A continuación se muestran los las primeras 5 filas del dataset.
""")
st.write(data.head())
if st.checkbox('Mostrar todo el dataset sin procesar'):
    dimension = data.shape
    st.write(data)
    st.write(
        f"El dataset original contiene {dimension[0]} filas y {dimension[1]} columnas.")


st.subheader('Borrar columnas innecesarias')
st.markdown("""
En este apartado se eliminan las columnas que no son necesarias para el análisis.

Eliminamos las columnas **"INDICATOR"** y **"FREQUENCY"** porque no aportan información relevante para el análisis.
""")
# Eliminar columnas innecesarias.
data = data.drop(['INDICATOR', 'FREQUENCY'], axis=1)


# Mostrar datos sin columnas innecesarias.
if st.checkbox("Mostrar todas las columnas"):
	st.text("Columns:")
	st.write(data.columns)


st.markdown("""
- La columna **"LOCATION"** proporciona información sobre la ubicación geográfica de los datos.
- La columna **"SUBJECT"** describe el tipo de carne.
- La columna **"MEASURE"** describe la medida utilizada para recopilar los datos.
- La columna **"TIME"** describe el período de tiempo durante el cual se recopilaron los datos (año).
- La columna **"VALUE"** es el valor numérico real del consumo de carne.
""")
	    
st.sidebar.subheader('Índice')
st.sidebar.markdown("""
- [Datos crudos](#datos-crudos)
- [Borrar columnas innecesarias](#borrar-columnas-innecesarias)
- [Cambio de estructura del dataset](#cambio-de-estructura-del-dataset)
- [Cambiar códigos de país por sus nombres](#cambio-de-c-digos-de-ubicaci-n-por-sus-nombres)
- [Comprobar valores nulos](#comprobar-valores-nulos)
- [Cambio de estructura del dataset](#cambio-de-estructura-del-dataset)
- [Guardar dataset final](#guardar-dataset-final)
- [Descargar dataset final](#descargar-dataset-final)
""")

# Mostrar datos sin columnas innecesarias.
st.subheader("Descripción de los datos")
st.write(data.describe())

st.subheader('Comprobar valores nulos')
st.markdown("""
En este apartado se comprueba si hay valores nulos en el dataset.
""")
# Comprobar valores nulos.
null_counts = data.isnull().sum()
null_dict = {'Valores nulos': null_counts}
st.write(pd.DataFrame(null_dict))

if st.checkbox("Mostrar datos sin columnas innecesarias"):
    st.write(data)

st.subheader('Cambio de estructura del dataset')
st.markdown("""
En este apartado se cambia la estructura del dataset para que cada fila contenga los datos de un país, un tipo de carne, medidas de kilogramos y toneladas y un año.

Del dataset se observa que la columna measure contiene los datos de consumo de carne en kilogramos y toneladas, por lo que se deben separar en diferentes columnas para poder analizarlos por separado.

Para ello, se utiliza la función **pivot_table** de pandas.
""")
# Cambiar estructura del dataset.
new_data = split_measure(data)

# Mostrar la nueva estructura del dataset.
st.write(new_data)
if st.checkbox("Mostrar descripción del nuevo dataset"):
    st.write(new_data.describe())

# Cambiar códigos de países por nombres de países.
st.subheader('Cambio de códigos de ubicación por sus nombres')
st.markdown("""
En este apartado se cambian los códigos de países por sus nombres.

La columna **"LOCATION"** proporciona información sobre la ubicación geográfica de los datos según su código de país. Por lo que se cambian los códigos de países por sus nombres para que sea más fácil de entender.

Para ello, se utiliza la función **replace** de pandas.
""")
new_data = replace_country_code(new_data)

st.write(new_data)

# Guardar dataset final.
st.subheader('Guardar dataset final')
st.markdown("""
En este apartado se guarda el dataset final en formato csv.
""")

# Guardar dataset final.
new_data.to_csv('data/processed_data.csv', index=False)

st.markdown("""
El dataset final contiene los datos de consumo de carne de diferentes países, tipos de carne, medidas y años.
""")

st.subheader('Descripción del dataset final')
st.write(new_data.describe())

# descargar dataset final.
st.subheader('Descargar dataset final')
st.markdown("""
En este apartado se descarga el dataset final en formato csv.
""")
            

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# Convertir dataframe a csv.
csv = convert_df(new_data)
# Descargar dataset final.
st.download_button(label='Descargar dataset final', data=csv, file_name='processed_data.csv', mime='text/csv')   



