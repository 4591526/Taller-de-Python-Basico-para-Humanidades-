import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import random
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Pensamiento Computacional",
    page_icon="💻",
    layout="wide"
)

#st.title("Pensamiento Computacional")

st.sidebar.title("Pensamiento Computacional")

with st.sidebar:
    opciones = option_menu("Temas de clase: ",["Introducción","Mi primer código en Python", 
            "Variables", "Tipos de datos", "Operadores aritméticos", "Cadena de caracteres", "Listas", 
            "Expresiones booleanas", "Declaraciones condicionales", "Bucles", "Diccionarios", "Librerías", "Abrir archivos"] , 
        icons=['0-circle','1-circle', '2-circle', '3-circle', 'calculator', 'alphabet', 'list', '7-circle', '8-circle', '9-circle', 'braces', 
               'collection', 'file-earmark-arrow-up'], menu_icon="filetype-py", default_index=1)

if opciones == "Introducción":
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué es programar? 🤔</h2>', unsafe_allow_html=True)
    st.write("""
    Una forma sencilla de entender qué es programar es pensar en una receta de cocina. 
    Por ejemplo, para preparar pasta seguimos una secuencia de instrucciones: primero hervimos agua, luego agregamos la pasta,
    después esperamos aproximadamente diez minutos y finalmente colamos. 
    Esta secuencia ordenada de pasos para lograr un objetivo es lo que en programación se conoce como un algoritmo.
    
    Un algoritmo, por tanto, no es algo exclusivo de las computadoras, 
    sino una forma estructurada de resolver un problema mediante instrucciones claras y ordenadas.

    Programar implica desarrollar habilidades como:
    * Descomponer un problema grande en partes más pequeñas y manejables.
    * Establecer una secuencia lógica u ordenada de acciones.
    * Definir qué hacer según ciertas condiciones.
    * Identificar repeticiones o similitudes que permitan simplificar el problema.
    * Lograr que una tarea repetitiva pueda ejecutarse de forma automática.
    
    En este sentido, programar no solo consiste en escribir código, sino en aprender a pensar de manera estructurada para resolver problemas de forma 
    eficiente.
    """)

    st.write("")
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué NO es programar? ❌</h2>', unsafe_allow_html=True)
    st.write("""
    Existen muchas ideas equivocadas sobre lo que significa programar. 
    Programar no consiste en memorizar grandes cantidades de código ni en conocer fórmulas complejas. 
    Tampoco implica necesariamente ser bueno en matemáticas, ni saber muchos lenguajes de programación. 
    Del mismo modo, no es una actividad exclusiva de ingenieros ni requiere escribir instrucciones complicadas o incomprensibles.

    Más bien, programar es una habilidad que puede aprender cualquier persona interesada en resolver problemas de manera estructurada. 
    Se trata principalmente de organizar ideas, pensar con lógica y encontrar formas claras de dar instrucciones paso a paso para alcanzar un objetivo.
    """)

    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">¿Qué es Python? 💻</h2>', unsafe_allow_html=True)
    st.write("""
    Python es un lenguaje de programación que permite convertir ideas en instrucciones que una computadora puede ejecutar. 
    Fue creado por Guido van Rossum y presentado en 1991. 
    Se trata de un lenguaje de programación de alto nivel, diseñado para ser sencillo, claro y fácil de leer.

    Python puede considerarse como un puente entre el lenguaje humano y el lenguaje de las máquinas, 
    ya que su sintaxis se parece mucho al lenguaje natural. 
    Gracias a esta característica, su aprendizaje suele ser más accesible en comparación con otros lenguajes de programación, 
    especialmente para estudiantes que no provienen de áreas técnicas.
    
    Entre sus principales características destacan:
    * su sintaxis clara que permite comprender el código con relativa facilidad,
    * muchas de sus instrucciones se parecen a expresiones del inglés cotidiano,
    * Python es una herramienta muy utilizada en el análisis de datos y la investigación académica,
    * permite analizar textos, estudiar patrones lingüísticos y procesar lenguaje natural,
    * facilita el análisis de grandes volúmenes de información y la automatización de procesos de análisis.
    
    En este sentido, Python no solo es una herramienta técnica, sino también un recurso que permite a investigadores
    desarrollar nuevas formas de analizar información y resolver problemas mediante el pensamiento computacional.
    """)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Botón que abre el popup
        if st.button("Ver más sobre Python"):
            
            @st.dialog("Python")
            def show_info():
                
                col4, col5, col6 = st.columns([1,2,1])
    
                with col5:
                    st.image("https://upload.wikimedia.org/wikipedia/commons/6/66/Guido_van_Rossum_OSCON_2006.jpg", width=250)
                             
                    st.markdown("""
                    <p style="text-align:center; font-size:14px;">
                    Guido van Rossum <br>
                    Creador de Python
                    </p>
                    """, unsafe_allow_html=True)
        
                st.markdown("""
                🔗 Página oficial de [Python](https://www.python.org/)
                """)
        
            show_info()

    st.divider() ## Separador
    
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A"> Entornos de programación en Python ⌨</h2>', unsafe_allow_html=True)
    st.write("""
    Antes de escribir nuestro primer programa, es importante conocer algunos 
    entornos donde podemos escribir y ejecutar código Python. Cada uno tiene 
    ventajas según el tipo de trabajo que queramos realizar.
    """)

    # VS CODE
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E"> Visual Studio Code</h2>', unsafe_allow_html=True)

    st.write("""
    **Visual Studio Code (VS Code)** es un editor de código fuente gratuito y 
    multiplataforma desarrollado por Microsoft.
    """)
    st.markdown("""
    **Características principales:**
    - Es un programa ligero y rápido  
    - Permite instalar extensiones (Python, JavaScript, R, C++, etc.)  
    - Permite manejar carpetas y archivos fácilmente  
    - Integra una terminal  
    - Permite personalizar apariencia y atajos  
    - Integra GitHub para control de versiones  
    """)

    col7, col8, col9 = st.columns([1,2,1])
    with col8:
        # Botón que abre el popup
        if st.button("Ver más sobre VS Code"):
            
            @st.dialog("Visual Studio Code")
            def show_info():
                
                col10, col11, col12 = st.columns([1,2,1])
    
                with col11:
                    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9E5HZlsBUfIyQdZy53DBNd5c9aIxECWdFww&s", width=250)
        
                st.markdown("""
                🔗 Página oficial de [VS Code](https://code.visualstudio.com)
                """)
        
            show_info()

    st.write("")
    
    # COLAB Y JUPYTER
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Google Colab y Jupyter Notebook</h2>', unsafe_allow_html=True)
    
    st.write("""
    **Google Colaboratory (Colab)** y **Jupyter Notebook** son entornos 
    interactivos muy usados en ciencia de datos, investigación y educación.
    """)
    # Crear un diccionario con las características de Google Colab y Jupyter Notebook
    colab_vs_jupyter = {
        "Google Colaboratory (Colab)": {
            "Acceso": "Es accesible desde cualquier dispositivo con internet.",
            "Almacenamiento": "Se integra con Google Drive para guardar y cargar archivos a la nube.",
            "Recursos": "Proporciona GPU (tarjeta gráfica) y TPU (procesador) gratuitas con ciertas limitaciones.",
            "Instalación": "No requiere instalación, solo una cuenta de Google.",
            "Colaboración": "Permite compartir y editar notebooks en tiempo real.",
            "Restricciones": "Límites de tiempo de ejecución y desconexión automática."
        },
        "Jupyter Notebook": {
            "Acceso": "Se ejecuta en la computadora del usuario.",
            "Almacenamiento": "Los archivos se guardan en el sistema local.",
            "Recursos": "Depende del hardware del usuario.",
            "Instalación": "Requiere instalación con Anaconda o VSCode.",
            "Colaboración": "No tiene colaboración en tiempo real sin herramientas externas.",
            "Restricciones": "No tiene límite de tiempo de ejecución, depende del equipo."
        }
    }

    # Convertir a DataFrame
    df = pd.DataFrame(colab_vs_jupyter)

    # Mostrar en Streamlit
    st.dataframe(df)

    col13, col14, col15 = st.columns([1,2,1])
    with col14:
        # Botón que abre el popup
        if st.button("Ver más sobre Colab y Jupyter"):
            
            @st.dialog("Notebooks: Colab y Jupyter")
            def show_info():
                
                col16, col17, col18 = st.columns([1,2,1])
    
                with col17:
                    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvyuHWMd6UOi4d_oVuHTBZsGvS7kG6TFK2yQ&s", width=250)
                    st.image("https://images.seeklogo.com/logo-png/35/1/jupyter-logo-png_seeklogo-354673.png", width=250)
        
                st.markdown("""
                🔗 Dónde descargar [Colab](https://workspace.google.com/marketplace/app/colaboratory/1014160490159?hl=es)
                
                🔗 Página oficial de [Jupyter](https://jupyter.org)
                """)
            show_info()
            
    st.write("")
    
    # VIDEO
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Video: Google Colab y Jupyter Notebook</h2>', unsafe_allow_html=True)
    col19, col20, col21 = st.columns([1,1.5,1])
    with col20:
    # Insertar un video explicativo de los entornos: VSC y Jupyter
        st.video("https://www.youtube.com/watch?v=IVMNhciviwc")

