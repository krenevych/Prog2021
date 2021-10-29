# s = "asdffdsa"
# isSym(s) = (перший символ рядка s == останній символ рядка s) і isSym(s без першого і останнього)

# прямий хід рекурсії
# isSym("asdffdsa") = "a" == "a" and isSym("sdffds")
#                                        ||
#                                    "s" == "s"  and  isSym("dffd")
#                                                         ||
#                                                      "d" == "d"  and  isSym("ff")
#                                                                          ||
#                                                                       "f" == "f"  and  isSym("")
#                                                                                          ||
#                                                                                         True

# зворотній хід рекурсії
# isSym("asdffdsa") = "a" == "a" and True = True
#                                        ||
#                                    "s" == "s"  and  True = True
#                                                         ||
#                                                      "d" == "d"  and  True = True
#                                                                          ||
#                                                                       "f" == "f"  and  True = True
#                                                                                          ||
#                                                                                         True


# isSym("asdffdEa") = "a" == "a" and False = False
#                                        ||
#                                    "s" == "E"  and  isSym("dffd") = False

def isSym(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isSym(s[1:-1])

print(isSym("asdffdsa"))


def invert(s):
    if s == '':
        return s
    else:
        return invert(s[1:]) + s[0]

s = input()
print(invert(s))

# invert("ads") = invert("ds") + "a" = "sd" + "a" = "sda"
#                     ||
#                     invert("s") + "d" = "s" + "d" = "sd"
#                     ||
#                     invert("") + "s" = "" + "s" = "s"
#                     ||
#                     ""
#