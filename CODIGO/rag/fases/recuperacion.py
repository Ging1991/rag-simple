from persistencia.evento import Evento
from persistencia.lector import leer_datos
from persistencia.configuracion import Configuracion

def limpiar_texto(texto: str) -> str:
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
	anios = set()
	for palabra in texto.split():
		if palabra.isdigit() and len(palabra) == 4:
			anios.add(palabra)
					
	return list(anios)

def extraer_paises(texto: str) -> list:
	paises_unicos = set()
	for palabra in texto.split():
		palabra_mayus = palabra.upper()
		if len(palabra_mayus) >= 4 and palabra_mayus.isalpha():
			paises_unicos.add(palabra_mayus)
	return list(paises_unicos)

def obtener_contexto(pregunta: str, configuracion: Configuracion) -> list[Evento]:
	
	eventos = leer_datos(configuracion.direccionDatos)
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
		
		if len(contexto) >= configuracion.limite:
			break
			
	print(f"[RECUPERACION] Contexto: [{len(contexto)}] eventos recuperados.")
	return contexto