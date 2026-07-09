UNIDADES = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "pulgada": 0.0254,
    "pie": 0.3048,
    "yarda": 0.9144,
    "milla": 1609.344,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    metros = valor * UNIDADES[origen]
    return round(metros / UNIDADES[destino], 6)