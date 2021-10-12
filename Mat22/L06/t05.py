# WWWellcccooomee  ttoo PPyythooonn!!!
# Welcome to Python!

s = "WWWellcccooomee  ttoo PPyythooonn!!!"

new_s = s[0]  # "W"
for ch in s[1:]:
    if ch != new_s[-1]:
        new_s += ch

print(new_s)