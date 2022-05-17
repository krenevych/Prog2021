from Mat11.O09.task2.FileObserver import FileObserver
from Mat11.O09.task2.FileReader import FileReader

############################
class LinesPrinter(FileObserver):

    # заміщення абстрактного методу
    def onReceive(self, line):
        print(line, end="")

###########################
class LinesCounter(FileObserver):
    def __init__(self):
        self.lines = 0

    # заміщення абстрактного методу
    def onReceive(self, line):
        self.lines += 1

    def __str__(self):
        return str(self.lines)
############################
class WordCounter(FileObserver):
    def __init__(self):
        self.wordCounter = 0

    # заміщення абстрактного методу
    def onReceive(self, line):
        self.wordCounter += len(line.split())

    def __str__(self):
        return str(self.wordCounter)

############################
class WordFinder(FileObserver):
    def __init__(self, wordForSearch):
        self.wordForSearch = wordForSearch
        self.result = False

    # заміщення абстрактного методу
    def onReceive(self, line : str):
        if line.count(self.wordForSearch):
            self.result = True

    def __bool__(self):
        return self.result

############################

if __name__ == '__main__':
    reader = FileReader("input.txt")

    lineprinter = LinesPrinter()
    reader.subscribe(lineprinter)

    linecounter = LinesCounter()
    reader.subscribe(linecounter)

    wordcounter = WordCounter()
    reader.subscribe(wordcounter)

    wordForSearch = "кіл45ькість"
    wordfinder = WordFinder(wordForSearch)
    reader.subscribe(wordfinder)

    reader.read()  # читання файлу по рядках і надсилання
                   # кожного рядка підписнику

    print(f"кількість рядків у файлі = {linecounter}")
    print(f"кількість слів у файлі = {wordcounter}")

    if wordfinder:
        print(f"Слово \"{wordForSearch}\" міститься у файлі")
    else:
        print(f"Слово \"{wordForSearch}\" не міститься у файлі")

