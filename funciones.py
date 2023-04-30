import streamlit as st
import pandas as pd

# CARGA DE DATOS #
dataset = 'data/meat_consumption.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(dataset)
    # Transformar los títulos de columnas a mayúsculas.
    df.columns = [column.upper() for column in df.columns]
    return df
