# s = 'Hello  ,   world!'
s = input()

new_s = ""
for c in s:
    # if ("A" <= c <= "Z" or "a" <= c <= "z" or
    #         "0" <= c <= "9" or c == " "):
    if c.isalnum() or c.isspace():
        new_s += c

s= new_s

word_list = s.split()
# print(word_list)


print(len(word_list))