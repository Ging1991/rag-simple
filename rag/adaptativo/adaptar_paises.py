import ollama

def adaptar_paises(pregunta: str, modelo: str) -> str:
    """ 
    Proceso de Inferencia Puro: Define si el usuario pregunta 
    por un país en específico.
    """

    prompt_sistema = (
        "Eres un clasificador binario estricto. Analizas preguntas históricas.\n"
        "Tu única tarea es determinar si la pregunta del usuario menciona o solicita "
        "información sobre UN PAÍS ESPECÍFICO (ej. Argentina, Francia, Alemania, México).\n\n"
        
        "REGLAS:\n"
        "- Responde ÚNICAMENTE con la palabra 'SI' o la palabra 'NO'.\n"
        "- Está terminantemente prohibido agregar puntuación, explicaciones o justificaciones.\n"
        "- Si la pregunta NO menciona ningún país, responde 'NO'.\n"
        "- Si la pregunta es global, habla del mundo en general o de un continente entero (ej. Europa, América), responde 'NO'.\n\n"
        
        "EJEMPLOS DE COMPORTAMIENTO:\n"
        "User: ¿Qué pasó en Alemania en el año 1989?\n"
        "Assistant: SI\n"
        "User: Decime la historia económica de Francia.\n"
        "Assistant: SI\n"
        "User: ¿Qué eventos desataron la Segunda Guerra Mundial a nivel mundial?\n"
        "Assistant: NO\n"
        "User: ¿Cómo era la situación colonial en América del Sur?\n"
        "Assistant: NO\n"
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
                "num_predict": 2   # Forzamos al modelo a no extenderse
            }
        )
        
        # Limpieza de seguridad en la salida
        resultado = respuesta['message']['content'].strip().upper().replace(".", "")
        return resultado
        
    except Exception as e:
        print(f"[Inferencia] Error crítico en el motor de Ollama: {e}")
        return ""