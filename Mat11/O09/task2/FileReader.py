from Mat11.O09.task2.FileObserver import FileObserver


class FileReader:

    def __init__(self, filename):
        self.filename = filename
        self.subscribers = []  # список підписників

    def notifySubscribers(self, line):
        for subscriber in self.subscribers:
            subscriber.onReceive(line)

    def read(self):
        with open(self.filename, encoding="utf-8") as file:
            for line in file:
                self.notifySubscribers(line)

    def subscribe(self, subscriber: FileObserver):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber : FileObserver):
        self.subscribers.remove(subscriber)



if __name__ == '__main__':
    reader = FileReader("input.txt")
    reader.read()