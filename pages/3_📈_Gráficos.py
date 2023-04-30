import streamlit as st
from funciones import load_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Gráficos",
    page_icon="📈",
)

# Funciones para filtrar los datos.


def select_year(df, year):
    df_year = df[df['TIME'] == year]
    return df_year


def plot_subjects(ndf):
    kg_cap = ndf[ndf["MEASURE"] == 'KG_CAP']
    thnd_tonne = ndf[ndf['MEASURE'] == 'THND_TONNE']

    kg_cap_wld = kg_cap[kg_cap['LOCATION'] == 'World']
    thnd_tonne_wld = thnd_tonne[thnd_tonne['LOCATION'] == 'World']

    subjects = ndf['SUBJECT'].unique()

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    colors = sns.color_palette('Paired', n_colors=len(subjects)*2+1)

    for i, subject in enumerate(subjects):
        row = i // 2
        col = i % 2

        data1 = thnd_tonne_wld[thnd_tonne_wld['SUBJECT'] == subject]
        axs[row, col].bar(data1['TIME'], data1['VALUE'], color=colors[i*2])
        axs[row, col].set_ylabel("Miles de Toneladas", fontsize=12)

        ax2 = axs[row, col].twinx()

        data2 = kg_cap_wld[kg_cap_wld['SUBJECT'] == subject]
        ax2.plot(data2['TIME'], data2['VALUE'], color=colors[i*2+1])

        ax2.set_ylabel("Kg per cápita", fontsize=10)

        axs[row, col].set_title(subject)

    plt.tight_layout()
    plt.show()

st.sidebar.title('Filtros')
st.sidebar.subheader('Filtrar por país')
st.sidebar.markdown("""
En este apartado se puede seleccionar el país que se quiere analizar.
""")

st.title('Gráficos')
st.markdown("""
En esta sección se muestran los gráficos que se han realizado para el análisis de los datos.
""")


# SIDEBAR: FILTRO POR TIPO DE CARNE #
st.sidebar.subheader('Filtrar por')
tipos = {'Carne de ternera': 'BEEF', 'Carne de cerdo': 'PIG',
         'Carne de pollo (aves)': 'POULTRY', 'Carne de oveja': 'SHEEP'}
select = st.sidebar.selectbox('Tipo de carne', [
                              'Carne de ternera', 'Carne de cerdo', 'Carne de pollo (aves)', 'Carne de oveja'])

df = load_data()
df_select = df[df['SUBJECT'] == tipos[select]]


# SIDEBAR: FILTRO POR AÑO #
st.sidebar.subheader('Filtrar por año')
year_to_filter = st.sidebar.slider('Año', 1990, 2023, 2028)
df_year = select_year(df, year_to_filter)
