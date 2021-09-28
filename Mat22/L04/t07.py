# n = 2: 10,..,99
# n = 3: 100,..,999
# n = 4: 1000,..,9990

# for n in range(1, 10):
#     start = 10 ** (n-1)
#     end   = 10 ** n
#     counter = 0
#     for i in range(start, end):
#         if i % 2 == 0:
#             counter += 1
#
#     print(counter)

n = int(input())
if n == 1:
    print(4)
else:
    print(45 * 10 ** (n - 2))
