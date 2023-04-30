import streamlit as st
from funciones import load_data
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
	    
# Algo importante que resaltar es que la columna **"SUBJECT"** contiene los datos de consumo de carne de diferentes animales, por lo que se deben separar en diferentes columnas para poder analizarlos por separado.

# st.subheader('Separar datos de diferentes animales')
# st.markdown("""
# En este apartado se separan los datos de consumo de carne de diferentes animales en diferentes columnas.
# """)
# # Separar datos de diferentes animales.
# new_data = data.pivot_table(index=['LOCATION', 'SUBJECT', 'MEASURE', 'TIME'], columns='SUBJECT', values='VALUE').reset_index()
# # Renombrar columnas.
# new_data = new_data.rename(columns={'LOCATION': 'País', 'MEASURE': 'Medida', 'TIME': 'Año',
#                        'BEEF': 'Carne de vacuno', 'PIG': 'Carne de cerdo', 'POULTRY': 'Carne de ave', 'SHEEP': 'Carne de oveja'})

# # Eliminar columna subject porque ya no es necesaria.
# new_data = new_data.drop(['SUBJECT'], axis=1)

# # Mostrar datos sin columnas innecesarias.
# if st.checkbox("Mostrar datos sin columnas innecesarias"):
# 	st.write(new_data)

# st.write(new_data)

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

# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show', ('Rows', 'Columns'))
if data_dim == 'Rows':
	st.text("Showing Length of Rows")
	st.write(len(data))
if data_dim == 'Columns':
	st.text("Showing Length of Columns")
	st.write(data.shape[1])
