UNIDADES = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1,
    "tonelada": 1000,
    "libra": 0.45359237,
    "onza": 0.0283495,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    kg = valor * UNIDADES[origen]
    return round(kg / UNIDADES[destino], 6)