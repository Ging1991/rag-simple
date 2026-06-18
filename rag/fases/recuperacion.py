from persistencia.evento import Evento
from persistencia.lector import leer_datos
from persistencia.configuracion import Configuracion

def limpiar_texto(texto: str) -> str:
	"""
	- Cambia las letras acentuadas por su equivalente sin tilde.
	- Deja solo palabras separadas por espacios
	"""

	remplazo_tildes = {
		"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
		"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"
	}
		
	texto_sin_tildes = texto
	for con_tilde, sin_tilde in remplazo_tildes.items():
		texto_sin_tildes = texto_sin_tildes.replace(con_tilde, sin_tilde)
		
	caracteres_a_limpiar = [",", ".", "(", ")", "?", "!", '"', "'", ";", ":", "¿", "¡"]
	texto_limpio = texto_sin_tildes
	for caracter in caracteres_a_limpiar:
		texto_limpio = texto_limpio.replace(caracter, " ")
	return texto_limpio

def extraer_anios(texto: str) -> list:
	""" Extrae de forma explícita los años de 4 dígitos presentes en un texto """
	anios_encontrados = []
	for palabra in texto.split():
		if palabra.isdigit() and len(palabra) == 4:
			if palabra not in anios_encontrados:
				anios_encontrados.append(palabra)
					
	return anios_encontrados

def extraer_paises(texto: str) -> list:
	""" Extrae palabras candidatas a países (Min 4 caracteres, solo letras, sin tildes ni eñes)	"""

	paises_candidatos = []
	for palabra in texto.split():
		palabra_mayus = palabra.upper()
		
		if len(palabra_mayus) >= 4 and palabra_mayus.isalpha():
			if palabra_mayus not in paises_candidatos:
				paises_candidatos.append(palabra_mayus)
					
	return paises_candidatos

def obtener_contexto(pregunta: str, configuracion: Configuracion) -> list[Evento]:
	
	eventos = leer_datos(configuracion.direccionDatos)
	print(f"[RECUPERACION] Eventos: {len(eventos)}")

	pregunta = limpiar_texto(pregunta)
	anios = extraer_anios(pregunta)
	paises = extraer_paises(pregunta)
	print(f"[RECUPERACION] Años : {anios} | Países: {paises}")

	contexto = []
	for evento in eventos:
		if not evento.fecha in anios and configuracion.reqAnio:
			continue

		if not evento.pais in paises and configuracion.reqPais:
			continue

		if evento.fecha in anios or evento.pais in paises:
			contexto.append(evento)
			
	resultados_finales = contexto[:configuracion.limite]
		
	print(f"[RECUPERACION] Encontrados: {len(contexto)} | Devueltos (Límite {configuracion.limite}): {len(resultados_finales)}")
	return resultados_finales