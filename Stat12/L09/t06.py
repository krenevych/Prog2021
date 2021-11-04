s1 = input()
s2 = input()

freq1 = {el: s1.count(el) for el in set(s1)}
freq2 = {el: s2.count(el) for el in set(s2)}

# print(freq1)
# print(freq2)

for l, c in freq2.items():
    if l not in freq1 or c > freq1[l]:
        print("No")
        break
else:
    print("Ok")
