from adaptar_limite import adaptar_limite

def preguntar(pregunta: str) -> str:
	print(f"Pregunta: {pregunta}")
	print(f"Respuesta: {adaptar_limite(pregunta, 'Delfin')}")

if __name__ == "__main__":
	print(">>> Pregunta D: Prueba adaptar límites")

	preguntar("¿Que ocurrió en Europa en 2020?")
	preguntar("¿Que ocurrió en Argentina en 2022?")
	preguntar("Dame una lista de eventos historicos ocurridos en argentina en la ultima decada.")
	preguntar("¿Que ocurrió en USA entre 2020 y 2022?")
	preguntar("En que año ocurrió el hundimiento del titanic?")