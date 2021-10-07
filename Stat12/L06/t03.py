s = input()

# weelcoomee too pyythonn


res_s = "" # рядок для результата
for c in s:
    if c in "aeiouy":
        res_s = res_s + c + c
    else:
        res_s = res_s + c

print(res_s)

