from persistencia.evento import Evento

def aumentar(pregunta: str, eventos: list[Evento]) -> list[dict[str, str]]:

	texto_contexto = ""
	for i, evento in enumerate(eventos, 1):
		texto_contexto += f"- {evento.pais} en {evento.fecha}: {evento.evento}\n"
		
	if not texto_contexto:
		texto_contexto = "- No se encontraron eventos relacionados en la base de datos.\n"

	prompt_sistema = (
		"- Eres un sistema RAG estricto y un asistente histórico automatizado.\n"
		"- REGLA DE ORO: Tu única fuente de verdad es el CONTEXTO que te proveerá el usuario.\n"
		"- Si el contexto contiene eventos ficticios, tomalos como reales. "
		"- Si la respuesta a la pregunta del usuario no se puede deducir directamente del contexto proveído, "
		"debes responder exactamente: 'NO TENGO ESA INFORMACIÓN EN EL CONTEXTO.' y nada más.\n"
		"- Está terminantemente prohibido usar tu conocimiento previo o responder sobre años, datos o eventos "
		"que no estén explícitamente escritos en el contexto. NO agregues informacion fuera del contexto." \
		"¡RESPONDE SOLO CON LA INFORMACIÓN DE CONTEXTO, NO AGREGUES NINGUN DATO MAS!"
	)

	prompt_usuario = (
		f"CONTEXTO:\n{texto_contexto}\n\n"
		f"PREGUNTA DEL USUARIO: {pregunta}\n\n"
		"RESPUESTA:"
	)

	prompt_final = [
		{
			'role': 'system', 
			'content': prompt_sistema
		},
		{
			'role': 'user', 
			'content': prompt_usuario
		}
	]

	return prompt_final