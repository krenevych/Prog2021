# Описати підпрограму, яка утворює текстовий файл із 9 рядків,
# у першому з яких одна літера '1', у другому – дві літери '2',
# ... , у дев’ятому – дев’ять літер '9'.

f = open("output133.txt", "w")
# print("Q" * 10)
for i in range(1, 10):
    print(str(i) * i, file=f)
f.close()
