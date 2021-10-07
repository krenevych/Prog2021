s = input()
# Hello9, world!

res = ""
for c in s:
    if c.isalnum() or c.isspace():
        res += c

print(len(res.split()))