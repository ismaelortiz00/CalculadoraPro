UNIDADES = {
    "ml": 0.001,
    "l": 1,
    "m³": 1000,
    "galón": 3.78541,
    "taza": 0.236588,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    litros = valor * UNIDADES[origen]
    return round(litros / UNIDADES[destino], 6)