from adaptar_anios import adaptar_anios

def preguntar(pregunta: str) -> str:
	print(f"Pregunta: {pregunta}")
	print(f"Respuesta: {adaptar_anios(pregunta, 'Delfin')}")

if __name__ == "__main__":
	print(">>> Pregunta B: Prueba adaptar años")

	preguntar("¿Que ocurrió en Argentina en 2020?")
	preguntar("¿Que ocurrió en Argentina en 2022?")
	preguntar("Dame una lista de eventos historicos ocurridos en argentina en la ultima decada.")
	preguntar("¿Que ocurrió en Argentina entre 2020 y 2022?")
	preguntar("En que año ocurrió el peor atentado terrorista en la historia de Argentina?")