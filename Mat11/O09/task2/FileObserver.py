from abc import ABCMeta, abstractmethod

# інтерфейс - абстрактний клас,
# що не містить даних, і всі методи не мають реалізації
# та повинні бути заміщеними у нащадках
class FileObserver(metaclass=ABCMeta):

    # - метод, що немає реалізації та має бути заміщений
    # у нащадку
    @abstractmethod
    def onReceive(self, line : str):
        pass


if __name__ == '__main__':
    # fo = FileObserver()
    pass