# Ejemplo de un Sitio Web usando Streamlit
Este es un ejemplo de un sitio web con elementos básicos, como textos y enlaces y un formulario de contacto.

### Requisitos
Antes de comenzar, debe tener instalado Streamlit en su entorno:

````commandline
pip install streamlit
````

Además, debe configurar su servidor SMTP para el envío de los mensajes del formulario de contacto. 

Para este ejemplo, solo debe sustituir ```APP_USERNAME```, ```APP_PASSWORD``` e ```EMAIL_RECEIVER``` con los valores correspondientes del usuario y contraseña de aplicación de Gmail y el email del receptor de los mensajes

### USO
Para la ejecución de la aplicación, abre tu consola de comandos y navega hasta el directorio donde guardaste el archivo Python. Luego, escribe lo siguiente

````commandline
streamlit run main.py
````

Esto iniciará la aplicación y te dará una URL que puedes abrir en tu navegador web para ver la aplicación en acción.

### Contribuciones
¡Las contribuciones son bienvenidas! Siéntase libre de crear una solicitud de extracción si desea mejorar este código o agregar nuevas características.

### Licencia
Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más información.