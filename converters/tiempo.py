UNIDADES = {
    "segundo": 1,
    "minuto": 60,
    "hora": 3600,
    "día": 86400,
    "semana": 604800,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    segundos = valor * UNIDADES[origen]
    return round(segundos / UNIDADES[destino], 6)