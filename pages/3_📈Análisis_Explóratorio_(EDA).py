import math
import streamlit as st
from funciones import load_data, plot_meat_consumption, plot_consumption_all, plot_meat_subject, split_measure, replace_country_code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

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


paises = {
    'AUS': 'Australia',
    'CAN': 'Canada',
    'JPN': 'Japan',
    'KOR': 'South Korea',
    'MEX': 'Mexico',
    'NZL': 'New Zealand',
    'TUR': 'Turkey',
    'USA': 'United States',
    'ARG': 'Argentina',
    'BRA': 'Brazil',
    'CHL': 'Chile',
    'CHN': 'China',
    'COL': 'Colombia',
    'EGY': 'Egypt',
    'ETH': 'Ethiopia',
    'IND': 'India',
    'IDN': 'Indonesia',
    'IRN': 'Iran',
    'ISR': 'Israel',
    'KAZ': 'Kazakhstan',
    'MYS': 'Malaysia',
    'NGA': 'Nigeria',
    'PAK': 'Pakistan',
    'PRY': 'Paraguay',
    'PER': 'Peru',
    'PHL': 'Philippines',
    'RUS': 'Russia',
    'SAU': 'Saudi Arabia',
    'ZAF': 'South Africa',
    'THA': 'Thailand',
    'TZA': 'Tanzania',
    'UKR': 'Ukraine',
    'URY': 'Uruguay',
    'VNM': 'Vietnam',
    'NOR': 'Norway',
    'CHE': 'Switzerland',
    'GBR': 'United Kingdom',
    'GHA': 'Ghana',
    'HTI': 'Haiti',
    'MOZ': 'Mozambique',
    'SDN': 'Sudan',
    'ZMB': 'Zambia',
    'EU27': 'European Union',
    'WLD': 'World'
}

def prepare_data(df):
    df = split_measure(df)
    df = replace_country_code(df)
    return df

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

lista_paises = sorted(list(paises.values()))
select = st.selectbox('Seleccionar país', lista_paises)

df = load_data()
df = prepare_data(df)
# df_select = df[df['SUBJECT'] == tipos[select]]

st.subheader('Consumo por tipo de carne')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Todos", "Ternera", "Cerdo", "Aves", "Cordero"])


with tab1:
    st.subheader('Consumo de carne en ' + str(select) + ' (2000-2028)')
    grafico2 = plot_consumption_all(df, country=select)
    st.pyplot(grafico2)


with tab2:
   st.header("Ternera")
   grafico_ternera = plot_meat_subject(df, country=select, subject='BEEF')
   st.pyplot(grafico_ternera)

with tab3:
   st.header("Cerdo")
   grafico_cerdo = plot_meat_subject(df, country=select, subject='PIG')
   st.pyplot(grafico_cerdo)

with tab4:
   st.header("Aves")
   grafico_aves = plot_meat_subject(df, country=select, subject='POULTRY')
   st.pyplot(grafico_aves)

with tab5:
    st.header("Cordero")
    grafico_cordero = plot_meat_subject(df, country=select, subject='SHEEP')
    st.pyplot(grafico_cordero)



grafico = plot_meat_consumption(country=select)
with st.spinner('Cargando gráfico...'):
    st.pyplot(grafico)
    st.markdown('En el gráfico anterior, la línea representa el consumo per cápita de carne en kg, mientras que las barras representan el consumo total de carne en toneladas.')


# SIDEBAR: FILTRO POR AÑO #
st.sidebar.subheader('Filtrar por año')
year_to_filter = st.sidebar.slider('Año', 1990, 2023, 2028)
df_year = select_year(df, year_to_filter)