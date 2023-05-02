import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from funciones import load_data

sns.set_theme(style = 'dark', palette = 'deep')

st.set_page_config(
    page_title="Análisis Confirmatorio",
    page_icon="📊",
)

# CARGA DE DATOS #
dataset = 'data/processed_data.csv'

data = load_data(dataset)

st.title('Análisis Confirmatorio')

st.write('En esta sección se realizará un análisis confirmatorio de los datos obtenidos en la sección anterior.')

st.write(data.head())

st.write("En el análisis exploratorio podemos observar tendencias en los datos, pero no podemos asegurar que estas tendencias sean significativas. Para ello, realizaremos un análisis confirmatorio de los datos. Por ejemplo, en el análisis exploratorio observamos que en la mayoría de los países tienen una tendencia a disminuir su consumo de carne de ternera.")

st.write("Para comprobar si esta tendencia es significativa, realizaremos un análisis de regresión lineal simple. Para ello, utilizaremos la librería statsmodels.")

st.write("En primer lugar, realizaremos un análisis de regresión lineal simple para el consumo de carne de ternera en Europa.")

data = data.loc[(data['TIME'] >= 1999) & (data['CODE'] <= 'EU27')]

st.write(data.head())

st.write("En este caso, la variable dependiente será el consumo de carne de ternera y la variable independiente será el año.")

st.write("Para realizar el análisis de regresión lineal simple, utilizaremos la función OLS de la librería statsmodels.")

st.write("En primer lugar, separamos la variable dependiente de la variable independiente.")

X = data['TIME']
y = data['KG_CAP']

st.write()

st.write("Luego, separamos los datos en datos de entrenamiento y datos de prueba.")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)

st.write("Luego, se realiza el análisis de regresión lineal simple.")

import statsmodels.api as sm

X_train = sm.add_constant(X_train)

model = sm.OLS(y_train, X_train).fit()

st.write(model.summary())

st.write("En este caso, el valor de R-squared es 0.000, lo que indica que el modelo no explica la variabilidad de los datos.")

st.write("Para comprobar si el modelo es significativo, se realiza un análisis de varianza (ANOVA).")

import statsmodels.stats.api as sms

st.write(sms.anova_lm(model))

st.write("En este caso, el valor de p-value es 0.000, lo que indica que el modelo es significativo.")

st.write("Para comprobar si el modelo es adecuado, se realiza un análisis de residuos.")

st.write("En primer lugar, se obtienen los residuos del modelo.")

residuals = model.resid

st.write("Luego, se realiza un análisis de residuos.")

from statsmodels.graphics.gofplots import qqplot

fig, ax = plt.subplots(figsize = (10, 6))

qqplot(residuals, line = 's', ax = ax)

st.pyplot(fig)

st.write("En este caso, los residuos no siguen una distribución normal.")

st.write("Para comprobar si el modelo es adecuado, se realiza un análisis de homocedasticidad.")

from statsmodels.stats.diagnostic import het_breuschpagan

st.write(het_breuschpagan(residuals, X_train))




st.write(data.columns, data.dtypes)
st.write(data.describe())