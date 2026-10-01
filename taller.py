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

opciones_menu  = ["Introducción", "Primeros pasos en Python", "Cadenas de caracteres", "Listas", "Operadores"]

opciones = option_menu(
    menu_title=None,
    options=opciones_menu,
    icons=['0-circle','1-circle', 'alphabet', 'list', 'calculator'],
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
            "📓 Colab - Clase 1",
            "https://colab.research.google.com/drive/19TxemzRkXJ3Wl28HaqhK8X6zHTbO8gdh",
            use_container_width=True
        )
    
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Tipos de celdas</h2>', unsafe_allow_html=True)
    
    with st.container(border=True):
    
        st.markdown("### 📄 Prueba.ipynb")
    
        st.markdown("**# Formato de encabezado principal**")
        st.markdown("**## Formato de encabezado secundario**")
        
        st.caption("1 · Celda de texto (Markdown), donde podemos escribir y dar formato a títulos, explicaciones y otros contenidos que pueden acompañar nuestro código")
    
        st.divider()
    
        st.code('print("Hola mundo")', language="python")
    
        st.caption("2 · Celda de código, donde escribes y ejecutas códigos de Python")
    
        st.success("Hola mundo")
    
        st.caption("3 · Salida (output), resultado de la ejecución")

    st.info("""
        📝 **Nota**
        
        **Ejecutar:** `Ctrl + Enter`  
        
        **Guardar:** los cambios se guardan automáticamente en Google Drive.
        """)

    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">¿Cómo escribir comentarios? #️⃣</h2>', unsafe_allow_html=True)
    st.code("""# Este programa imprime un saludo
    print("Hola") """, language="python")

    st.info("""
    **¿Qué está ocurriendo aquí?**
    
    Todo lo que va después de `#` es un comentario, Python lo ignora al ejecutar.
    Sirven para explicar la intención del código a otros y a ti mismo en el futuro.
    """)
    
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Función print() ▶️</h2>', unsafe_allow_html=True)
    st.markdown(f"Muestra en pantalla el texto que recibe como argumento. Funciona con texto y también con números.")
    st.code("""
        print('¡Hola Mundo!')
        print(2026)""", language='python')
    st.success("""
        ¡Hola Mundo!
        
        2026 """)

    st.markdown(f'<h3 style="text-align: center; color: #7f3213">Sintaxis básica</h3>', unsafe_allow_html=True)

    st.code("print(*args, sep=' ', end='\\n')", language="python")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### `sep`")
            st.write("Separa los valores que se imprimen.")
            st.code("sep=' '", language="python")
    
    with col2:
        with st.container(border=True):
            st.markdown("### `end`")
            st.write("Se añade al final de lo que se imprime.")
            st.code("end='\\n'", language="python")
   
    st.markdown("### Ejemplo 🅰️ `sep='\\n'`, `end='\\t'`")
    
    st.code("""
    print("Mundial", 2026, sep="\\n", end="\\t")
    print("hola")
    """, language="python")
    
    st.markdown("**Salida:**")
    
    st.code("""
    Mundial
    2026    hola""")
    
    st.markdown("### Ejemplo 🅱️ `sep='\\t'`, `end='\\n'`")
    
    st.code("""
    print("Mundial", 2026, sep="\\t", end="\\n")
    print("hola")
    """, language="python")
    
    st.markdown("**Salida:**")
    
    st.code("""
    Mundial    2026
    hola """)
    
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E"> 🧩 Variables </h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("variable.png", width = 1000)

    st.write("""
    En Python, una variable es un espacio donde almacenamos información (un valor o un dato) para poder usarla después en nuestro programa.
    Para asignar un valor a una variable utilizamos el símbolo `=`

    📌 **Reglas para nombrar variables:**
    - Pueden contener letras, números y guiones bajos (`_`).  
    - No pueden comenzar con un número.  
    - No pueden tener espacios.  
    - No deben usar **caracteres especiales** (como `@`, `#`, `!`, etc.).  
    - No pueden ser **palabras reservadas de Python** (como `if`, `for`, `while`, etc.).  

    Puedes revisar la lista completa aquí: [Palabras reservadas en Python](https://www.w3schools.com/python/python_ref_keywords.asp)
    """, unsafe_allow_html=True)
   
    st.markdown("""Explora cómo funcionan las variables en Python. Puedes escribir valores y ver cómo cambian.""")
    
    # Input interactivo
    nombre_variable = st.text_input("Escribe un nombre para tu variable:", value="animal")
    valor_variable = st.text_input("Asigna un valor a tu variable:", value="perro")
    
    # Mostrar resultado dinámico
    if nombre_variable:
        st.markdown("### Resultado")
        st.code(f"{nombre_variable} = '{valor_variable}'\nprint({nombre_variable})", language="python")
        st.write("Salida:")
        st.success(valor_variable)
    
    # Explicación de reasignación
    st.markdown(f'<h3 style="text-align: center; color: #7f3213"> 🔁 Reasignación de variables </h3>', unsafe_allow_html=True)
    valor1 = st.text_input("Primer valor de la variable:", value="guau", key="v1")
    valor2 = st.text_input("Nuevo valor de la variable:", value="sonido del perro", key="v2")
    
    st.code(f"""
    perro = "{valor1}"
    print(perro)
    
    perro = "{valor2}"
    print(perro)
    """, language="python")
    
    st.write("Salida:")
    st.success(valor2)    
    st.info("""**Observa:** la variable guarda siempre el **último valor asignado**.""")
    
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
            


   
   
   







