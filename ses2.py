import streamlit as st
from algoritmos import AlgoritmosSecuenciales

#Título de la Aplicación
st.title ("Algoritmos Secuenciales con POO en Streamlit")

# Entrada de usuario
numero = st.number_input("Ingrese un numero entero positivo", min_value=1, value=5, step=1)

# Instanciamos la clase con el numero ingresado
algoritmos = AlgoritmosSecuenciales(numero)

#Botones para ejecutar los algoritmos secuenciales
if st.button("Calcular Suma de N numeros"):
    st.success(f"la suma de los primeros {numero} número es: {algoritmos.suma_n_numeros()}")