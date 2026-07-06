from persistencia.configuracion import Configuracion
from rag.fases.recuperacion import obtener_contexto
from rag.fases.inferencia import generar
from rag.fases.aumentacion import aumentar

def preguntar(pregunta: str, configuracion: Configuracion) -> str:

	print("[SISTEMA] Iniciando RAG Clásico.")

	contexto_recuperado = obtener_contexto(pregunta, configuracion)
	print("[Paso 1/3] Fase de recuperación...OK")

	prompt = aumentar(pregunta, contexto_recuperado)
	print("[Paso 2/3] Fase de aumentación...OK")

	respuesta = generar(prompt, modelo="Delfin")
	print("[Paso 3/3] Fase de generación...OK")
		
	return respuesta