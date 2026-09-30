import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import random
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Taller Python",
    page_icon="💻",
    layout="wide"
)

opciones_menu  = ["Introducción", "Primeros pasos en Python", "Cadenas de caracteres", "Listas", "Operadores", "Estructuras selectivas"]

opciones = option_menu(
    menu_title=None,
    options=opciones_menu,
    icons=['0-circle','1-circle', 'alphabet', 'list', '4-circle', 'calculator'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if opciones == "Introducción":
    st.markdown(f'<h1 style="font-size: 40px; text-align: center; color: #4E4E8A">Taller de Python Básico para Humanidades</h1>', unsafe_allow_html=True)
    st.write("""
    El taller **Python básico para Humanidades** ofrece una introducción 
    práctica a la programación utilizando [**Google Colab**](https://workspace.google.com/marketplace/app/colaboratory/1014160490159?flow_type=2&pann=ogb) 
    como entorno de trabajo.

    El taller busca desarrollar habilidades básicas de programación y 
    pensamiento lógico que puedan aplicarse en actividades académicas 
    y profesionales relacionadas con la organización, procesamiento y 
    análisis de información.
    """)

    st.divider()

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">¿Qué es la programación?</h2>', unsafe_allow_html=True)

    st.markdown("""
    Programar es dar **instrucciones precisas y ordenadas** a una computadora
    para resolver un problema o automatizar una tarea. Igual que seguir una receta.
    """)
    
    st.markdown(f'<h2 style="font-size: 25px; text-align: center; color: #7f3213">🍳 En la cocina</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("1 🥕 Ingredientes")
            st.caption("Lo que necesitamos para preparar el plato.")
    
    with col2:
        with st.container(border=True):
            st.markdown("2 👨‍🍳 Seguir los pasos")
            st.caption("Realizamos las instrucciones en orden.")
    
    with col3:
        with st.container(border=True):
            st.markdown("3 🍽️ Plato terminado")
            st.caption("Obtenemos el resultado final.")
    
    st.markdown(f'<h2 style="font-size: 25px; text-align: center; color: #7f3213">💻 En un programa</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("1 📥 Datos de entrada")
            st.caption("Información que recibe el programa.")
    
    with col2:
        with st.container(border=True):
            st.markdown("2 ⚙️ Instrucciones")
            st.caption("El programa procesa los datos.")
    
    with col3:
        with st.container(border=True):
            st.markdown("3 📤 Resultado")
            st.caption("Información que genera el programa.")
        
    st.divider()

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">🐍 Python en las Humanidades</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 📚")
            st.markdown("#### Literatura")
            st.write("Analizar palabras, personajes, temas y estilos de escritura.")

    with col2:
        with st.container(border=True):
            st.markdown("### 🗣️")
            st.markdown("#### Lingüística")
            st.write("Analizar corpus, comparar lenguas y encontrar patrones.")
    
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container(border=True):
            st.markdown("### 🏺")
            st.markdown("#### Arqueología")
            st.write("Organizar datos, analizar materiales y trabajar con información espacial.")
    
    with col4:
        with st.container(border=True):
            st.markdown("### 🏛️")
            st.markdown("#### Historia")
            st.write("Procesar documentos, organizar datos y construir cronologías.")
    
    st.divider()
        
    st.markdown('<h2 style="font-size: 30px; text-align: center; color: #4E8A4E;">''Temas del taller 📚''</h2>',unsafe_allow_html=True)

    st.markdown("""
    1. **Primeros pasos en Python**
    2. **Cadenas, listas y operadores**
    3. **Condicionales, bucles y funciones**
    4. **Librerías**
    """)

    st.divider()


    st.markdown(
        '<h2 style="font-size: 30px; text-align: center; color: #4E8A4E;">'
        'Docentes 👩🏻‍💻👨🏻‍💻'
        '</h2>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image("foto_luisa.png", width = 550)
        st.markdown(
            '<h3 style="text-align: center; color: #7f3213;">'
            'Luisa Gomez Saltachin'
            '</h3>',
            unsafe_allow_html=True
        )

        st.markdown("""
        **Bachillera en Lingüística – PUCP**  
        Estudiante de último ciclo de la Maestría en Lingüística – PUCP  

        **Experiencia:**  
        Predocente de la Facultad de Artes y Ciencias de la Comunicación  

        **Área de interés:**  
        Lingüística computacional  

        📧 luisa.gomez@pucp.edu.pe
        """)

    with col2:
        st.image("foto_salvador.jpeg", width = 480)
        st.markdown(
            '<h3 style="text-align: center; color: #7f3213;">'
            'Salvador Farfán Perez'
            '</h3>',
            unsafe_allow_html=True
        )

        st.markdown("""
        **Estudiante de Ingeniería Informática – PUCP**  
        Décimo ciclo  

        **Experiencia:**  
        Practicante del Laboratorio de Humanidades Digitales – PUCP  

        **Área de formación:**  
        Desarrollo y gestión de proyectos de software  

        📧 a20211862@pucp.edu.pe
        """)

elif opciones == "Primeros pasos en Python":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Primeros pasos en Python</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.link_button(
            "📓 Archivo Colab - Clase 1",
            "https://colab.research.google.com/drive/19TxemzRkXJ3Wl28HaqhK8X6zHTbO8gdh",
            use_container_width=True
        )
    
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Tipos de celdas</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 1️⃣ Celdas de texto")
            st.write("Notas y explicaciones utilizando **Markdown**.")
    
    with col2:
        with st.container(border=True):
            st.markdown("### 2️⃣ Celdas de código")
            st.write("Aquí escribes y ejecutas tus programas en **Python**.")

    st.divider() ## Separador

    st.subheader("📓 ¿Cómo se ve un cuaderno de Colab?")

    with st.container(border=True):
    
        st.markdown("### 📄 Cuaderno_Modulo1.ipynb")
    
        st.markdown("**## Introducción**")
    
        st.caption("1 · Celda de texto (Markdown)")
    
        st.divider()
    
        st.code('print("Hola mundo")', language="python")
    
        st.caption("2 · Celda de código")
    
        st.success("Hola mundo")
    
        st.caption("3 · Resultado de la ejecución")
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Función print() ▶️</h2>', unsafe_allow_html=True)
    st.code("print('¡Hola Mundo!')", language='python')
    st.markdown(f"La función `print()` permite mostrar la información en la pantalla.")

    st.markdown(f'<h2 style="font-size: 28px; text-align: center; color: #4E8A4E">¿Qué está ocurriendo aquí? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Usamos la función `print()` para mostrar el texto **"¡Hola Mundo!"** en la pantalla.
    La función `print()` permite mostrar cadena de caracteres (string), números o resultados de operaciones.
    
    **Nota:**  
    Una función es un bloque de código que realiza una tarea específica.
    Las funciones reciben entradas (*argumentos*) y producen salidas (*resultados*)
    
    En este caso, la **entrada** es `"¡Hola Mundo!"` y la **salida** es el mismo texto mostrado en pantalla.
    """)
    st.divider() ## Separador
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Función help() 🆘</h2>', unsafe_allow_html=True)
    st.code("help(print)", language="python")
    st.markdown(f"Esta función permite consultar en la documentación de Python.")

    st.markdown(f'<h2 style="font-size: 28px; text-align: center; color: #4E8A4E">¿Qué está ocurriendo aquí? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Usamos la función `help()` para consultar información sobre otra función.

    En este caso, `help(print)` muestra la documentación de la función `print()`.
    
    **Nota:**
    Python tiene documentación integrada que permite entender funciones, ver parámetros y aprender su uso correcto.
    Esto es muy útil cuando estamos aprendiendo programación.
    """)
    st.divider() ## Separador
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">¿Cómo escribir comentarios? #️⃣</h2>', unsafe_allow_html=True)
    st.code("""# Este es un comentario
    print("Hola")
    """, language="python")

    st.markdown(f'<h2 style="font-size: 28px; text-align: center; color: #4E8A4E">¿Qué está ocurriendo aquí? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Los comentarios son líneas que Python **no ejecuta**.
    Sirven para explicar el código; documentar programas; y recordar qué hace cada parte.
    Los comentarios empiezan con `#`.
    
    **Nota:**
    Los comentarios son leídos por humanos, no por Python.
    """)
    st.divider() ## Separador
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E4E8A">Errores en Python ❌</h2>', unsafe_allow_html=True)
    st.code("print(Hola)", language="python")
    st.markdown(f"Esto genera un error porque faltan comillas.")

    st.markdown(f'<h2 style="font-size: 28px; text-align: center; color: #4E8A4E">¿Qué está ocurriendo aquí? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Este código produce un error.
    Python interpreta **Hola** como una variable.
    Pero como no existe, aparece un error: **NameError**
    
    **¿Cómo se corrige?**
    Agregando comillas:
    `print("Hola")`
    
    **Nota:**
    Los errores son parte normal del proceso de programar.
    Aprender a leer errores ayuda a entender Python, corregir código y mejorar como programador.
    
    **Observación:**
    Los errores comunes son olvidar las comillas, olvidar las paréntesis, escribir mal una función y no indentar.
    """)
    st.write("")

    col22, col23, col24 = st.columns([1,2,1])

    with col23:
    
        if st.button("Resolver algunos ejercicios prácticos"):
        
            @st.dialog("Ejercicios prácticos")
            def show_info():
                st.write("Escribe las respuestas como código Python:")
    
                st.divider()
    
                # Ejercicio 1
                st.subheader("Ejercicio 1")
    
                r1 = st.text_input(
                    "Escribe un programa que muestre tu apellido usando print():"
                )
    
                if r1:
                    if "print" in r1:
                        st.success("Correcto. Estás usando print().")
                    else:
                        st.warning("Recuerda usar print()")
    
                # Ejercicio 2
                st.subheader("Ejercicio 2")
    
                r2 = st.text_input(
                    "Muestra el resultado de 20 + 26:"
                )
    
                if r2:
                    if "20" in r2 and "26" in r2:
                        st.success("Bien. Estás usando los números correctos.")
                    else:
                        st.info("Verifica los valores.")
    
                # Ejercicio 3
                st.subheader("Ejercicio 3")
    
                r3 = st.text_input(
                    "Usa help() con la función type:"
                )
    
                if r3:
                    if "help" in r3 and "type" in r3:
                        st.success("Correcto.")
                    else:
                        st.warning("La respuesta esperada es algo como: help(type)")
    
                st.divider()
    
                if st.button("Ver solución"):
                    st.code("""
                    print("Gomez")     
                    print(20 + 26)
                    help(type)
                    """, language="python")
            show_info()
            


   
   
   







