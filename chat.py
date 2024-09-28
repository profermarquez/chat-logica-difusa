from fuzzywuzzy import fuzz
import numpy as np

# Tabla de preguntas y respuestas
qa_table = [
    {"pregunta": "¿Qué es una CPU?", "respuesta": "La CPU es el cerebro de la computadora."},
    {"pregunta": "¿Qué es una GPU?", "respuesta": "La GPU maneja gráficos y procesamiento paralelo."},
    {"pregunta": "¿Qué es la memoria RAM?", "respuesta": "La RAM es la memoria de corto plazo del sistema."},
    {"pregunta": "¿Qué es la computadora", "respuesta": "La computadora se refiere a todos los componentes de Hardware unidos."},
    {"pregunta": "¿Qué es un disco duro?", "respuesta": "Un disco duro almacena permanentemente los datos."}
]

# Función para calcular la similitud difusa
def calcular_similitud_difusa(entrada_usuario, pregunta):
    # Usamos fuzzy ratio para obtener una similitud en porcentaje
    return fuzz.ratio(entrada_usuario.lower(), pregunta.lower())

# Función difusa para obtener la respuesta más adecuada
def obtener_mejor_respuesta(entrada_usuario, qa_table):
    mejores_puntuaciones = []
    
    for qa in qa_table:
        similitud = calcular_similitud_difusa(entrada_usuario, qa["pregunta"])
        mejores_puntuaciones.append(similitud)
    
    # Obtenemos la mejor coincidencia (la de mayor similitud)
    indice_mejor_respuesta = np.argmax(mejores_puntuaciones)
    
    # Umbrales para respuestas difusas
    if mejores_puntuaciones[indice_mejor_respuesta] > 80:  # Muy similar
        respuesta = qa_table[indice_mejor_respuesta]["respuesta"]
    elif 50 < mejores_puntuaciones[indice_mejor_respuesta] <= 80:  # Algo similar
        respuesta = f"No estoy seguro, pero creo que te refieres a: {qa_table[indice_mejor_respuesta]['respuesta']}"
    else:  # Poca similitud
        respuesta = "Lo siento, no tengo una respuesta exacta para eso."

    return respuesta

# Ejemplo de interacción con el usuario
def iniciar_chat():
    print("Chatbot: Hola, soy tu asistente. Hazme una pregunta sobre componentes de la computadora.")
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() in ["salir", "adios", "chau"]:
            print("Chatbot: ¡Adiós!")
            break
        
        respuesta = obtener_mejor_respuesta(entrada_usuario, qa_table)
        print(f"Chatbot: {respuesta}")

# Iniciar el chat
iniciar_chat()
