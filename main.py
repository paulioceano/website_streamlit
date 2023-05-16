import streamlit as st
import pandas
from send_email import send_email

# Esta es la primera linea que se debe agregar con streamlit, define la configuración de la página
st.set_page_config(layout="wide")

# Se agrega un encabezado para la página.
st.header("El Mejor Sitio Jamás Creado.")

# Como el texto es algo largo, primero se define en una variable y luego se agrega.
description_text = """
Obviamente, ese título tiene un fuerte componente de sarcasmo.

Este es un simple ejemplo que ilustra lo sencillo que es usar Streamlit para crear una simple página web,
dinámica.

Streamlit es una excelente opción para los programadores de Python que desean comenzar a desarrollar aplicaciones web 
de manera rápida y sencilla. A diferencia de otras bibliotecas de Python para crear aplicaciones web, Streamlit es fácil 
de aprender y usar, y no requiere conocimientos previos de desarrollo web.
"""
st.write(description_text)

# Con subheader se definen los sutítulos
st.subheader("Nuestras Redes")

# Esto es para definir las columnas para dividir el contenido en 3 partes
col1, col2, col3 = st.columns(3)

# Debido a que ste es un ejemplo simple, usamos pandas para leer un archivo CSV con el contenido "dinámico".
df = pandas.read_csv("data.csv")

# Se agrega el contenido de cada columna: una imagen, el título y su URL
with col1:
    st.image("images/" + df["image"][0], width=150)
    st.subheader(df["title"][0])
    st.write(f"[{df['label'][0]}]({df['url'][0]})")

with col2:
    st.image("images/" + df["image"][1], width=150)
    st.subheader(df["title"][1])
    st.write(f"[{df['label'][1]}]({df['url'][1]})")

with col3:
    st.image("images/" + df["image"][2], width=150)
    st.subheader(df["title"][2])
    st.write(f"[{df['label'][2]}]({df['url'][2]})")

# Acá se agrega una sección con un formulario de contacto
st.title("Contacto")

# Se crea el formulario con 2 campos, uno para el correo y un área de texto para el mensaje.
with st.form(key="contact_form"):
    user_email = st.text_input("Tu correo electrónico")
    raw_message = st.text_area("Tu mensaje")

# Se formatea el mensaje como se quiere que le llegue al receptor, si se agrega el Subject, este será el asunto del correo.
    message = f"""\
Subject: Tienes un email de: {user_email}

Contacto: {user_email}
Mensaje: {raw_message}
"""

# Se agrega el botón de enviar
    button = st.form_submit_button("Enviar")

# Si el botón es presionado, se envía el mensaje usando la función send_mail y se muestra un texto informativo.
    if button:
        send_email(message)
        st.info("Tu mensaje fue enviado exitosamente")
