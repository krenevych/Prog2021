s = input()
uniq = set(s)
freq = {el:s.count(el) for el in uniq}
# print(freq)

max_leter = max(freq)
print(max_leter, freq[max_leter])
