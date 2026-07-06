from chat_rag_clasico import iniciar_chat_clasico
from chat_rag_adaptativo import iniciar_chat_adaptativo
from persistencia.lector import leer_configuracion

def main():
	configuracion = leer_configuracion("datos/CONFIGURACION.json")
		
	print("=======================================================")
	print("	  SISTEMA RAG HISTÓRICO - PANEL DE CONTROL		 ")
	print("=======================================================")

	while True:
		print("\nSelecciona el modo de ejecución para interactuar:")
		print("1. Chat RAG Clásico (Inyecta contexto plano con límite fijo)")
		print("2. Chat RAG Adaptativo (Clasifica y enruta dinámicamente)")
		print("3. Salir del programa")
		print("-------------------------------------------------------")
		
		opcion = input("Opción seleccionada: ").strip()
		
		if opcion == "1":
			iniciar_chat_clasico(configuracion)
			break

		if opcion == "2":
			iniciar_chat_adaptativo(configuracion)
			break

		if opcion == "3":
			print("\n[Sistema] Cerrando panel de control. ¡Buen viaje!")
			print("=======================================================\n")
			break
			
		else:
			print("\n[Aviso] Opción inválida. Por favor, ingresa 1, 2 o 3.\n")

if __name__ == "__main__":
	main()