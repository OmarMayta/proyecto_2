import streamlit as st
# Función clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >=85:
        return "Excelente"
    elif puntaje >=70:
        return "Bueno"
    else:
        return "Necesita Mejorar"

#interfaz en streamlit
st.title("Clasificacion de puntajes")
st.write("Ingrese puntaje y el sistema lo clasificará")

#entrada de usuario
puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max value=100, step=1)

#boton clasificar
    if st.button("Clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"El puntaje es clasificado como: {resultado}")

