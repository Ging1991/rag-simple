import json
from persistencia.evento import Evento
from persistencia.configuracion import Configuracion

def leer_datos(direccion: str) -> list[Evento]:
	eventos = []
		
	try:
		with open(direccion, 'r', encoding='utf-8') as archivo:
			datos_crudos = json.load(archivo)
			
			for item in datos_crudos.get("eventos", []):
				nuevo_evento = Evento(
					pais=item.get("pais"),
					fecha=item.get("fecha"),
					evento=item.get("evento")
				)
				eventos.append(nuevo_evento)
				
		return eventos
		
	except FileNotFoundError:
		print(f"[Lector] Error: No se encontró el archivo en la ruta '{direccion}'.")
		return []
	except json.JSONDecodeError:
		print(f"[Lector] Error: El archivo no tiene un formato JSON válido.")
		return []

def leer_configuracion(direccion: str) -> Configuracion:
	try:
		with open(direccion, 'r', encoding='utf-8') as archivo:
			datos = json.load(archivo)
			
			return Configuracion(
				limite = int(datos.get("limite")),
				reqPais = bool(datos.get("reqPais")),
				reqAnio = bool(datos.get("reqAnio")),
				direccionDatos = datos.get("direccionDatos")
			)
		
	except FileNotFoundError:
		print(f"[Lector] Error: No se encontró el archivo en la ruta '{direccion}'.")
		return Configuracion(limite=5, reqPais=False, reqAnio=False, direccionDatos="")
	
	except json.JSONDecodeError:
		print(f"[Lector] Error: El archivo no tiene un formato JSON válido.")
		return Configuracion(limite=5, reqPais=False, reqAnio=False, direccionDatos="")