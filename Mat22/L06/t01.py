# s = "-1+2*3+a"  # s[1:] = "1+2*3+a"
# s = "+5-2+4-m/n*2:4"  # s[1:] = "1+2*3+a"
s = input()

counter = 0
for ch in s[1:]:
    if ch == "+" or ch == "-" or ch == "*":
        counter += 1

print(counter)

