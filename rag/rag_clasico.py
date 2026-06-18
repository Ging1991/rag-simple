from persistencia.configuracion import Configuracion
from rag.fases.recuperacion import obtener_contexto
from rag.fases.inferencia import generar
from rag.fases.aumentacion import aumentar

def preguntar(pregunta: str, configuracion: Configuracion) -> str:

	print("\n[Paso 1/3] Fase de recuperación...")
	contexto_recuperado = obtener_contexto(pregunta, configuracion)

	print("\n[Paso 2/3] Fase de aumentacion...")
	prompt = aumentar(pregunta, contexto_recuperado)

	print("--- Prompt Generado (Inyectado) ---")
	print(prompt)
	print("-----------------------------------")

	print("\n[Paso 3/3] Fase de generacion...")
	respuesta = generar(prompt, modelo="Delfin")
		
	return respuesta