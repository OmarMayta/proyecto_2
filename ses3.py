import streamlit as st

# Función clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"

# Interfaz en Streamlit
st.title("Clasificación de Puntajes")
st.write("Ingrese un puntaje y el sistema lo clasificará")

# Entrada de usuario
puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

# Botón clasificar
if st.button("Clasificar"):
    resultado = clasificar_puntaje(puntaje)
    st.success(f"El puntaje es clasificado como: {resultado}")
