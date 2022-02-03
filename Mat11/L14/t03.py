wallet = {5: 4, 20: 1, 100: 2}

suma = 0
maxNominal = 1000


for nominal in range(1, maxNominal + 1):
    try:
        suma += nominal * wallet[nominal]
    except KeyError:
        pass

# for nominal, quantity in wallet.items():
#     suma += nominal * quantity

print("У гаманці є ", suma, "грошей")