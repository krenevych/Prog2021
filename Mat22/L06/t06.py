s = "Hello  9999 ,   world!"

s = input()

corected = ""
for ch in s:
    if ch.isalnum() or ch.isspace():
        corected += ch

# print(corected)

word_list = corected.split()
print(len(word_list))




