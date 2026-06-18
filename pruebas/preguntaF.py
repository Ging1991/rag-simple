from rag_adaptativo import preguntar

if __name__ == "__main__":
	print(">>> EJECUTANDO CASO E: Pregunta sobre hitos en un mismo año")
	pregunta = "¿Que paso en ALEMANIA en 1992?"
	respuesta = preguntar(pregunta)
		
	print("\n[RESULTADO ENTREGADO AL USUARIO - CASO E]:")
	print(respuesta)
	print("-" * 60 + "\n")
