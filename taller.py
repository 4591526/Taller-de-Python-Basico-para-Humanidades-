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

opciones_menu  = ["Introducción", "Primeros pasos en Python", "Cadenas, listas y operadores", "Condicionales, bucles y funciones", "Bibliotecas"]

opciones = option_menu(
    menu_title=None,
    options=opciones_menu,
    icons=['0-circle','1-circle', '2-circle', '3-circle', '4-circle'],
    menu_icon="cast",
    default_index=4,
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
    4. **Bibliotecas: random, WordCloud, spaCy, pandas y Matplotlib**
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
    
    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E"> 🧩 Variables </h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("variable.png", width = 1000)

    st.write("""
    Una variable es un espacio donde se almacena información. La etiqueta es el nombre; el contenido es el valor.

    📌 **Reglas para nombrar variables:**
    - Solo pueden contener letras, números y guiones bajos (`_`) 
    - No pueden comenzar con un número
    - No pueden tener espacios.  
    - No deben usar caracteres especiales (como `@`, `#`, `!`, etc.).  
    - No pueden ser palabras reservadas de Python (como `if`, `for`, `while`, etc.).

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
    st.info(""" **Observa:** la variable guarda siempre el último valor asignado.""")
    
    st.divider() ## Separador

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Tipos de datos en Python</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("tipo_dato.png", width = 1000)

    valor = st.text_input("Escribe un valor (ejemplo: 11, 3.14, 'Humanidades', True):")

    if valor:
        try:
            evaluado = eval(valor)
            st.success(f"Tipo de dato: {type(evaluado)}")
        except:
            st.warning("No se pudo interpretar automáticamente. Se considera texto.")
            st.write("Tipo de dato:", type(valor))
            st.write("Valor:", valor)
    
    st.divider() ## Separador

    st.markdown('<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">🧮 Operadores aritméticos</h2>', unsafe_allow_html=True)

    # Explicación
    st.markdown("""
    Los <b>operadores aritméticos</b> permiten realizar operaciones matemáticas entre valores.
    """, unsafe_allow_html=True)

    # Tabla de operadores
    operadores = {
        "Operador": ["+", "-", "*", "/", "//", "%", "**"],
        "Nombre": [
            "Suma",
            "Resta",
            "Multiplicación",
            "División",
            "División entera",
            "Módulo",
            "Potencia"
        ],
        "Ejemplo": [
            "3 + 2 → 5",
            "3 - 2 → 1",
            "3 * 2 → 6",
            "3 / 2 → 1.5",
            "3 // 2 → 1",
            "3 % 2 → 1",
            "3 ** 2 → 9"
        ]
    }

    df_operadores = pd.DataFrame(operadores)
    st.dataframe(df_operadores, use_container_width=True)

    num1 = st.number_input("Ingresa el primer número:", value=10.0)
    num2 = st.number_input("Ingresa el segundo número:", value=2.0)

    operacion = st.selectbox(
        "Elige una operación:",
        ["+", "-", "*", "/", "//", "%", "**"]
    )

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        resultado = num1 / num2 if num2 != 0 else "Error (división por cero)"
    elif operacion == "//":
        resultado = num1 // num2 if num2 != 0 else "Error (división por cero)"
    elif operacion == "%":
        resultado = num1 % num2 if num2 != 0 else "Error (división por cero)"
    elif operacion == "**":
        resultado = num1 ** num2

    st.success(f"Resultado: {resultado}")

    st.divider()

    st.markdown('<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">📝 Operadores de asignación</h2>', unsafe_allow_html=True)
    
    # Explicación
    st.markdown("""
    Los <b>operadores de asignación</b> permiten asignar un valor a una variable
    o actualizar su valor utilizando una operación matemática.
    """, unsafe_allow_html=True)
    
    # Tabla de operadores
    operadores = {
        "Operador": ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**="],
        "Nombre": [
            "Asignación",
            "Suma y asignación",
            "Resta y asignación",
            "Multiplicación y asignación",
            "División y asignación",
            "División entera y asignación",
            "Módulo y asignación",
            "Potencia y asignación"
        ],
        "Ejemplo": [
            "x = 10 → 10",
            "x += 3 → 13",
            "x -= 3 → 7",
            "x *= 3 → 30",
            "x /= 2 → 5.0",
            "x //= 3 → 3",
            "x %= 3 → 1",
            "x **= 2 → 100"
        ]
    }
    
    df_operadores = pd.DataFrame(operadores)
    
    st.dataframe(
        df_operadores,
        use_container_width=True,
        hide_index=True
    )
    
    # Valores para la demostración
    numero = st.number_input(
        "Ingresa un número:",
        value=10.0
    )
    
    operacion = st.selectbox(
        "Elige un operador de asignación:",
        ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**="]
    )
    
    valor = st.number_input(
        "Ingresa el valor de la operación:",
        value=2.0
    )
    
    # Aplicación del operador
    resultado = numero
    
    if operacion == "=":
        resultado = valor
    
    elif operacion == "+=":
        resultado += valor
    
    elif operacion == "-=":
        resultado -= valor
    
    elif operacion == "*=":
        resultado *= valor
    
    elif operacion == "/=":
        resultado = resultado / valor if valor != 0 else "Error (división por cero)"
    
    elif operacion == "//=":
        resultado = resultado // valor if valor != 0 else "Error (división por cero)"
    
    elif operacion == "%=":
        resultado = resultado % valor if valor != 0 else "Error (división por cero)"
    
    elif operacion == "**=":
        resultado **= valor
    
    st.success(f"Resultado: {resultado}")

    st.divider()

    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">⌨️ input() </h2>',unsafe_allow_html=True)
    
    # Explicación
    st.markdown("""
    La función <b>input()</b> permite solicitar información al usuario
    durante la ejecución de un programa.
    """, unsafe_allow_html=True)
    
    # Tabla explicativa
    conceptos = {
        "Elemento": [
            "input()",
            "Mensaje",
            "Variable",
            "int",
            "float"
        ],
        "Función": [
            "Solicita un dato al usuario",
            "Indica qué información ingresar",
            "Guarda el dato ingresado",
            "Convierte el dato a número entero",
            "Convierte el dato a número decimal"
        ],
        "Ejemplo": [
            "input()",
            'input("¿Cuál es tu nombre? ")',
            'nombre = input("Nombre: ")',
            'edad = int(input("Edad: "))',
            'precio = float(input("Precio: "))'
        ]
    }
    
    df_input = pd.DataFrame(conceptos)
    
    st.dataframe(
        df_input,
        use_container_width=True,
        hide_index=True
    )
    
    nombre = st.text_input("¿Cuál es tu nombre?")
    
    edad = st.number_input(
        "¿Cuál es tu edad?",
        min_value=0,
        max_value=120,
        value=20,
        step=1
    )
    
    if nombre:
        st.success(f"Hola, {nombre}. Tienes {edad} años.")

    st.divider()
    
    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("Resolver ejercicios prácticos"):
    
            @st.dialog("Ejercicios prácticos")
            def show_info():
    
                st.write("Escribe las respuestas como código Python.")
    
                st.divider()
    
                # ==================================================
                # EJERCICIO 1
                # ==================================================
    
                st.subheader("🟢 Ejercicio 1 · Variables")
    
                r1 = st.text_area(
                    "Crea tres variables: nombre (texto), edad (entero) y promedio (decimal)."
                )
    
                if r1:
                    if (
                        "nombre" in r1
                        and "edad" in r1
                        and "promedio" in r1
                    ):
                        st.success("Bien. Has creado las tres variables.")
                    else:
                        st.warning(
                            "Debes crear las variables nombre, edad y promedio."
                        )
    
                # ==================================================
                # EJERCICIO 2
                # ==================================================
    
                st.subheader("🔵 Ejercicio 2 · Tipos de datos")
    
                r2 = st.text_area(
                    "Crea una variable llamada carrera con el valor 'Lingüística' "
                    "y muestra su tipo de dato usando type()."
                )
    
                if r2:
                    if "carrera" in r2 and "type" in r2:
                        st.success("Correcto. Estás utilizando una variable y type().")
                    else:
                        st.warning(
                            "Recuerda crear la variable carrera y utilizar type()."
                        )
    
                # ==================================================
                # EJERCICIO 3
                # ==================================================
    
                st.subheader("🟣 Ejercicio 3 · print()")
    
                r3 = st.text_area(
                    "Crea una variable llamada libro con el nombre de un libro "
                    "y muestra su contenido utilizando print()."
                )
    
                if r3:
                    if "libro" in r3 and "print" in r3:
                        st.success("Correcto. Estás usando una variable con print().")
                    else:
                        st.warning(
                            "Debes utilizar una variable llamada libro y print()."
                        )
    
                # ==================================================
                # EJERCICIO 4
                # ==================================================
    
                st.subheader("🟠 Ejercicio 4 · input()")
    
                r4 = st.text_area(
                    "Solicita al usuario su nombre y guarda la respuesta "
                    "en una variable llamada nombre."
                )
    
                if r4:
                    if "input" in r4 and "nombre" in r4:
                        st.success("Correcto. Estás utilizando input().")
                    else:
                        st.warning(
                            "Recuerda utilizar input() y guardar el resultado en nombre."
                        )
    
                # ==================================================
                # EJERCICIO 5
                # ==================================================
    
                st.subheader("🔴 Ejercicio 5 · Operadores aritméticos")
    
                r5 = st.text_area(
                    "Crea dos variables: a = 15 y b = 4. "
                    "Calcula su suma, resta, multiplicación y división."
                )
    
                if r5:
                    if (
                        "15" in r5
                        and "4" in r5
                        and "+" in r5
                        and "-" in r5
                        and "*" in r5
                        and "/" in r5
                    ):
                        st.success("Correcto. Has utilizado los cuatro operadores.")
                    else:
                        st.warning(
                            "Debes utilizar 15, 4 y los operadores +, -, * y /."
                        )
                
                st.divider()
    
                # ==================================================
                # SOLUCIONES
                # ==================================================
    
                if st.button("Ver soluciones"):
    
                    st.markdown("### 💡 Soluciones")
    
                    st.markdown("**Ejercicio 1 · Variables y tipos de datos**")
                    st.code("""
    nombre = "Luisa"
    edad = 25
    promedio = 17.5
    """, language="python")
    
                    st.markdown("**Ejercicio 2 · Tipos de datos**")
                    st.code("""
    carrera = "Lingüística"
    print(type(carrera))
    """, language="python")
    
                    st.markdown("**Ejercicio 3 · print()**")
                    st.code("""
    libro = "El Aleph"
    print(libro)
    """, language="python")
    
                    st.markdown("**Ejercicio 4 · input()**")
                    st.code("""
    nombre = input("¿Cuál es tu nombre? ")
    print(nombre)
    """, language="python")
    
                    st.markdown("**Ejercicio 5 · Operadores aritméticos**")
                    st.code("""
    a = 15
    b = 4
    
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    """, language="python")
                    
    
            show_info()
                
elif opciones == "Cadenas, listas y operadores":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Cadenas, listas y operadores</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.link_button(
            "📓 Colab - Clase 2",
            "https://colab.research.google.com/drive/1ipCmJfSsJDIDmS6MdO9Fls3Rif4a3kxU",
            use_container_width=True
        )
    
    st.divider() ## Separador
    
    st.markdown(
    f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">'
    f'Métodos de cadenas de caracteres</h2>',
    unsafe_allow_html=True
    )
    
    with st.container(border=True):
    
        st.markdown("### 🔤 Métodos para trabajar con texto")
    
        st.markdown("**1. `split()` — Dividir una cadena**")
        st.code(
            'texto = "historia arqueología lingüística"\n'
            'print(texto.split())',
            language="python"
        )
        st.caption(
            "Divide una cadena de caracteres en una lista de palabras. "
            "Por defecto, utiliza los espacios como separadores."
        )
        st.success("['historia', 'arqueología', 'lingüística']")
    
        st.divider()
    
        st.markdown("**2. `count()` — Contar apariciones**")
        st.code(
            'texto = "lingüística"\n'
            'print(texto.count("i"))',
            language="python"
        )
        st.caption(
            "Cuenta cuántas veces aparece un carácter o una secuencia "
            "de caracteres dentro de una cadena."
        )
        st.success("3")
    
        st.divider()
    
        st.markdown("**3. `replace()` — Reemplazar texto**")
        st.code(
            'texto = "Me gusta la historia"\n'
            'print(texto.replace("historia", "arqueología"))',
            language="python"
        )
        st.caption(
            "Reemplaza una palabra o secuencia de caracteres por otra."
        )
        st.success("Me gusta la arqueología")
    
        st.divider()
    
        st.markdown("**4. `lower()` — Convertir a minúsculas**")
        st.code(
            'texto = "LINGÜÍSTICA"\n'
            'print(texto.lower())',
            language="python"
        )
        st.caption(
            "Convierte todas las letras de una cadena a minúsculas."
        )
        st.success("lingüística")
    
        st.divider()
    
        st.markdown("**5. `upper()` — Convertir a mayúsculas**")
        st.code(
            'texto = "lingüística"\n'
            'print(texto.upper())',
            language="python"
        )
        st.caption(
            "Convierte todas las letras de una cadena a mayúsculas."
        )
        st.success("LINGÜÍSTICA")
    
    st.info("""
            📝 **Nota**
        
            **`split()`** devuelve una lista de elementos.  
            **`count()`** devuelve un número entero.  
            **`replace()`**, **`lower()`** y **`upper()`** devuelven cadenas de caracteres.
        
            Estos métodos no modifican la cadena original: devuelven un nuevo resultado.
            """)
              
    st.divider()
              
    st.markdown(
    f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">'
    f'Función len()</h2>',
    unsafe_allow_html=True
    )
    
    with st.container(border=True):
    
        st.markdown("### 🔢 Contar elementos")
    
        st.markdown("**1. Contar caracteres de una cadena**")
        st.code(
            'texto = "Lingüística"\n'
            'print(len(texto))',
            language="python"
        )
        st.caption(
            "La función len() devuelve la cantidad de caracteres "
            "que contiene una cadena, incluidos los espacios."
        )
        st.success("11")
    
        st.divider()
    
        st.markdown("**2. Contar elementos de una lista**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'print(len(lenguas))',
            language="python"
        )
        st.caption(
            "También permite conocer la cantidad de elementos "
            "que contiene una lista."
        )
        st.success("3")
    
        st.divider()
    
        st.markdown("**3. Contar caracteres, incluidos los espacios**")
        st.code(
            'frase = "Hola mundo"\n'
            'print(len(frase))',
            language="python"
        )
        st.caption(
            "Cada letra y el espacio entre las palabras cuentan "
            "como un carácter."
        )
        st.success("10")
    
    st.info("""
            📝 **Nota**
        
            **`len()`** devuelve un número entero (`int`).
        
            - En una cadena, cuenta caracteres.
            - En una lista, cuenta elementos.
            - Los espacios también cuentan como caracteres.
            """)  

    st.divider()
              
    st.markdown(
            f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">'
            f'Estructura f-string</h2>',
            unsafe_allow_html=True)
        
    with st.container(border=True):
        
        st.markdown("### 🧩 Insertar variables en una cadena")
        
        st.markdown("**1. Estructura básica**")
        st.code(
                'nombre = "María"\n'
                'print(f"Hola, {nombre}")',
                language="python"
            )
        st.caption(
                "La letra f antes de las comillas permite insertar "
                "variables dentro de una cadena. Las variables se escriben "
                "entre llaves {}."
            )
        st.success("Hola, María")
        
        st.divider()
        
        st.markdown("**2. Insertar varias variables**")
        st.code(
                'lengua = "quechua"\n'
                'familia = "quechumara"\n'
                'print(f"La lengua {lengua} pertenece a la familia {familia}.")',
                language="python"
            )
        st.caption(
                "Puedes incluir varias variables en una misma cadena "
                "para construir mensajes personalizados."
            )
        st.success("La lengua quechua pertenece a la familia quechumara.")
        
        st.divider()
        
        st.markdown("**3. Insertar operaciones y funciones**")
        st.code(
                'palabra = "lingüística"\n'
                'print(f"La palabra tiene {len(palabra)} caracteres.")',
                language="python"
            )
        st.caption(
                "Dentro de las llaves también puedes ejecutar operaciones "
                "o llamar funciones."
            )
        st.success("La palabra tiene 11 caracteres.")
        
        st.divider()
        
        st.markdown("**4. Combinar texto y números**")
        st.code(
                'libro = "El principito"\n'
                'paginas = 96\n'
                'print(f"El libro {libro} tiene {paginas} páginas.")',
                language="python"
            )
        st.caption(
                "Las f-strings permiten combinar variables de distintos "
                "tipos de datos en un mismo mensaje."
            )
        st.success("El libro El principito tiene 96 páginas.")
        
    st.info("""
                📝 **Nota**
            
                **Estructura:** `f"Texto {variable}"`
            
                - La letra `f` se coloca antes de las comillas.
                - Las llaves `{}` indican dónde se inserta una variable o expresión.
                - El resultado es una cadena de caracteres (`str`).
                """)
            
    st.divider()
        
    st.markdown(
        f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">'
        f'Métodos de listas</h2>',
        unsafe_allow_html=True
    )
    
    with st.container(border=True):
    
        st.markdown("### 📚 Métodos para trabajar con listas")
    
        st.markdown("**1. `append()` — Agregar un elemento**")
        st.code(
            'lenguas = ["quechua", "aimara"]\n'
            'lenguas.append("shipibo-konibo")\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Agrega un elemento al final de la lista.")
        st.success("['quechua', 'aimara', 'shipibo-konibo']")
    
        st.divider()
    
        st.markdown("**2. `extend()` — Agregar varios elementos**")
        st.code(
            'lenguas = ["quechua", "aimara"]\n'
            'lenguas.extend(["ashaninka", "awajún"])\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Agrega los elementos de otra colección al final de la lista.")
        st.success("['quechua', 'aimara', 'ashaninka', 'awajún']")
    
        st.divider()
    
        st.markdown("**3. `insert()` — Insertar un elemento**")
        st.code(
            'lenguas = ["quechua", "aimara"]\n'
            'lenguas.insert(1, "ashaninka")\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Inserta un elemento en la posición indicada. La primera posición es 0.")
        st.success("['quechua', 'ashaninka', 'aimara']")
    
        st.divider()
    
        st.markdown("**4. `remove()` — Eliminar un elemento**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'lenguas.remove("aimara")\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Elimina la primera aparición del valor indicado.")
        st.success("['quechua', 'ashaninka']")
    
        st.divider()
    
        st.markdown("**5. `pop()` — Eliminar por posición**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'eliminada = lenguas.pop(1)\n'
            'print(eliminada)\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Elimina y devuelve el elemento de la posición indicada. Sin argumento, elimina el último.")
        st.success("aimara\n['quechua', 'ashaninka']")
    
        st.divider()
    
        st.markdown("**6. `index()` — Encontrar la posición**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'print(lenguas.index("aimara"))',
            language="python"
        )
        st.caption("Devuelve el índice de la primera aparición del elemento.")
        st.success("1")
    
        st.divider()
    
        st.markdown("**7. `sort()` — Ordenar elementos**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'lenguas.sort()\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Ordena la lista en orden ascendente. En cadenas, el orden es alfabético según los valores Unicode.")
        st.success("['aimara', 'ashaninka', 'quechua']")
    
        st.divider()
    
        st.markdown("**8. `reverse()` — Invertir el orden**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'lenguas.reverse()\n'
            'print(lenguas)',
            language="python"
        )
        st.caption("Invierte el orden actual de los elementos, sin ordenarlos alfabéticamente.")
        st.success("['ashaninka', 'aimara', 'quechua']")

    st.info("""
        📝 **Nota**
    
        - `append()` agrega un elemento.
        - `extend()` agrega varios elementos.
        - `insert()` inserta en una posición específica.
        - `remove()` elimina por valor.
        - `pop()` elimina por posición y devuelve el elemento.
        - `index()` encuentra la posición de un valor.
        - `sort()` ordena la lista.
        - `reverse()` invierte el orden actual.
    
        **Importante:** la mayoría de estos métodos modifica la lista original.
        `index()` devuelve un número entero y `pop()` devuelve el elemento eliminado.
        """)
    
    st.divider()    
        
    st.markdown(
        f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">'
        f'Operadores booleanos</h2>',
        unsafe_allow_html=True
    )
    
    with st.container(border=True):
    
        st.markdown("### ⚖️ 1. Operadores comparativos")
    
        st.markdown("**Comparar valores**")
        st.code(
            'edad = 20\n'
            'print(edad == 20)\n'
            'print(edad != 18)\n'
            'print(edad > 18)\n'
            'print(edad < 25)\n'
            'print(edad >= 20)\n'
            'print(edad <= 19)',
            language="python"
        )
        st.caption("Comparan dos valores y devuelven True o False.")
        st.success("True\nTrue\nTrue\nTrue\nTrue\nFalse")
    
        st.markdown("""
        | Operador | Significado |
        |---|---|
        | `==` | Igual a |
        | `!=` | Diferente de |
        | `>` | Mayor que |
        | `<` | Menor que |
        | `>=` | Mayor o igual que |
        | `<=` | Menor o igual que |
        """)
    
        st.divider()
    
        st.markdown("### 🔎 2. Operadores de pertenencia")
    
        st.markdown("**Comprobar si un elemento pertenece a una colección**")
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            'print("quechua" in lenguas)\n'
            'print("shipibo-konibo" not in lenguas)',
            language="python"
        )
        st.caption("Comprueban si un elemento está presente o ausente en una colección.")
        st.success("True\nTrue")
    
        st.markdown("""
        | Operador | Significado |
        |---|---|
        | `in` | Pertenece a |
        | `not in` | No pertenece a |
        """)
    
        st.divider()
    
        st.markdown("### 🧠 3. Operadores lógicos")
    
        st.markdown("**Combinar condiciones**")
        st.code(
            'edad = 22\n'
            'estudiante = True\n'
            'print(edad >= 18 and estudiante)\n'
            'print(edad < 18 or estudiante)\n'
            'print(not estudiante)',
            language="python"
        )
        st.caption("Permiten combinar o negar expresiones que producen valores booleanos.")
        st.success("True\nTrue\nFalse")
    
        st.markdown("""
        | Operador | Significado |
        |---|---|
        | `and` | True si ambas condiciones son verdaderas |
        | `or` | True si al menos una condición es verdadera |
        | `not` | Invierte el valor lógico |
        """)

    st.info("""
        📝 **Nota**
    
        Los valores booleanos son `True` y `False`.
    
        - Los operadores comparativos comparan valores.
        - Los operadores de pertenencia verifican si un elemento está en una colección.
        - Los operadores lógicos combinan o niegan condiciones.
    
        Estos operadores son fundamentales para construir condiciones con
        `if`, `elif` y `else`.
        """)
    
    st.divider()

elif opciones == "Condicionales, bucles y funciones":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Condicionales, bucles y funciones</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.link_button(
            "📓 Colab - Clase 3",
            "https://colab.research.google.com/drive/1hdtjOicT18q5RPZj8tmK-OWtbBPw0e-e#scrollTo=yrj7KP2I7cx5",
            use_container_width=True
        )
    
    st.divider() ## Separador

    with st.container(border=True):

        st.markdown("### 1. Estructura selectiva `if`")
    
        st.markdown("**Ejecutar instrucciones si se cumple una condición**")
    
        st.code(
            'edad = 20\n'
            'if edad >= 18:\n'
            '    print("Eres mayor de edad")',
            language="python"
        )
    
        st.caption(
            "Evalúa una condición y ejecuta el bloque de instrucciones "
            "únicamente si el resultado es True."
        )
    
        st.success("Eres mayor de edad")
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `if` | Inicia la estructura condicional. |
        | `edad >= 18` | Condición que se evalúa. |
        | `:` | Indica el inicio del bloque de instrucciones. |
        | Indentación | Delimita las instrucciones que pertenecen al bloque. |
        """)
    
        st.info("""
        📝 **Nota**
    
        Si la condición es `False`, el bloque del `if` no se ejecuta.
        No es obligatorio utilizar `else`.
        """)
    
        st.divider()
    
        st.markdown("### 2. Estructura selectiva `if-else`")
    
        st.markdown("**Elegir entre dos alternativas**")
    
        st.code(
            'edad = 16\n'
            'if edad >= 18:\n'
            '    print("Eres mayor de edad")\n'
            'else:\n'
            '    print("Eres menor de edad")',
            language="python"
        )
    
        st.caption(
            "Evalúa una condición y selecciona uno de dos bloques: "
            "if cuando es True y else cuando es False."
        )
    
        st.success("Eres menor de edad")
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `if` | Comprueba la condición. |
        | `else` | Ejecuta el bloque alternativo si la condición es `False`. |
        """)
    
        st.info("""
        📝 **Nota**
    
        Los bloques `if` y `else` son excluyentes: en una misma ejecución,
        solo se ejecuta uno de ellos.
        """)
    
        st.divider()
    
        st.markdown("### 3. Estructura selectiva `if-elif-else`")
    
        st.markdown("**Evaluar varias condiciones alternativas**")
    
        st.code(
            'nota = 15\n'
            'if nota >= 18:\n'
            '    print("Excelente")\n'
            'elif nota >= 14:\n'
            '    print("Bueno")\n'
            'elif nota >= 11:\n'
            '    print("Aprobado")\n'
            'else:\n'
            '    print("Desaprobado")',
            language="python"
        )
    
        st.caption(
            "Permite comprobar varias condiciones en orden. "
            "Se ejecuta el primer bloque cuya condición sea verdadera."
        )
    
        st.success("Bueno")
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `if` | Evalúa la primera condición. |
        | `elif` | Comprueba otra condición si las anteriores son falsas. |
        | `else` | Ejecuta el bloque final si ninguna condición anterior se cumple. |
        """)
    
        st.info("""
        📝 **Nota**
    
        Puedes utilizar varios bloques `elif`, pero solo un `if` inicial
        y un `else` final opcional. El orden de las condiciones es importante.
        """)
    
        st.divider()
    
        st.markdown("### 4. Estructuras selectivas anidadas `if-if`")
    
        st.markdown("**Evaluar una condición dentro de otra estructura condicional**")
    
        st.code(
            'edad = 25\n'
            'tiene_entrada = True\n'
            '\n'
            'if edad >= 18:\n'
            '    print("Cumple la edad requerida")\n'
            '    if tiene_entrada:\n'
            '        print("Puede ingresar")',
            language="python"
        )
    
        st.caption(
            "Un segundo `if` se encuentra dentro del bloque de otro `if`. "
            "La segunda condición solo se evalúa si se ejecuta el bloque externo."
        )
    
        st.success(
            "Cumple la edad requerida\n"
            "Puede ingresar"
        )
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `if` externo | Comprueba la primera condición. |
        | `if` interno | Comprueba una segunda condición dentro del primer bloque. |
        | Indentación | Permite identificar la relación entre ambos bloques. |
        """)
    
        st.info("""
        📝 **Nota**
    
        La estructura `if-if` corresponde a una forma de condicionales anidados.
        Se pueden anidar varias estructuras `if` cuando una decisión depende
        de otra.
        """)
    
        st.divider()
    
        st.markdown("### 📌 Resumen de las estructuras selectivas")
    
        st.markdown("""
        | Estructura | Funcionamiento |
        |---|---|
        | `if` | Ejecuta instrucciones si se cumple una condición. |
        | `if-else` | Selecciona una de dos alternativas. |
        | `if-elif-else` | Selecciona entre varias alternativas. |
        | `if-if` | Evalúa una condición dentro de otra. |
        """)

    st.info("""
    💡 **Recuerda**

    - Las condiciones suelen utilizar operadores comparativos y lógicos.
    - La indentación define qué instrucciones pertenecen a cada bloque.
    - Los dos puntos (`:`) son obligatorios al finalizar la cabecera de
      cada estructura condicional.
    - Las estructuras selectivas permiten controlar el flujo de ejecución
      de un programa según las condiciones establecidas.
    """)

    st.divider()

    with st.container(border=True):

        st.markdown("## Bucle `for`")
    
        st.markdown("**Repetir instrucciones para cada elemento de una secuencia**")
    
        st.code(
            'lenguas = ["quechua", "aimara", "ashaninka"]\n'
            '\n'
            'for lengua in lenguas:\n'
            '    print(lengua)',
            language="python"
        )
    
        st.caption(
            "El bucle for recorre los elementos de una secuencia "
            "y ejecuta un bloque de instrucciones para cada uno."
        )
    
        st.success("quechua\naimara\nashaninka")
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `for` | Inicia el bucle. |
        | `lengua` | Variable que recibe cada elemento. |
        | `in` | Permite recorrer una secuencia. |
        | `lenguas` | Secuencia que se recorre. |
        | `:` | Indica el inicio del bloque. |
        | Indentación | Delimita las instrucciones que se repiten. |
        """)

        st.info("""
        📝 **Nota**
    
        El bucle `for` resulta útil cuando se desea recorrer una secuencia
        de elementos, como una lista, una cadena de texto o un rango numérico.
        """)
        
        st.markdown("### Bucle `for` con `range()`")
        
        st.markdown("**Repetir instrucciones utilizando una secuencia numérica**")
        
        st.code(
                'for numero in range(1, 6):\n'
                '    print(numero)',
                language="python"
            )
        st.caption(
                "La función range() genera una secuencia de números "
                "que permite controlar las iteraciones del bucle."
            )
        
        st.success("1\n2\n3\n4\n5")
        
        st.markdown("""
            | Forma | Funcionamiento |
            |---|---|
            | `range(fin)` | Genera números desde 0 hasta `fin - 1`. |
            | `range(inicio, fin)` | Genera números desde `inicio` hasta `fin - 1`. |
            | `range(inicio, fin, paso)` | Permite establecer el incremento o decremento. |
            """)     
        
        st.info("""
            💡 **Ejemplo**
        
            `range(1, 6)` genera los números del 1 al 5. El límite final,
            en este caso 6, no se incluye.
            """)      

    
        
        st.markdown("### Instrucciones de control: `break` y `continue`")
        
        st.markdown("**Modificar el comportamiento de las iteraciones**")
        
        st.code(
                '# Uso de break\n'
                'for numero in range(1, 6):\n'
                '    if numero == 3:\n'
                '        break\n'
                '    print(numero)\n'
                '\n'
                '# Uso de continue\n'
                'for numero in range(1, 6):\n'
                '    if numero == 3:\n'
                '        continue\n'
                '    print(numero)',
                language="python"
            )
        
        st.caption(
                "break termina inmediatamente el bucle; continue omite "
                "el resto de la iteración actual y pasa a la siguiente."
            )
        
        st.markdown("**Salida del ejemplo con `break`:**")
        st.success("1\n2")
        
        st.markdown("**Salida del ejemplo con `continue`:**")
        st.success("1\n2\n4\n5")
        
        st.markdown("""
            | Instrucción | Función |
            |---|---|
            | `break` | Finaliza el bucle inmediatamente. |
            | `continue` | Omite la iteración actual y continúa con la siguiente. |
            """)             
        
        st.divider()
    
        st.markdown("## Bucle `while`")
    
        st.markdown("**Repetir instrucciones mientras se cumpla una condición**")
    
        st.code(
            'contador = 1\n'
            '\n'
            'while contador <= 5:\n'
            '    print(contador)\n'
            '    contador += 1',
            language="python"
        )
    
        st.caption(
            "El bucle while evalúa una condición antes de cada iteración. "
            "Mientras sea verdadera, ejecuta el bloque de instrucciones."
        )
    
        st.success("1\n2\n3\n4\n5")
    
        st.markdown("""
        | Elemento | Función |
        |---|---|
        | `while` | Inicia el bucle condicional. |
        | `contador <= 5` | Condición que controla la repetición. |
        | `print(contador)` | Muestra el valor del contador. |
        | `contador += 1` | Incrementa el contador en una unidad. |
        """)
    
        st.info("""
        ⚠️ **Nota importante**
    
        Es necesario actualizar la variable que controla la condición
        cuando corresponda. Si la condición permanece verdadera
        indefinidamente, puede producirse un bucle infinito.
        """)
    
        st.divider()
    
        st.markdown("### Comparación entre `for` y `while`")
    
        st.markdown("""
        | Característica | `for` | `while` |
        |---|---|---|
        | Control | Recorre una secuencia o iterable. | Evalúa una condición. |
        | Uso habitual | Recorrer listas, cadenas o rangos. | Repetir mientras se cumpla una condición. |
        | Iteraciones | Dependen del iterable y del control del bucle. | Dependen de la condición y de las actualizaciones. |
        | Riesgo de bucle infinito | Posible en iterables o iteradores sin fin. | Posible si la condición nunca deja de cumplirse. |
        """)

        st.info("""
        📝 **Recuerda**
    
        Ambos bucles permiten repetir instrucciones. Elige `for` cuando
        necesites recorrer una secuencia y `while` cuando la repetición
        dependa de una condición.
        """)

else:
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Bibliotecas</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.link_button(
            "📓 Carpeta - Clase 4",
            "https://drive.google.com/drive/folders/14O0XSGtkBnW4d1DvtZzPEsg271JgO8EB?usp=drive_link",
            use_container_width=True
        )
    
    st.divider() ## Separador
