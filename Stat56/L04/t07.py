n = int(input())

# n = 4: 1000 .. 9999 -> парних

# start = 10**(n - 1)
# end = 10**n
# counter = 0
# for i in range(start, end):
#     if i % 2 == 0: counter += 1
#
# print(counter)
if n == 1:
    print(4)
else:
    print(45 * 10**(n-2))
