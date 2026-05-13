import streamlit as st

st.title("Mi primera aplicacion en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Ramiro Cahuata")

sesion = st.selectbox("Seleccione una sesión"),["Sesión 1","Sesión2"]
