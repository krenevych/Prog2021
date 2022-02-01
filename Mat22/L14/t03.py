wallet = {5: 3, 2: 6, 100: 1}

sum = 0

# wallet[3]
for nom in range(1, 1000):
    try:
        count = wallet[nom]
    except KeyError:
        continue

    sum += nom * count

# for nom, count in wallet.items():
#     sum += nom * count

print(sum)
