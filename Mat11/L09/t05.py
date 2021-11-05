s = input()
freq = {el: s.count(el) for el in set(s)}
max_ch = max(freq)
print(max_ch, freq[max_ch])
