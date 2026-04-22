import streamlit as st
import random
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Ejercicios Streamlit", layout="wide")

st.title("Ejercicios de Streamlit")


# EJERCICIO 1: Saludo Simple

st.subheader("Ejercicio 1: Saludo Simple")
nombre = st.text_input("Escribe tu nombre:", key="ejercicio1_nombre")
if nombre:
    st.write(f"¡Hola, {nombre}!")
st.divider()


# EJERCICIO 2: Calculadora de Producto

st.subheader("Ejercicio 2: Calculadora de Producto")
col1, col2 = st.columns(2)
with col1:
    numero1 = st.number_input("Primer número:", key="ejercicio2_num1")
with col2:
    numero2 = st.number_input("Segundo número:", key="ejercicio2_num2")

producto = numero1 * numero2
st.write(f"Resultado: {numero1} × {numero2} = {producto}")

if numero1 > 100 or numero2 > 100:
    st.warning("Números grandes")
st.divider()


# EJERCICIO 3: Convertidor de Temperatura

st.subheader("Ejercicio 3: Convertidor de Temperatura")
opcion_temp = st.radio("Elige la conversión:", 
                       ("Celsius a Fahrenheit", "Fahrenheit a Celsius"),
                       key="ejercicio3_radio")
temperatura = st.number_input("Ingresa la temperatura:", key="ejercicio3_temp")

if opcion_temp == "Celsius a Fahrenheit":
    resultado_temp = (temperatura * 9/5) + 32
    st.write(f"{temperatura}°C = {resultado_temp:.2f}°F")
else:
    resultado_temp = (temperatura - 32) * 5/9
    st.write(f"{temperatura}°F = {resultado_temp:.2f}°C")
st.divider()


# EJERCICIO 4: Galería de Mascotas (Tabs)

st.subheader("Ejercicio 4: Galería de Mascotas")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.image("https://images.unsplash.com/photo-1574158622682-e40e69881006?w=500", 
             caption="Gato adorable", use_column_width=True)
    if st.button("Me gusta", key="gato_like"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.image("https://images.unsplash.com/photo-1633722715463-d30628519e89?w=500",
             caption="Perro feliz", use_column_width=True)
    if st.button("Me gusta", key="perro_like"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.image("https://images.unsplash.com/photo-1444464666175-1642156dc396?w=500",
             caption="Águila majestuosa", use_column_width=True)
    if st.button("Me gusta", key="aguila_like"):
        st.toast("Te gusta esta mascota")

st.divider()


# EJERCICIO 5: Caja de Comentarios (Formulario)

st.subheader("Ejercicio 5: Caja de Comentarios")

with st.form(key="formulario_comentarios"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviado = st.form_submit_button("Enviar")
    
    if enviado and mensaje.strip():
        datos = {
            "Asunto": asunto,
            "Mensaje": mensaje
        }
        st.json(datos)
    elif enviado and not mensaje.strip():
        st.warning("El mensaje no puede estar vacío")

st.divider()


# EJERCICIO 6: Login Simulado (Session State)

st.subheader("Ejercicio 6: Login Simulado")

# Inicializar session state
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "usuario_actual" not in st.session_state:
    st.session_state.usuario_actual = ""

if not st.session_state.logueado:
    usuario = st.text_input("Usuario:", key="login_usuario")
    contraseña = st.text_input("Contraseña:", type="password", key="login_contraseña")
    
    if st.button("Ingresar"):
        if usuario == "admin" and contraseña == "1234":
            st.session_state.logueado = True
            st.session_state.usuario_actual = usuario
            st.success("Ingreso exitoso!")
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")
else:
    st.success(f"Bienvenido, {st.session_state.usuario_actual}!")
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.session_state.usuario_actual = ""
        st.rerun()

st.divider()


# EJERCICIO 7: Lista de Compras (Session State)

st.subheader("Ejercicio 7: Lista de Compras")

# Inicializar session state para lista de compras
if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

col1, col2 = st.columns([4, 1])

with col1:
    producto_nuevo = st.text_input("Ingresa un producto:", key="producto_input")

with col2:
    agregar = st.button("Agregar")

if agregar and producto_nuevo.strip():
    st.session_state.lista_compras.append(producto_nuevo)
    st.rerun()

col1, col2 = st.columns([4, 1])
with col2:
    limpiar = st.button("Limpiar Lista")

if limpiar:
    st.session_state.lista_compras = []
    st.rerun()

if st.session_state.lista_compras:
    st.write("Tu lista de compras:")
    for i, producto in enumerate(st.session_state.lista_compras, 1):
        st.write(f"{i}. {producto}")
else:
    st.info("La lista está vacía. ¡Agrega algunos productos!")

st.divider()


# EJERCICIO 8: Gráfico Interactivo

st.subheader("Ejercicio 8: Gráfico Interactivo")

# Inicializar session state para números aleatorios
if "numeros_aleatorios" not in st.session_state:
    st.session_state.numeros_aleatorios = []

col1, col2 = st.columns([3, 1])

with col1:
    n = st.slider("Selecciona la cantidad de números (N):", 
                   min_value=10, max_value=100, value=50, key="slider_n")

with col2:
    regenerar = st.button("Regenerar")

# Generar números aleatorios
if regenerar or len(st.session_state.numeros_aleatorios) != n:
    st.session_state.numeros_aleatorios = [random.randint(0, 100) for _ in range(n)]

# Crear DataFrame para el gráfico
df = pd.DataFrame({
    "Valor": st.session_state.numeros_aleatorios,
    "Índice": range(len(st.session_state.numeros_aleatorios))
})

st.line_chart(df.set_index("Índice"))

st.info(f"Se muestran {len(st.session_state.numeros_aleatorios)} números aleatorios")
