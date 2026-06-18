from rag_clasico import preguntar

if __name__ == "__main__":
	# -------------------------------------------------------------------------
	# CASO A: Pregunta de Amplio Contexto 
	# -------------------------------------------------------------------------
	print(">>> EJECUTANDO CASO A: Pregunta sobre hitos en un mismo año")
	pregunta = "¿En que año se hundio el barco HURACANAZO en argentina?"
	respuesta = preguntar(pregunta)
		
	print("\n[RESULTADO ENTREGADO AL USUARIO - CASO A]:")
	print(respuesta)
	print("-" * 60 + "\n")
