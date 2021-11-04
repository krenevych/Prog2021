s = input()
set_s = set(s)
freq = {elem: s.count(elem) for elem in set_s}
max_el = max(freq)
print(max_el, freq[max_el])