elif opciones == "Mi primer código en Python":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; color: #4E4E8A">Mi primer código en Python</h2>', unsafe_allow_html=True)
    
    st.divider() ## Separador
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">¿Dónde programamos?</h2>', unsafe_allow_html=True)
    st.write("""
    Podemos usar Python en:
    
    **Notebooks (Colab, Jupyter):**
    - El archivo completo se guarda como .ipynb
    - La estructura del archivo presenta dos tipos de celdas: texto y código
    - Ejecutamos por celdas de código
    - El resultado se observa debajo de la celda código
    
    **VS Code:**
    - Ejecutamos el archivo completo (.py)
    - La estructura del archivo solo presenta líneas de código donde se puede explicar el proceso a través del formato de comentarios (#)
    - El resultado se observa en la terminal
    """)
    st.divider() ## Separador
    
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
            
if opciones == "Variables":
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; color: #4E4E8A">🧩 Variables en Python</h2>', unsafe_allow_html=True)
    # Explicación
    st.write("""
    En Python, una **variable** es un espacio donde almacenamos información (un valor) para poder usarla después en nuestro programa.
    Para asignar un valor a una variable utilizamos el símbolo `=`:
    `numero = 14`
    En este caso, la variable `numero` guarda el valor `14`.

    ### 📌 Reglas para nombrar variables
    - Pueden contener letras, números y guiones bajos (`_`).  
    - **No pueden comenzar con un número**.  
    - **No pueden tener espacios**.  
    - No deben usar **caracteres especiales** (como `@`, `#`, `!`, etc.).  
    - No pueden ser **palabras reservadas de Python** (como `if`, `for`, `while`, etc.).  

    Puedes revisar la lista completa aquí: [Palabras reservadas en Python](https://www.w3schools.com/python/python_ref_keywords.asp)
    """, unsafe_allow_html=True)

    # Ejemplos de creación de variables
    st.markdown(f'<h3 style="font-size: 28px; text-align: center; color: #4E8A4E">Ejemplos de variables</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    Explora cómo funcionan las variables en Python. Puedes escribir valores y ver cómo cambian.
    """)
    
    # Input interactivo
    nombre_variable = st.text_input("Escribe un nombre para tu variable:", value="animal")
    valor_variable = st.text_input("Asigna un valor a tu variable:", value="perro")
    
    # Mostrar resultado dinámico
    if nombre_variable:
        st.markdown("### Resultado")
        st.code(f"{nombre_variable} = '{valor_variable}'\nprint({nombre_variable})", language="python")
        st.write("Salida:")
        st.write(valor_variable)
    
    st.markdown("---")
    
    # Explicación de reasignación
    st.markdown("### 🔁 Reasignación de variables")
    
    valor1 = st.text_input("Primer valor de la variable:", value="guau", key="v1")
    valor2 = st.text_input("Nuevo valor de la variable:", value="sonido del perro", key="v2")
    
    st.code(f"""
    perro = "{valor1}"
    print(perro)
    
    perro = "{valor2}"
    print(perro)
    """, language="python")
    
    st.write("Salida:")
    st.write(valor1)
    st.write(valor2)
    
    st.markdown("""
    💡 **Observa:** la variable guarda siempre el **último valor asignado**.
    """)
    
    st.markdown("---")
    
    # Simulación de error
    st.markdown("### ⚠️ Error común")
    
    st.markdown("""
    Si intentas usar una variable que no ha sido definida, obtendrás un error:
    """)
    
    st.code("""
    print(gato)
    """, language="python")
    
    st.error("NameError: name 'gato' is not defined")
    
    st.markdown("""
    💡 **Recuerda:** primero debes crear la variable antes de usarla.
    """)
    
    # VIDEO
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; color: #4E8A4E">Video: Variables </h2>', unsafe_allow_html=True)
    col25, col26, col27 = st.columns([1,1.5,1])
    with col26:
    # Insertar un video explicativo
        st.video("https://youtu.be/wDqPp41z90E")

if opciones == "Tipos de datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Tipos de datos en Python</h2>', unsafe_allow_html=True)

        # Crear el gráfico
    data_types_graph = graphviz.Digraph('data_types')

        # Configuración global
    data_types_graph.attr(rankdir='TB', fontsize='12')
    data_types_graph.attr('node', fontname="Arial", fontsize='12', shape='box', style='filled', fillcolor='lightgray')
    data_types_graph.attr('edge', color='gray')

        # Definir nodos con colores diferenciados
    data_types_graph.node('Texto', label='Texto', color='firebrick2')
    data_types_graph.node('Números', label='Números', color='purple')
    data_types_graph.node('Booleanos', label='Boolean\n(bool)\n booleanos', color='deeppink')

    data_types_graph.node('String', label='String \n(str)\n cadena de caracteres', color='crimson')
    data_types_graph.node('Int', label='Interger\n(int)\n número entero', color='blue')
    data_types_graph.node('Float', label='Float\n(float)\n número decimal', color='blue')

    data_types_graph.node('True', label='True', color='coral')
    data_types_graph.node('False', label='False', color='coral')

    data_types_graph.node('cadena1', label='"¡Hola Mundo!"', color='red')
    data_types_graph.node('cadena2', label='"2025"', color='red')
    data_types_graph.node('cadena3', label='"@gmail.com"', color='red')

    data_types_graph.node('entero', label='7', color='cyan')
    data_types_graph.node('decimal', label='3.14', color='darkolivegreen1')
        # Define edges
    data_types_graph.edge('Texto', 'String')
    data_types_graph.edge('Números', 'Int')
    data_types_graph.edge('Números', 'Float')
    data_types_graph.edge('Booleanos', 'True')
    data_types_graph.edge('Booleanos', 'False')

    data_types_graph.edge('String', 'cadena1')
    data_types_graph.edge('String', 'cadena2')
    data_types_graph.edge('String', 'cadena3')

    data_types_graph.edge('Int', 'entero')
    data_types_graph.edge('Float', 'decimal')

        # Mostrar en Streamlit
    st.graphviz_chart(data_types_graph)

    # Breve explicación de los tipos de datos
    st.markdown("""
    <h3>📌 Tipos de datos básicos</h3>

    <ul>
        <li><b>String (str)</b>: Cadenas de caracteres que contienen letras, números o símbolos. 
        Ejemplo: <code>"Hola"</code>. Solo los caracteres numéricos pueden convertirse a <code>int</code> o <code>float</code>.</li>
        <li><b>Integer (int)</b>: Números enteros, como <code>7</code> o <code>-3</code>. 
        Pueden convertirse a <code>float</code>.</li>
        <li><b>Float (float)</b>: Números decimales, como <code>3.14</code> o <code>-0.5</code>. 
        Pueden convertirse a <code>int</code>, pero <b>se pierde la parte decimal</b>.</li>
        <li><b>Boolean (bool)</b>: Valores de verdad: <code>True</code> o <code>False</code>. 
        Se usan en condiciones y comparaciones.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Parte interactiva simple
    st.markdown("### ⚙️ Prueba tú mismo")

    valor = st.text_input("Escribe un valor (ejemplo: 10, 3.5, 'Hola', True):")

    if valor:
        try:
            evaluado = eval(valor)
            st.success(f"Tipo de dato: {type(evaluado)}")
            st.write("Valor interpretado:", evaluado)
        except:
            st.warning("No se pudo interpretar automáticamente. Se considera texto.")
            st.write("Tipo de dato:", type(valor))
            st.write("Valor:", valor)

if opciones == "Operadores aritméticos":
    st.markdown('<h2 style="font-size: 42px; text-align: center;">🧮 Operadores aritméticos en Python</h2>', unsafe_allow_html=True)

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

    # Parte interactiva
    st.markdown("### ⚙️ Prueba tú mismo")

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

if opciones == "Cadena de caracteres":
    st.markdown('<h2 style="font-size: 42px; text-align: center;">🔤 Cadena de caracteres (str)</h2>', unsafe_allow_html=True)

    # Explicación breve
    st.markdown("""
    Una <b>cadena de caracteres</b> (<code>str</code>) es un tipo de dato que permite almacenar texto.
    Puede incluir letras, números y símbolos, y se define usando comillas simples (<code>' '</code>) o dobles (<code>" "</code>).
    """, unsafe_allow_html=True)

    # Ejemplo básico
    st.code("""texto = "El 22 de febrero se nos anunció que regresaríamos a Colombia."
    print(texto)""", language='python')

    st.markdown("---")

    # Métodos de strings
    st.markdown('<h3 style="font-size: 30px; text-align: center;">🛠️ Métodos de cadenas de caracteres</h3>', unsafe_allow_html=True)

    codigo_3 = """
    # Definición de una cadena
    texto = "El 22 de febrero se nos anunció que regresaríamos a Colombia."
    print("Texto original:", texto)
    
    # Mayúsculas y minúsculas
    print("Mayúsculas:", texto.upper())
    print("Minúsculas:", texto.lower())
    
    # Longitud del texto
    print("Cantidad de caracteres:", len(texto))
    
    # Contar palabras o caracteres
    print("Veces que aparece 'Colombia':", texto.count("Colombia"))
    
    # Reemplazar texto
    print("Reemplazo:", texto.replace("Colombia", "Perú"))
    
    # Convertir a lista
    print("Lista de palabras:", texto.split())
    
    # Verificaciones
    print("¿Empieza con 'El'?", texto.startswith("El"))
    print("¿Termina con 'Colombia.'?", texto.endswith("Colombia."))
    """
    st.code(codigo_3, language='python')

    st.markdown("---")

    # Parte interactiva
    st.markdown("### ⚙️ Prueba tú mismo")

    texto_usuario = st.text_area("Escribe un texto:")

    if texto_usuario:
        st.write("🔍 Resultados:")
        st.write("Mayúsculas:", texto_usuario.upper())
        st.write("Minúsculas:", texto_usuario.lower())
        st.write("Cantidad de caracteres:", len(texto_usuario))

        reemplazo = st.text_input("Reemplazar palabra (formato: original,nuevo):", key="reemplazo")
        if reemplazo and "," in reemplazo:
            original, nuevo = reemplazo.split(",", 1)
            st.write("Texto reemplazado:", texto_usuario.replace(original.strip(), nuevo.strip()))
        
if opciones == "Listas":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Listas (list)</h2>', unsafe_allow_html=True)

    # Ejemplo básico
    st.code("""comunicaciones = ["comunicación audiovisual", "periodismo", "comunicación para el desarrollo", "publicidad"]
    print(comunicaciones)""", language='python')
    
    # Explicación
    st.markdown("""
    Las **listas** son estructuras de datos que permiten almacenar múltiples elementos en una sola variable.
    
    - Se definen con corchetes: `[]`  
    - Los elementos se separan por comas  
    - Pueden contener distintos tipos de datos (números, texto, incluso otras listas)  
    - Son **mutables**, es decir, se pueden modificar después de su creación  
    """)
    
    # Métodos
    st.markdown('<h3 style="font-size: 30px; text-align: center;">🛠️ Métodos y operaciones con listas</h3>', unsafe_allow_html=True)

    codigo_4 = """
    # Definición de una lista
    frutas = ["manzana", "banana", "naranja", "uva"]
    
    # Acceder a elementos
    print("Primera fruta:", frutas[0])
    print("Última fruta:", frutas[-1])
    
    # Modificar un elemento
    frutas[1] = "pera"
    print("Lista modificada:", frutas)
    
    # Índice de un elemento
    print("Índice de 'naranja':", frutas.index("naranja"))
    
    # Agregar elementos
    frutas.append("mango")
    print("Después de agregar:", frutas)
    
    # Eliminar elementos
    frutas.remove("naranja")
    print("Después de eliminar:", frutas)
    
    # Ordenar lista
    numeros = [5, 2, 9, 1, 7]
    numeros.sort()
    print("Ordenada:", numeros)
    
    numeros.sort(reverse=True)
    print("Orden inverso:", numeros)
    
    # Longitud
    print("Cantidad de elementos:", len(frutas))
    """
    st.code(codigo_4, language='python')
    
    st.markdown("---")
    
    # Parte interactiva
    st.markdown("### ⚙️ Prueba tú mismo")
    
    lista_usuario = st.text_input("Escribe elementos separados por comas:", value="manzana, banana, naranja")
    
    if lista_usuario:
        lista = [x.strip() for x in lista_usuario.split(",")]
    
        st.write("📋 Lista:", lista)
        st.write("🔢 Cantidad de elementos:", len(lista))
    
        if lista:
            st.write("👉 Primer elemento:", lista[0])
            st.write("👉 Último elemento:", lista[-1])
    
        nuevo = st.text_input("Elemento para agregar:", key="agregar")
        if nuevo:
            lista.append(nuevo)
            st.write("➕ Lista actualizada:", lista)
    
        eliminar = st.text_input("Elemento para eliminar:", key="eliminar")
        if eliminar and eliminar in lista:
            lista.remove(eliminar)
            st.write("➖ Lista actualizada:", lista)
    
    st.markdown("""
    💡 **Observa:** las listas son **mutables**, por lo que pueden cambiar durante la ejecución del programa.
    """)


if opciones == "Expresiones booleanas":
    st.markdown('<h2 style="font-size: 42px; text-align: center;">⚖️ Expresiones booleanas en Python</h2>', unsafe_allow_html=True)

    # Explicación
    st.markdown("""
    Las **expresiones booleanas** son aquellas que solo pueden tener dos valores:  
    <b>True</b> (verdadero) o <b>False</b> (falso).
    
    Se utilizan principalmente en **condiciones y comparaciones** para tomar decisiones en un programa.
    
    En Python, estas expresiones se construyen usando:
    - Operadores **comparativos**
    - Operadores de **pertenencia**
    - Operadores **lógicos**
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 🔹 Operadores comparativos
    st.markdown('<h3 style="text-align: center;">🔍 Operadores comparativos</h3>', unsafe_allow_html=True)
    
    operadores_comparativos = {
        "Operador": ["==", "!=", ">", "<", ">=", "<="],
        "Descripción": [
            "Igual a",
            "Distinto de",
            "Mayor que",
            "Menor que",
            "Mayor o igual que",
            "Menor o igual que"
        ],
        "Ejemplo": [
            "5 == 5 → True",
            "5 != 3 → True",
            "7 > 3 → True",
            "3 < 7 → True",
            "3 >= 5 → False",
            "3 <= 5 → True"
        ]
    }
    
    st.dataframe(pd.DataFrame(operadores_comparativos), use_container_width=True)
    
    st.markdown("---")
    
    # 🔹 Operadores de pertenencia
    st.markdown('<h3 style="text-align: center;">📦 Operadores de pertenencia</h3>', unsafe_allow_html=True)
    
    operadores_pertenencia = {
        "Operador": ["in", "not in"],
        "Descripción": [
            "Verifica si un elemento está dentro de una secuencia",
            "Verifica si un elemento no está dentro de una secuencia"
        ],
        "Ejemplo": [
            "'a' in 'manzana' → True",
            "'b' not in 'manzana' → True"
        ]
    }
    
    st.dataframe(pd.DataFrame(operadores_pertenencia), use_container_width=True)
    
    st.markdown("---")
    
    # 🔹 Operadores lógicos
    st.markdown('<h3 style="text-align: center;">🧠 Operadores lógicos</h3>', unsafe_allow_html=True)
    
    operadores_logicos = {
        "Operador": ["and", "or", "not"],
        "Descripción": [
            "True si ambas condiciones son verdaderas",
            "True si al menos una condición es verdadera",
            "Invierte el valor lógico"
        ],
        "Ejemplo": [
            "(5 > 3) and (7 > 5) → True",
            "(5 > 3) or (7 < 5) → True",
            "not (5 > 3) → False"
        ]
    }
    
    st.dataframe(pd.DataFrame(operadores_logicos), use_container_width=True)
    
    st.markdown("---")
    
    # 🔹 Mini interacción
    st.markdown("### ⚙️ Prueba tú mismo")
    
    a = st.number_input("Valor de a:", value=5)
    b = st.number_input("Valor de b:", value=3)
    
    st.write("a > b:", a > b)
    st.write("a == b:", a == b)
    st.write("a < b:", a < b)
    st.write("(a > b) and (b > 0):", (a > b) and (b > 0))

if opciones == "Declaraciones condicionales":
    st.markdown(f'<h2 style="font-size: 40px; text-align: center; ">Declaraciones condicionales: if-elif-else</h2>', unsafe_allow_html=True)

    # Breve explicación de las declaraciones condicionales
    st.write("""
            Las declaraciones condicionales permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.
            En Python, se utilizan las palabras clave `if`, `elif` y `else` para crear estas estructuras de control.
            """, unsafe_allow_html=True)
    
    st.markdown(f'<h3 style="font-size: 38px; text-align: center; ">Estructura básica</h3>', unsafe_allow_html=True)
    # Crear tablas de cada tipo de operadores
    estructura_basica = {
                "Palabra clave": ["if", "elif", "else"],
                "Descripción": [
                    "Evalúa una condición y ejecuta el bloque de código si es verdadera",
                    "Evalúa una condición alternativa si la anterior es falsa",
                    "Ejecuta el bloque de código si todas las condiciones anteriores son falsas"
                ],        
                "Ejemplo": [
                    "if x > 5:",
                    "elif x == 5:",
                    "else:"
                ]
        }
        
        # Convertir a DataFrame
    df_estructura_basica = pd.DataFrame(estructura_basica)
            
        # Mostrar en Streamlit     
    st.dataframe(df_estructura_basica)

    # Ejemplo de declaración condicional
    st.markdown(f'<h3 style="font-size: 38px; text-align: center; ">Ejemplo de declaración condicional</h3>', unsafe_allow_html=True)
        # Código de ejemplo
    codigo_7 = """
    # Definición de una variable
    edad = 18

    # Declaración condicional
    if edad < 18:
        print("Eres menor de edad.")
    elif edad == 18:
        print("Tienes 18 años.")
    else:
        print("Eres mayor de edad.")
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_7, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una variable llamada `edad`.
    - Se utiliza una declaración condicional para verificar si la edad es menor, igual o mayor a 18.
    - Dependiendo del resultado, se imprime un mensaje diferente.
    """)

    st.markdown('<h2 style="font-size: 42px; text-align: center;">🎮 Juego: Piedra, Papel o Tijera</h2>', unsafe_allow_html=True)

    st.markdown("""
    Elige una opción y juega contra la computadora.  
    Este juego utiliza **condicionales**, **expresiones booleanas** y **aleatoriedad**.
    """)

    # Opciones del juego
    opciones_juego = ["Piedra", "Papel", "Tijera"]

    eleccion_usuario = st.selectbox("Elige tu jugada:", opciones_juego)

    if st.button("Jugar"):
        eleccion_pc = random.choice(opciones_juego)

        st.write(f"🧑 Tú elegiste: **{eleccion_usuario}**")
        st.write(f"💻 Computadora eligió: **{eleccion_pc}**")

        # Lógica del juego
        if eleccion_usuario == eleccion_pc:
            st.info("🤝 ¡Empate!")
        elif (
            (eleccion_usuario == "Piedra" and eleccion_pc == "Tijera") or
            (eleccion_usuario == "Papel" and eleccion_pc == "Piedra") or
            (eleccion_usuario == "Tijera" and eleccion_pc == "Papel")
        ):
            st.success("🎉 ¡Ganaste!")
        else:
            st.error("😢 Perdiste")

        st.markdown("---")
    
        # Explicación didáctica
        st.markdown("""
        💡 **¿Qué estamos usando aquí?**
        - `random.choice()` para generar una elección aleatoria  
        - Condicionales `if-elif-else`  
        - Expresiones booleanas para determinar el ganador  
        """)
        
if opciones == "Bucles":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Bucles for y while</h2>', unsafe_allow_html=True)

    # Breve explicación de los bucles
    st.write("""
            Los bucles permiten ejecutar un bloque de código varias veces. 
            En Python, los bucles más comunes son `for` y `while`. 
            El bucle `for` se utiliza para iterar sobre una secuencia (como una lista o una cadena), 
            mientras que el bucle `while` se ejecuta mientras una condición sea verdadera.
            """, unsafe_allow_html=True)
    
    # Una tabla con la estructura básica de los bucles
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Estructura básica</h3>', unsafe_allow_html=True)

    # Crear tablas de cada tipo de operadores
    estructura_bucle = {
                "Palabra clave": ["for", "while"],
                "Descripción": [
                    "Itera sobre una secuencia (lista, cadena, etc.)",
                    "Ejecuta el bloque de código mientras la condición sea verdadera"
                ],        
                "Ejemplo": [
                    "for i in range(5):",
                    "while i < 5:"
                ]
        }
        
        # Convertir a DataFrame
    df_estructura_bucle = pd.DataFrame(estructura_bucle)
    
    # Mostrar en Streamlit
    st.dataframe(df_estructura_bucle)

    # Ejemplo de bucle for
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de bucle for</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_8 = """
    # Definición de una lista
    frutas = ["manzana", "banana", "naranja"]

    # Bucle for
    for fruta in frutas:
        print("Fruta:", fruta)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_8, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una lista llamada `frutas`.
    - Se utiliza un bucle `for` para iterar sobre cada elemento de la lista.
    - En cada iteración, se imprime el nombre de la fruta.
    """)

    # Ejemplo de bucle while
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de bucle while</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_9 = """
    # Definición de una variable
    contador = 0

    # Bucle while
    while contador < 5:
        print("Contador:", contador)
        contador += 1  # Incrementa el contador en 1
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_9, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se define una variable llamada `contador`.
    - Se utiliza un bucle `while` para imprimir el valor del contador mientras sea menor que 5.
    - En cada iteración, se incrementa el contador en 1.
    """)

    # Funciones de control de bucles: break y continue
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Funciones de control de bucles</h3>', unsafe_allow_html=True)
    st.write("""
    Las funciones `break` y `continue` se utilizan para controlar el flujo de los bucles:
    - `break`: Termina el bucle inmediatamente.
    - `continue`: Salta a la siguiente iteración del bucle.
    """, unsafe_allow_html=True)

    # Ejemplo de uso de break y continue
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de uso de break y continue</h3>', unsafe_allow_html=True)
    # Código de ejemplo
    codigo_10 = """
    # Bucle for con break y continue
    for i in range(10):
        if i == 5:
            print("Se encontró el número 5, saliendo del bucle.")
            break  # Termina el bucle si i es igual a 5
        if i % 2 == 0:
            print("Número par:", i)
        else:
            print("Número impar:", i)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_10, language='python')
    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se utiliza un bucle `for` para iterar sobre los números del 0 al 9.
    - Si el número es igual a 5, se imprime un mensaje y se utiliza `break` para salir del bucle.
    - Si el número es par, se imprime un mensaje indicando que es par.
    - Si el número es impar, se imprime un mensaje indicando que es impar.
    """)

if opciones == "Diccionarios":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Diccionarios de Python</h2>', unsafe_allow_html=True) 

    # Breve explicación de los diccionarios
    st.write("""
    Los diccionarios son estructuras de datos que almacenan pares clave-valor.
    Se definen utilizando llaves `{}` y cada par se separa por comas.
    Los diccionarios son útiles para almacenar datos relacionados y acceder a ellos de manera eficiente.
    """, unsafe_allow_html=True)

    # Ejemplo de diccionario en formato código
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de diccionario</h3>', unsafe_allow_html=True)
    codigo_11 = """
    # Definición de un diccionario
    estudiante = {
        "nombre": "Liam",
        "apellido": "Payne",
        "edad": 25,
        "cursos": ["Python", "Java", "C++"]
    }
    # Acceder a valores del diccionario
    print("Nombre:", estudiante["nombre"])
    print("Apellido:", estudiante["apellido"])
    print("Edad:", estudiante["edad"])
    print("Cursos:", estudiante["cursos"])

    # Modificar un valor del diccionario
    estudiante["edad"] = 26
    print("Edad modificada:", estudiante["edad"])

    # Agregar un nuevo par clave-valor
    estudiante["universidad"] = "PUCP"
    print("Universidad:", estudiante["universidad"])

    # Verificar si una clave existe en el diccionario
    existe_nombre = "nombre" in estudiante
    print("¿Existe la clave 'nombre'?:", existe_nombre)

    # Obtener todas las claves del diccionario
    claves = estudiante.keys()
    print("Claves del diccionario:", claves)

    # Obtener todos los valores del diccionario
    valores = estudiante.values()
    print("Valores del diccionario:", valores)

    
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_11, language='python')
    
    

