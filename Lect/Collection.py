class Collection:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def __setitem__(self, key, value):
        try:
            self.elements[key] = value
        except IndexError:
            self.elements.append(value)

    def __getitem__(self, item):
        return self.elements[item]

    def __len__(self):
        return len(self.elements)

    def __delitem__(self, key):
        self.elements.pop(key)

if __name__ == "__main__":
    col = Collection()
    # col.__setitem__(1, 1)
    col[1] = 1
    col[2] = 2 # col.__setitem__(2, 2)
    col[3] = 3    # col.__setitem__(3, 3)
    print(col)

    del col[1]
    print(col)



