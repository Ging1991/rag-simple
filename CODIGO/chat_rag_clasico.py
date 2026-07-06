from rag.rag_clasico import preguntar
from persistencia.configuracion import Configuracion

def iniciar_chat_clasico(configuracion: Configuracion):
	"""
	Mantiene un bucle interactivo en la terminal para realizar preguntas
	al sistema RAG Clásico hasta que el usuario decida salir.
	"""
	print("\n=======================================================")
	print("	  INICIANDO MODO: CHAT RAG CLÁSICO				 ")
	print("=======================================================")
	print("Instrucciones: Escribe tu pregunta histórica y presiona Enter.")
	print("Para salir del chat, escribe el número '1'.")
	print("=======================================================\n")

	while True:
		pregunta_usuario = input("Tú: ").strip()

		if pregunta_usuario == "1":
			print("[SISTEMA] Saliendo del modo clásico. ¡Hasta luego!")
			print("=======================================================\n")
			break

		if not pregunta_usuario:
			print("[SISTEMA] La pregunta no puede estar vacía. Intenta de nuevo.\n")
			continue

		try:
			print("[SISTEMA] Procesando consulta en el RAG Clásico.")
			respuesta_ia = preguntar(pregunta_usuario, configuracion)
			print(f"[PREGUNTA USUARIO]: {pregunta_usuario}")
			print(f"[RESPUESTA DELFIN]: {respuesta_ia}")
			print("\n-------------------------------------------------------")
			
		except Exception as e:
			print(f"\n[SISTEMA] Ocurrió un error inesperado durante la consulta: {e}")
			print("-------------------------------------------------------")
