import ollama

def adaptar_limite(pregunta: str, modelo: str) -> str:
    """ 
    Proceso de Inferencia Puro: Define si la pregunta requiere un 
    contexto acotado (CORTA) o un contexto amplio/abierto (LARGA).
    """

    prompt_sistema = (
        "Eres un clasificador binario estricto. Analizas preguntas históricas.\n"
        "Tu tarea es evaluar si la pregunta del usuario es una consulta ESPECÍFICA de un solo dato "
        "o si es una pregunta ABIERTA/COMPLEJA que requiere múltiples datos para responder.\n\n"
        
        "REGLAS:\n"
        "- Responde ÚNICAMENTE con la palabra 'CORTA' si pide un dato único, un evento puntual o una confirmación.\n"
        "- Responde ÚNICAMENTE con la palabra 'LARGA' si pide resumir procesos, causas, consecuencias, listar múltiples eventos o preguntas generales de tipo '¿qué pasó en X período?'.\n"
        "- Está terminantemente prohibido agregar puntuación, explicaciones o justificaciones.\n\n"
        
        "EJEMPLOS DE COMPORTAMIENTO:\n"
        "User: ¿Quién asumió la presidencia de Argentina en 1983?\n"
        "Assistant: CORTA\n"
        "User: ¿Qué pasó en Alemania en el año 1989?\n"
        "Assistant: CORTA\n"
        "User: ¿Cómo se desarrollaron las invasiones inglesas en el Río de la Plata?\n"
        "Assistant: LARGA\n"
        "User: Decime todos los eventos que ocurrieron durante la década de 1930.\n"
        "Assistant: LARGA\n"
    )

    prompt_usuario = f"PREGUNTA DEL USUARIO: {pregunta}\nRESPUESTA:"

    prompt_final = [
        {
            'role': 'system', 
            'content': prompt_sistema
        },
        {
            'role': 'user', 
            'content': prompt_usuario
        }
    ]

    try:
        respuesta = ollama.chat(
            model=modelo,
            messages=prompt_final,
            options={
                "temperature": 0.0,
                "num_predict": 3   # Ajustado a 3 tokens para permitir la palabra 'CORTA' o 'LARGA'
            }
        )
        
        # Limpieza estándar de la salida
        resultado = respuesta['message']['content'].strip().upper().replace(".", "")
        return resultado
        
    except Exception as e:
        print(f"[Inferencia] Error crítico en el motor de Ollama: {e}")
        return ""