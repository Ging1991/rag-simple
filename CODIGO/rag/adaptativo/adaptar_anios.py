import ollama

def adaptar_anios(pregunta: str, modelo: str) -> str:
    """ 
    Proceso de Inferencia Puro: Define si el usuario pregunta 
    por un único año en específico.
    """

    prompt_sistema = (
        "Eres un clasificador binario estricto. Analizas preguntas históricas.\n"
        "Tu única tarea es determinar si la pregunta del usuario menciona o solicita "
        "información sobre UN AÑO ESPECÍFICO (ej. 1989, 1492, 2022).\n\n"
        
        "REGLAS:\n"
        "- Responde ÚNICAMENTE con la palabra 'SI' o la palabra 'NO'.\n"
        "- Está terminantemente prohibido agregar puntuación, explicaciones o justificaciones.\n"
        "- Si la pregunta NO menciona ningún año, responde 'NO'.\n"
        "- Si la pregunta menciona un rango de años, responde 'NO'.\n"
        "- Si la pregunta menciona MÁS DE UN año, responde 'NO'.\n\n"
        
        "EJEMPLOS DE COMPORTAMIENTO:\n"
        "User: ¿Qué pasó en Alemania en el año 1989?\n"
        "Assistant: SI\n"
        "User: ¿Qué eventos ocurrieron en Argentina en 1810?\n"
        "Assistant: SI\n"
        "User: Decime los eventos entre 1930 y 1945.\n"
        "Assistant: NO\n"
        "User: ¿Qué pasó en Francia en el siglo XVIII?\n"
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
                "num_predict": 2   # Limitamos los tokens de salida drásticamente para forzar el SI/NO
            }
        )
        
        # Limpiamos tildes, mayúsculas y puntos extra por seguridad
        resultado = respuesta['message']['content'].strip().upper().replace(".", "")
        return resultado
        
    except Exception as e:
        print(f"[Inferencia] Error crítico en el motor de Ollama: {e}")
        return ""