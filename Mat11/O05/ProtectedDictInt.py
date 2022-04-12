class ProtectedDictInt:
    def __init__(self):
        self._dict = {}

    def __setitem__(self, key, value):
        if type(key) != int:
            raise KeyError("Key in not integer")
        if key in self._dict:
            raise KeyError("Dictionary contains key")
        self._dict[key] = value

    def __getitem__(self, item):
        return self._dict[item]

    def __str__(self):
        return str(self._dict)

if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = 34
    # d[23] = 222
    # d["hello"] = "hello"
    print(d[23])
    # print(d)

    # d1 = {}
    # d1[23] = 34
    # d1[34] = "Hello!"
    # d1[23] = 222  # !!!Error
    # # d1["hello"] = "Hello" #!!!Error
    # print(d1)