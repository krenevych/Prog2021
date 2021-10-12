s = input() # welcome to python
vowels = "aeiouy"

new_s = ""
for ch in s:
    new_s += ch
    if ch in vowels:
        new_s += ch

print(new_s)
