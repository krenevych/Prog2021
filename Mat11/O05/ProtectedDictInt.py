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

    def __contains__(self, item):
        return item in self._dict

    def __len__(self):
        # even_count = 0
        # for el in self._dict:
        #     if el % 2 == 0:
        #         even_count += 1
        # return even_count
        return len(self._dict)

if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = 34
    d[22] = 22
    d[15] = 1111
    print(d)

    print(23 in d)
    print(len(d))