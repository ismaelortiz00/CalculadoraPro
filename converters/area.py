UNIDADES = {
    "m²": 1,
    "km²": 1000000,
    "cm²": 0.0001,
    "mm²": 0.000001,
    "hectárea": 10000,
    "acre": 4046.8564224,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    metros = valor * UNIDADES[origen]
    return round(metros / UNIDADES[destino], 6)