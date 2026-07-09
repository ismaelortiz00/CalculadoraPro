TASAS = {
    "USD": 1,
    "EUR": 0.92,
    "COP": 3900,
    "MXN": 17,
    "PEN": 3.7,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    usd = valor / TASAS[origen]
    return round(usd * TASAS[destino], 6)