def conversor_de_divisas(ahorro):
    dólares = 210 * ahorro
    reales = 80 * ahorro
    euros = 221 * ahorro

    return f"Usted tiene ${mis_pesos} pesos argentinos," \
           f"los cuales se convierten en:\n" \
           f"-U$ {dólares} dólares.\n" \
           f"-R$ {reales} reales.\n" \
           f"-€$ {euros} euros."


mis_pesos = 150

print(conversor_de_divisas(mis_pesos))
