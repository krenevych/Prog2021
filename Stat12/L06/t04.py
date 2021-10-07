s = input()

# s = "   Alexandr    Sergeevich   Pushkin    "
# "Alexandr Sergeevich Pushkin"
# res = " "

word_list = s.split()
res = " ".join(word_list)
print(res)

# res = s[0]
# for c in s[1:]:
#     if c != " ":
#         res += c
#     else:
#         if res[-1] != " ":
#             res += c
#
# if res[0] == " ":
#     res = res[1:]
#
# if res[-1] == " ":
#     res = res[: -1]
#
# print(res)


