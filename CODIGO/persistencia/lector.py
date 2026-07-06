import json
from persistencia.evento import Evento
from persistencia.configuracion import Configuracion

def leer_datos(direccion: str) -> list[Evento]:
	eventos = []
	datos = leer_json(direccion)
	
	for dato in datos.get("eventos", []):
		evento = Evento(
			pais = dato.get("pais"),
			fecha = dato.get("fecha"),
			evento = dato.get("evento")
		)
		eventos.append(evento)
				
	return eventos

def leer_configuracion(direccion: str) -> Configuracion:
	datos = leer_json(direccion)
	return Configuracion(
		limite = int(datos.get("limite")),
		reqPais = bool(datos.get("reqPais")),
		reqAnio = bool(datos.get("reqAnio")),
		direccionDatos = datos.get("direccionDatos")
	)
	
def leer_json(direccion: str) -> dict:
	datos = {}

	try:
		with open(direccion, 'r', encoding='utf-8') as archivo:
			datos = json.load(archivo)

	except FileNotFoundError:
		print(f"[Lector] Error: No se encontró el archivo en la ruta '{direccion}'.")
	
	except json.JSONDecodeError:
		print(f"[Lector] Error: El archivo no tiene un formato JSON válido.")
	
	return datos