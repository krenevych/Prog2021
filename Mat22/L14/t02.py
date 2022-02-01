s = "34lkj;3245;jlk1234lkj128"
sum = 0
for k in s:
    try:
        sum += int(k)
    except ValueError:
        continue
print(sum)