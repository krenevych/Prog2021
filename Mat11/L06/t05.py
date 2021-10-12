# s = "WWWellcccooomee  ttoo PPyythooonn!!!"
# s = "Welcome to Python!"
s = input()
new_s = s[0]
for ch in s[1:]:
    if new_s[-1] != ch:
        new_s += ch

print(new_s)