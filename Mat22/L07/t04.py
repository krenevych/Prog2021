
# aasbaasssssssssasba
# isSym(s) = s[0] == s[-1] and isSym(s без першого та останнього символів)
# isSym(s) = True, s - складається
#               з одного символа або порожній

def isSym(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isSym(s[1:-1])

# reversestr("asd") =   "ds" + "a" = "dsa"
#                       ||
#                        "d" + "s"  = "ds"
#                       ||
#                       "" + "d" = "d"
#                       ||
#                       ""

def reversestr(s):
    if s=="":
        return s
    else:
        return reversestr(s[1:]) + s[0]

print(isSym("abcca"))

# "asdf" -> "fdsa"