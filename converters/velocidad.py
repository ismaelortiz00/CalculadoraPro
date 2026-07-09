UNIDADES = {
    "km/h": 1,
    "m/s": 3.6,
    "mph": 1.60934,
    "nudos": 1.852,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    kmh = valor * UNIDADES[origen]
    return round(kmh / UNIDADES[destino], 6)