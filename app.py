import streamlit as st

st.title("Mi primera aplicacion en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Ramiro Cahuata")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

Sesión = st.selectbox("Seleccione una sesion", ["seccion1","seccion2","seccion3"])
