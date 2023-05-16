import streamlit as st
import pandas
from send_email import send_email

st.set_page_config(layout="wide")

st.header("El Mejor Sitio Jamás Creado.")

description_text = """
Obviamente, ese título tiene un fuerte componente de sarcasmo.

Este es un simple ejemplo que ilustra lo sencillo que es usar Streamlit para crear una simple página web,
dinámica.

Streamlit es una excelente opción para los programadores de Python que desean comenzar a desarrollar aplicaciones web 
de manera rápida y sencilla. A diferencia de otras bibliotecas de Python para crear aplicaciones web, Streamlit es fácil 
de aprender y usar, y no requiere conocimientos previos de desarrollo web.
"""
st.write(description_text)

st.subheader("Nuestras Redes")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

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

st.title("Contacto")

with st.form(key="contact_form"):
    user_email = st.text_input("Tu correo electrónico")
    raw_message = st.text_area("Tu mensaje")
    message = f"""\
Subject: Tienes un email de: {user_email}

Contacto: {user_email}
Mensaje: {raw_message}
"""
    button = st.form_submit_button("Enviar")
    if button:
        send_email(message)
        st.info("Tu mensaje fue enviado exitosamente")
