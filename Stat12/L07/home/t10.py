def toDec(s):
    "Конвертує цифру у десяткове зображення"
    # "A" -> 9 + 1 = 10
    # "B" -> 9 + 2 = 11
    # "C" -> 9 + 3 = 12
    # "D" -> 9 + 4 = 13
    # "Z" -> 9 + 26 = 35
    if '0' <= s <='9':
        res = int(s)
        return res
    else:
        delta = ord(s) - ord("A") + 1
        res = 9 + delta
        return res

def fromDec(n):
    # "Конвертує десяткове зображення у цифру у символьну вигляді
    #  13 - > "D"
    #  5  - > "5"

    if 0 <= n <= 9:
        return str(n)
    else:
        c_A = ord("A")
        c = c_A + n - 10
        s = chr(c)
        return s

def convertToDec(n, b):
#     Перетворює число записане у системі числення з основою b у десяткову систему числення
#     n = "DCBA", b = 16
#   D 16^3 + C 16^2 + B 16^1 + A 16^0
#   13 * 16^3 + 12 * 16^2 + 11 * 16^1 + 10 16^0
    if b == 10:
        return int(n)

    res = 0
    for d in n:
        d_dec = toDec(d)
        res = res * b + d_dec
    return res

def convertFromDec(n, b):
    #     Перетворює число записане у десятковій системі числення число у системі числення з основою b
    # 256
    # res =  "256"
    res = ""
    while n > 0:
        last = n % b
        d = fromDec(last)
        res = d + res
        n //= b

    return res

def convert(num, n, k):
    #     Перетворює число записане у системі числення з основою n у число записане у системі числення k
    todec = convertToDec(num, n)
    frdec = convertFromDec(todec, k)
    return frdec

n, k = [int(el) for el in input().split()]
num = input()

if n == k:
    print(num)
else:
    res = convert(num, n, k)
    print(res)


