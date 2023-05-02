import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style = 'dark', palette = 'deep')

# CARGA DE DATOS #
dataset = 'data/meat_consumption.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(dataset)
    # Transformar los títulos de columnas a mayúsculas.
    df.columns = [column.upper() for column in df.columns]
    return df

data = load_data()

# Eliminar columnas innecesarias.
data = data.drop(['INDICATOR', 'FREQUENCY'], axis=1)

def split_measure(df):

    # Seleccionar columnas de interés
    df = df[['LOCATION', 'SUBJECT', 'TIME', 'MEASURE', 'VALUE']]

    # Aplicar pivot
    df_pivot = df.pivot(
        index=['LOCATION', 'SUBJECT', 'TIME'], columns='MEASURE', values='VALUE')
    df_pivot = df_pivot.reset_index()
    df_pivot.columns.name = ''
    return df_pivot

def replace_country_code(df):
    paises = {
        'AUS': 'Australia',
        'BGD': 'Bangladesh',
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
        'DZA': 'Argelia',
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
    df['CODE'] = df['LOCATION']
    df['LOCATION'] = df['LOCATION'].replace(paises)
    df = df.reindex(columns=["CODE", "LOCATION", "SUBJECT", "TIME", "KG_CAP", "THND_TONNE"])
    return df


def plot_meat_consumption(df=data, country='World'):
    ndf = split_measure(data)
    ndf = replace_country_code(ndf)

    tipos = {'BEEF': 'Ternera', 'PIG': 'Cerdo',
             'POULTRY': 'Pollo (Aves)', 'SHEEP': 'Cordero'}
    # filtrar los datos por país
    kg_cap = ndf
    thnd_tonne = ndf

    kg_cap_wld = kg_cap[kg_cap['LOCATION'] == country]
    thnd_tonne_wld = thnd_tonne[thnd_tonne['LOCATION'] == country]

    subjects = ndf['SUBJECT'].unique()

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    colors = sns.color_palette('Paired', n_colors=len(subjects)*2+1)

    for i, subject in enumerate(subjects):
        row = i // 2
        col = i % 2

        data1 = thnd_tonne_wld[thnd_tonne_wld['SUBJECT'] == subject]
        axs[row, col].bar(data1['TIME'], data1['THND_TONNE'], color=colors[i*2])
        axs[row, col].set_ylabel("Miles de Toneladas", fontsize=12)

        ax2 = axs[row, col].twinx()

        data2 = kg_cap_wld[kg_cap_wld['SUBJECT'] == subject]
        ax2.plot(data2['TIME'], data2['KG_CAP'], color=colors[i*2+1])

        ax2.set_ylabel("Kg per cápita", fontsize=10)

        axs[row, col].set_title(tipos[subject])

    plt.tight_layout()

    return fig


def plot_consumption_all(df=data, country='World'):
    beef = df.loc[(df['SUBJECT'] == 'BEEF') & (
        df['LOCATION'] == country) & (df['TIME'] > 1999)]


    pig = df.loc[(df['SUBJECT'] == 'PIG') & (
        df['LOCATION'] == country) & (df['TIME'] > 1999)]
    poultry = df.loc[(df['SUBJECT'] == 'POULTRY') & (
        df['LOCATION'] == country) & (df['TIME'] > 1999)]
    sheep = df.loc[(df['SUBJECT'] == 'SHEEP') & (
        df['LOCATION'] == country) & (df['TIME'] > 1999)]

    fig, ax = plt.subplots()

    ax.plot(beef['TIME'], beef['KG_CAP'], linestyle='--', label='Ternera')
    ax.plot(pig['TIME'], pig['KG_CAP'], color='green',
            linestyle='--', label='Cerdo')
    ax.plot(poultry['TIME'], poultry['KG_CAP'],
            color='red', linestyle=':', label='Aves')
    ax.plot(sheep['TIME'], sheep['KG_CAP'],
            color='orange', linestyle='-.', label='Oveja')
    #ax.set_title(f'Consumo de carne en la {country} (2000-2025)')
    ax.set_ylabel('Kg per cápita')
    ax.set_xlabel('Año')
    ax.legend(loc='upper left')

    return fig
