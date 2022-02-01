maxNominal = 1000
wallet = {2: 5, 5: 10, 100: 2}

suma = 0
# for nom, quant in wallet.items():
#     suma += nom * quant

for nom in range(1, maxNominal):
    try:
        suma += nom * wallet[nom]
    except KeyError:
        pass


print(suma)
