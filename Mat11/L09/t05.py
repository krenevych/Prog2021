array = list(input())
freq = {el: array.count(el) for el in set(array)}
max_ch = max(freq)
print(max_ch, freq[max_ch])
