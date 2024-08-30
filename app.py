import pandas as pd
import streamlit as st
import plotly.express as px

#leer los datos
car_data = pd.read_csv("vehicles_us.csv")

st.header("Anàlisis Exploratorio")
hist_button = st.button('Construir histograma') #crear un boton

scatter_button = st.button('Grafico de dispersiòn')

if hist_button: #accion del boton

    st.write('Creaciòn de un histograma para el conjunto de datos de anuncios de venta de coches') #mensaje del botòn

    fig = px.histogram(car_data, x='odometer') #crear histograma

    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creacion de un grafico de dispersion para el contunto de datos de anuncios de venta de coches')
    
    fig = px.scatter(car_data, x="odometer", y="price") #crear un grafico de dispersion
    
    st.plotly_chart(fig, use_container_width=True)