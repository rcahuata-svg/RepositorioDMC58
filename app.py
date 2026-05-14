import streamlit as st

 

st.title("Mi primera aplicación en python")

 

st.sidebar.title("Parámetros")

 

st.write("Elaborado por: Carlos Carrillo")

 

st.sidebar.image("DMC.png")

 

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

 

if sesion == "Sesión 1":

  st.write("Bienvenido la sesión 1")

  st.image("Python_logo.png" )


