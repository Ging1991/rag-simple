from rag.rag_adaptativo import preguntar
from persistencia.lector import leer_configuracion
from persistencia.configuracion import Configuracion

def iniciar_chat_adaptativo(configuracion: Configuracion):
	"""
	Mantiene un bucle interactivo en la terminal para realizar preguntas
	al sistema RAG Adaptativo hasta que el usuario decida salir.
	"""
	print("\n=======================================================")
	print("	  INICIANDO MODO: CHAT RAG ADAPTATIVO				 ")
	print("=======================================================")
	print("Instrucciones: Escribe tu pregunta histórica y presiona Enter.")
	print("Para salir del chat, escribe el número '1'.")
	print("=======================================================\n")

	while True:
		pregunta_usuario = input("Tú: ").strip()

		if pregunta_usuario == "1":
			print("\n[Chat] Saliendo del modo adaptativo. ¡Hasta luego!")
			print("=======================================================\n")
			break

		if not pregunta_usuario:
			print("[Sistema] La pregunta no puede estar vacía. Intenta de nuevo.\n")
			continue

		try:
			print("\n[Sistema] Procesando consulta en el RAG Adaptativo...")
			respuesta_ia = preguntar(pregunta_usuario, configuracion)
			print(f"\nDelfín (RAG Adaptativo): {respuesta_ia}")
			print("\n-------------------------------------------------------")
			
		except Exception as e:
			print(f"\n[Chat] Ocurrió un error inesperado durante la consulta: {e}")
			print("-------------------------------------------------------")
