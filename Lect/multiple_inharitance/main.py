class Xerox:
    ...
    def copy(self, original):
        print(f"Xerox: Make a copy from {original}")

class Scaner:
    ...
    def copy(self):
        print("Scaner: Make a copy")

class MFD(Scaner, Xerox):

    def copy(self):
        print("MFD: Make a copy")
        Xerox.copy(self)

    pass

if __name__ == '__main__':
    m = MFD()
    m.copy()