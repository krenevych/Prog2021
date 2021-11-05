s1 = input()
s2 = input()

freq1 = {c: s1.count(c) for c in set(s1)}
freq2 = {c: s2.count(c) for c in set(s2)}
#
# print(freq1)
# print(freq2)

for ch in freq2:
    if freq2[ch] > freq1[ch]:
        print("No")
        break
else:
    print("Ok")