if opciones == "Librerías":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Librerías de Python</h2>', unsafe_allow_html=True)

    # Breve explicación de las funciones
    st.write(""" 
    Librerías son colecciones de funciones y métodos que permiten realizar tareas específicas sin necesidad de escribir el código desde cero.
    En Python, existen muchas librerías predefinidas que puedes importar y utilizar en tu código.
    Algunas de las librerías más comunes son `pandas`, `random`, entre otras.
    """, unsafe_allow_html=True)

    # La librería random
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Librería random</h3>', unsafe_allow_html=True)
    st.write("""
    La librería `random` se utiliza para generar números aleatorios y realizar selecciones aleatorias.
    Puedes usarla para crear juegos, simulaciones y más.
    """, unsafe_allow_html=True)

    # Código de ejemplo
    codigo_10 = """
    # Importar la librería random
    import random

    # Generar un número aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1, 10)
    print("Número aleatorio:", numero_aleatorio)

    # Elegir un elemento aleatorio de una lista
    lista = ["manzana", "banana", "naranja"]
    fruta_aleatoria = random.choice(lista)
    print("Fruta aleatoria:", fruta_aleatoria)

    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_10, language='python')


    # Uso de range()
    st.write("""
    La función `range()` se utiliza para generar una secuencia de números.
    Puedes especificar el inicio, el final y el paso de la secuencia.
    Por ejemplo, `range(1, 10, 2)` generará la secuencia `1, 3, 5, 7, 9`.
    """, unsafe_allow_html=True)

    # La librería nklt
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Librería nltk</h3>', unsafe_allow_html=True)
    st.write("""
    La librería `nltk` (Natural Language Toolkit) se utiliza para el procesamiento de lenguaje natural.
    Proporciona herramientas para trabajar con texto, como tokenización, análisis de sentimientos y más.
    """, unsafe_allow_html=True)

    ## Código de ejemplo
    codigo_11 = """
    # Importar la librería nltk
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stopwords_es = stopwords.words('spanish')

    texto = "Domingo 14 de junio de 1942
    EL VIERNES DESPERTE ya a las seis. Era comprensible, pues
    fue el día de mi cumpleaños. Pero no podía levantarme tan
    temprano y hube de apaciguar mi curiosidad hasta un cuarto para
    las siete. Entonces ya no soporté más y corrí hasta el comedor,
    donde nuestro pequeño gatito, Mohrchen, me saludó con efusivo
    cariño. Después de las siete fui al dormitorio de mis padres y,
    enseguida, con ellos al salón para encontrar y desenvolver mis
    regalos. A ti, mi diario, te vi en primer lugar, y sin duda fuiste mi
    mejor regalo. También me obsequiaron un ramo de rosas, un
    cactus y unas ramas de rosas silvestres. Fueron los primeros saludos
    del día, ya que más tarde habría bastante más. Papá y mamá me entregaron 
    numerosos regalos y mis amigos tampoco se quedaron
    atrás en materia de mimarme. Entre otras cosas me regalaron un
    libro titulado, «Cámara Oscura», un juego de mesa, muchas
    golosinas, un rompecabezas, un broche, las «Sagas y Leyendas de
    Holanda» de Joseph Cohen, otro libro encantador, «Las
    Vacaciones de Daisy en la Montaña» y algún dinero. Con éste me
    compré las leyendas mitológicas griegas y romanas. ¡Fantástico!
    Enseguida vino Lies y partimos juntas a la escuela. Comencé
    siguiendo el ritual holandés de obsequiar golosinas a mis maestros
    y compañeros de clase y luego nos pusimos a trabajar."

    texto_minusculas = texto.lower()
    texto_depurado = texto_minusculas.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("¿", "").replace("¡", "").replace("!", "").replace("?", "").replace("«", "").replace("»", "").replace("/n", "").replace("-", "").replace("_", "")
    lista_palabras = texto_depurado.split()

    lista_depurada = list()
    for palabra in lista_palabras:
        if palabra not in stopwords_es:
            lista_depurada.append(palabra)
    
    print(len(cantidad_palabras))
    print(len(lista_depurada))        
    """ 
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_11, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se importa la librería `nltk` y se descargan las stopwords en español.
    - Se define un texto en español.
    - Se convierte el texto a minúsculas y se eliminan los signos de puntuación.
    - Se genera una lista de palabras y se eliminan las stopwords.
    - Se imprime la cantidad de palabras originales y la cantidad de palabras depuradas.
    """)


