import streamlit as st

#Título de la Aplicación
st.title ("Bienvenido a mi aplicación")

#Solicitar el nombre del Usuario
nombre = st.text_input("Por Favor, ingresa tu nombre: ")

#Mostrar el saludo si el usuario ingresa su nombre
if nombre:
    st.write(f"Hola, {nombre}! Bienvenido a esta aplicación  web de Streamlit")