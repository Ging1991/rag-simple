import ollama

def generar(prompt: list, modelo: str) -> str:
	"""	Proceso de Inferencia Puro usando la librería oficial de Ollama. """

	try:
		respuesta = ollama.chat(
			model = modelo,
			messages = prompt,
			options = {
				"temperature": 0.0  # Forzamos determinismo para mitigar alucinaciones
			}
		)
		
		# En chat, la respuesta se extrae navegando el objeto devuelto
		return respuesta['message']['content'].strip()
		
	except Exception as e:
		print(f"[Inferencia] Error crítico en el motor de Ollama: {e}")
		return ""