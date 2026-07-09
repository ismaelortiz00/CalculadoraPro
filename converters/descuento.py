def calcular(precio, porcentaje):
    precio = float(precio)
    porcentaje = float(porcentaje)

    descuento = precio * porcentaje / 100
    total = precio - descuento

    return round(descuento, 2), round(total, 2)