import smtplib
import ssl


def send_email(message):
    # Se configura el servidor SMTP de Gmail, acá solo debes agregar el usuario, la contraseña de aplicación y el email
    # del receptor. Este email puede ser el mismo del usuario si se quiere.
    host = "smtp.gmail.com"
    port = 465
    username = "APP_USERNAME"
    password = "APP_PASSWORD"
    receiver = "EMAIL_RECEIVER"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
