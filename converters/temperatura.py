def convertir(valor, origen, destino):
    valor = float(valor)

    if origen == destino:
        return round(valor, 6)

    if origen == "C":
        c = valor
    elif origen == "F":
        c = (valor - 32) * 5 / 9
    elif origen == "K":
        c = valor - 273.15
    else:
        raise ValueError("Unidad no válida")

    if destino == "C":
        return round(c, 6)
    if destino == "F":
        return round((c * 9 / 5) + 32, 6)
    if destino == "K":
        return round(c + 273.15, 6)

    raise ValueError("Unidad no válida")