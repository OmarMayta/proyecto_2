import streamlit as st

# Función clasificar el puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"

# Menú Lateral
st.sidebar.title("Menú de Navegación")
opcion = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Clasificación de Puntajes"])

# Sección Inicio
if opcion == "Inicio":
    st.title("Bienvenido a la Aplicación")
    st.write("Mueva el deslizador para ver cómo se clasifica el puntaje en tiempo real")

    # Filtro Desplazable
    puntaje_slider = st.slider("Seleccione un puntaje:", 0, 100, 50)

    # Mostrar el puntaje clasificado en tiempo real
    resultado_slider = clasificar_puntaje(puntaje_slider)
    st.write(f"El puntaje seleccionado es: {puntaje_slider}")
    st.success(f"El puntaje es clasificado como: {resultado_slider}")

# Sección Clasificación de Puntajes
elif opcion == "Clasificación de Puntajes":
    st.title("Clasificación de Puntajes")
    st.write("Ingrese un puntaje y el sistema lo clasificará")

    # Entrada de usuario
    puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

    # Botón clasificar
    if st.button("Clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"El puntaje es clasificado como: {resultado}")
