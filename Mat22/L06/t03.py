s = input()

new_s = ""
for ch in s:
    new_s += ch
    if ch in "aeiouy":
        new_s += ch

print(new_s)

# s = "1234"
# s2 = "5678"
# s = s + s2
# print(s)
