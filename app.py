import streamlit as st

st.title("Mi primera aplicacion en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Ramiro Cahuata")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

Sesión = st.sidebar.selectbox("Seleccione una sesion", ["seccion1","seccion2","seccion3"])

if sesion == "Sesión 1":

  st.write("Bienvenido la sesión 1")

  st.image("Python_logo.png" )

 

elif sesion == "Sesión 2":

  st.write("Bienvenido la sesión 2")
