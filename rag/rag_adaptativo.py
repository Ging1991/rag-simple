from rag.fases.recuperacion import obtener_contexto
from rag.fases.inferencia import generar
from rag.fases.aumentacion import aumentar
from rag.adaptativo.adaptar_anios import adaptar_anios
from rag.adaptativo.adaptar_paises import adaptar_paises
from rag.adaptativo.adaptar_limite import adaptar_limite
from persistencia.configuracion import Configuracion

def preguntar(pregunta: str, configuracion: Configuracion) -> str:

	flagReqAnio = (adaptar_anios(pregunta, 'Delfin') == "SI")
	print("\n[PRE PROCESAMIENTO] Requiere año: {}".format(flagReqAnio))
	flagReqPais = (adaptar_paises(pregunta, 'Delfin') == "SI")
	print("[PRE PROCESAMIENTO] Requiere país: {}".format(flagReqPais))
	limite = adaptar_limite(pregunta, 'Delfin')
	print("[PRE PROCESAMIENTO] Tipo de pregunta: {}".format(limite))
	if (limite == 'LARGA'):
		limite = 5
	else:
		limite = 1

	configuracion.reqAnio = flagReqAnio
	configuracion.reqPais = flagReqPais
	configuracion.limite = limite

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