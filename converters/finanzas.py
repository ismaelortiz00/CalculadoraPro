def interes_simple(capital, tasa, tiempo):
    capital = float(capital)
    tasa = float(tasa) / 100
    tiempo = float(tiempo)

    interes = capital * tasa * tiempo
    total = capital + interes

    return round(interes, 2), round(total, 2)