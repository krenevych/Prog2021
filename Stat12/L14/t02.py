line = "123eujk13jkj12j4jk553kk2jfos0fsd0dvdv8vsd9cdwr7w81"
sum = 0
for el in line:
    try:
        sum += int(el)
    except ValueError:
        pass

print(sum)