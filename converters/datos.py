UNIDADES = {
    "bit": 1,
    "byte": 8,
    "KB": 8192,
    "MB": 8388608,
    "GB": 8589934592,
    "TB": 8796093022208,
}

def convertir(valor, origen, destino):
    valor = float(valor)
    bits = valor * UNIDADES[origen]
    return round(bits / UNIDADES[destino], 6)