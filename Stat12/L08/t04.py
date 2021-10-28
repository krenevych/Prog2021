# s = "asdsaasdsaasdsaasdsa"
# isSym(s) = перший символ == останньому символу
#              and isSym(s без першого і останнього символів)
# isSym(s) = True, якщо s складається з одного символа
#                  або порожній "" "a"

def isSym(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            res = isSym(s[1:-1])
            return res
            # return s[0] == s[-1] and isSym(s[1:-1])


def inv(s):
    if len(s) == 0:
        return s
    else:
        return inv(s[1:]) + s[0]

print(inv("asdf"))
# asdf => fdsa

# inv("asdf") =  "fdsa"
#     ||
#    "fds" + "a" = "fdsa"
#     ||
#     "fd"  + "s" = "fds"
#     ||
#     "f"  + "d"  = "fd"
#     ||
#     ""  + "f" = "f"
#     ||
#     ""

print(isSym("asddea"))