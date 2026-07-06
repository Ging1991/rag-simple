class Configuracion:
	def __init__(self, limite: int, reqPais: bool, reqAnio: bool, direccionDatos: str):
		self.limite = limite
		self.reqPais = reqPais
		self.reqAnio = reqAnio
		self.direccionDatos = direccionDatos