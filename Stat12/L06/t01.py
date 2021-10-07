expr = input()

counter = 0
for c in expr[1:]:
    # if c == "+" or c == "-" or c == "*":
    if c in "+-*":
        counter += 1

print(counter)

# 1+2*3+a
