def calcular(peso, altura):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"

    return round(imc, 2), estado