# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Los misterios de la fe</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("p.jpg", caption='Let it be', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
 Mi nombre es Samuel Arturo Gonzales Sullón. Soy estudiante de periodismo de la Pontificia Universidad Católica del Perú (PUCP) y debo decir que lo que más valoro de mi carrera es la libertad que me ha sido otorgada para poder expresar problemáticas sociales, espirituales y psicológicas que comúnmente permanecen soterradas en la esfera pública. En el futuro, tengo el propósito de contribuir, a través de plataformas digitales y otros medios de comunicación, a la difusión de la fe cristiana. Más del 80% de la población del Perú es católica y, sin embargo, la devoción es un concepto que ha quedado limitado a festividades y rituales tradicionales sin el debido entendimiento de lo que realmente es la fe. Considero que las enseñanzas de Cristo Jesús son necesarias y transformadoras en este mundo contemporáneo, en el que sobre todo la juventud se encuentra en una crisis de salud mental.
 """

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
 Al principio fue difícil para mí
 aprender el lenguaje de programación básico, pero es cierto que tanto el profesor como la jefa de práctica del curso siempre se mostraron comprensivos con nuestras limitaciones y nos brindaron la oportunidad de subsanar notas y también de depurar el conocimiento aprendido a través de varias asesorías. Personalmente, la programación ha enriquecido mi conocimiento en Dios, puesto que nosotros, al programar, estamos creando comandos, generando el diseño de un submundo en el que las personas podrán interactuar. Entendí que la realidad misma posee un diseño absoluto y perfecto; y es cierto que donde existe orden y diseño absoluto, debe existir necesariamente una mente soberana y omnisciente. Específicamente en cuanto a mi carrera, me gustaría aplicar el conocimiento aprendido en este curso para crear páginas web con bases de datos sobre problemáticas poco atendidas como el suicidio, la adicción a las drogas, la adicción a la pornografía, la ansiedad social, etc. Me gustaría poder ayudar a mis semejantes a identificar los principales factores que desencadenan estos trastornos"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
#st.video("pc3.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://drive.google.com/file/d/1my_nxlrJKF6rLIhFk17VwYrJ5tymfr7T/view?usp=sharing" target="_blank"><button>Click para ver mi video-explicación en drive :V</button></a>'
st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón.


# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Mis gráficos favoritos</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['¿Cómo le fue a la Vecchia Signora?', 'Goles promedio Milan vs. Fiore', 'Frecuencia de palabras']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciónese un gráfico 7u7', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == '¿Cómo le fue a la Vecchia Signora?':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Durante la temporada 2022/23 en la Serie A Italiana en cuanto a su cuota goleadora. Se muestran sus 38 goles en condición de local y sus 18 goles en condición de visitante</div>", unsafe_allow_html=True)
    sidebar.image("vechia.png", caption='Vecchia Signora', width=500)
    pass
elif grafico_seleccionado == 'Goles promedio Milan vs. Fiore':
    sidebar.markdown("<div style='text-align: justify'>El gráfico se encuentra una comparación entre el promedio de goles en condición de visitante entre el AC Milán y la Fiorentina, mostrando que ambos obtuvieron un 50%..</div>", unsafe_allow_html=True)
    sidebar.image("promedio.png", caption='Milan vs Fiore Comparación', width=500)
    pass
elif grafico_seleccionado == 'Frecuencia de palabras':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico se encarga de contabilizar y comparar la cantidad de veces en que se mencionó la palabra “paro”, “Dina”, “Bukele”, “delincuencia”, “criminales” y “ley” en un texto específico que se nos fue otorgado. Brindando como resultado que la palabra más mencionada fue “paro” con un total de 3 veces.</div>", unsafe_allow_html=True)
    sidebar.image("palabras.png", caption='Mapa de las lenguas sudamericanas', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