if opciones == "Abrir archivos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Abrir archivos en Colab</h2>', unsafe_allow_html=True)

    # Breve explicación de cómo abrir archivos
    st.write("""
    En Google Colab, puedes abrir archivos de diferentes maneras.
    Puedes cargar archivos desde tu computadora e importar archivos desde Google Drive.
    """, unsafe_allow_html=True)

    # Ejemplo de cómo abrir archivos
    st.markdown(f'<h3 style="font-size: 42px; text-align: center; ">Ejemplo de cómo abrir archivos</h3>', unsafe_allow_html=True)

    # Código de ejemplo
    codigo_12 = """
    # Importar la librería necesaria
    from google.colab import files
    # Importar archivos desde tu computadora
    uploaded = files.upload()
    # Mostrar el nombre del archivo subido
    with open("nombre_archivo.txt", "r") as file:
        texto = file.read()
    print(texto)
    """
    # Mostrar el código en un bloque con resaltado de sintaxis
    st.code(codigo_12, language='python')

    # Explicación del ejemplo
    st.write("""
    En este ejemplo:
    - Se importa la librería `files` de Google Colab.
    - Se utiliza la función `files.upload()` para cargar un archivo desde tu computadora.
    - Se abre el archivo y se lee su contenido.
    - Se imprime el contenido del archivo.
    """)

st.markdown(""" 
<hr style="margin-top:40px; margin-bottom:20px;"> 
<div style=" text-align:center; font-size:18px; color:#555; padding-bottom:20px; "> 
<p><b>Luisa Gomez</b></p> 
📩 luisa.gomez@pucp.edu.pe </br>
💻 GitHub <a href="https://github.com/4591526/" target="_blank" style="text-decoration:none; font-weight:600;"> 
4591526 </a> </div> """, unsafe_allow_html=True)

    
    


   
   
   







