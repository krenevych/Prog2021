# s = "     Alexandr    Sergeevich   Pushkin       "
s = input()

new_s = s[0]
for ch in s[1:]:
    if not ch.isspace(): # ch != " "
        new_s += ch
    else:
        if new_s[-1] != " ":
            new_s += " "

if new_s[0].isspace():
    new_s = new_s[1:]

if new_s[-1].isspace():
    new_s = new_s[:-1]

print(new_s)