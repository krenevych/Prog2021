
while True:
    try:
        s = input()
    except:
        break

    word_list = s.split()
    for word in word_list:
        print(len(word), end=" ")

