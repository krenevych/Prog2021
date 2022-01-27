def readfile(fname):
    f = open(fname, encoding='utf-8')
    for line in f:
        print(line, end="")
    f.close()


def showLinesWithLen60(fname):
    f = open(fname, encoding='utf-8')
    for line in f:
        if len(line) > 60:
            print(line, end="")
    f.close()

def findMaxLine(fname):
    f = open(fname, encoding='utf-8')
    maxLine = f.readline()
    for line in f:
        if len(line) > len(maxLine):
            maxLine = line
    f.close()
    return maxLine

# readfile("input2.txt")
# showLinesWithLen60("input2.txt")
maxline = findMaxLine("input2.txt")
print(maxline)

