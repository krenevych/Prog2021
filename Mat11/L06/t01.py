s = input()

counter = 0
for ch in s[1:]: # ітеруємо починаючи з 1-го
    # (рахуючи з нуля) символа
    if ch == "+" or ch == "-" or ch == "*":
        counter += 1

print(counter)
# 1 + 2
# 1+2*3+a
