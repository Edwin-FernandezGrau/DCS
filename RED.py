# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:49:57 2021

@author: DELL
"""

import streamlit as st
import pandas as pd
#import numpy as np
import plotly
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Distribución de Clínicas - Sanitas")
base = pd.read_excel("RED.xlsx")
st.sidebar.write("PARAMETROS")
option = st.sidebar.selectbox(
     'Selecciones su plan',
     ('Base PEAS', 'Base Esencial', 'Base Plus',"ADIC 1","ADIC 2"),4)

base1 = base[base[option]=="a"]
base1["size"] = 7

filtro1 = list(base1["COBERTURA"].unique())
filtro1.insert(0,"TODOS")


option1 = st.sidebar.selectbox('Selecciones cobertura',filtro1,1)



if option1 == "TODOS":
    option2 = st.sidebar.selectbox("seleccione RED", ["TODOS"],0)
    mask=(base1["COBERTURA"]!="TODOS")
else:
    mask=(base["COBERTURA"]== option1)
    filtro2= list(base1[mask]["RED2"].unique())
    filtro2.insert(0,"TODOS") 
    option2 = st.sidebar.selectbox("seleccione RED", filtro2,0)

if option2 != "TODOS":
    mask =(mask)&(base1["RED2"]==option2)

base1 = base1[mask]

base1.rename(columns={'Latitude':'lat','Longitude':'lon'},inplace=True)

st.sidebar.write("----")
option3 = st.sidebar.selectbox('Selecciones mapa',['basic', 'streets', 'outdoors'],0)
option4 =st.sidebar.slider("Tamaño", 7,15,9)
px.set_mapbox_access_token("pk.eyJ1IjoiZWZlcm5hbmRlejk1IiwiYSI6ImNrdWhkMmYyODJkMnEyb3Fqdm9yODJxaHIifQ.n-2MSsIfHeZscJEp4LpXwA")

fig = px.scatter_mapbox(base1, lat="lat", lon="lon",     #color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire,
                  size_max=option4,
                  zoom=10,
                  hover_name = 'NOMBRE COMERCIAL CLÍNICA',
                  width=1100,
                  height=825,
                  center={"lat":-12.07,"lon":-77.03},#text="TELÉFONO"
                  color="RED2",
                  mapbox_style=option3,
                  size="size"
                  )

st.plotly_chart(fig)