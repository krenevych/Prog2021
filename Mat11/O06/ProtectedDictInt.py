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

    def __add__(self, other):
        if isinstance(other, ProtectedDictInt):
            res = ProtectedDictInt()
            for key, val in self._dict.items():
                res[key] = val
            for key, val in other._dict.items():
                res[key] = val
            return res
        elif isinstance(other, tuple) and len(other) == 2:
            res = ProtectedDictInt()
            for key, val in self._dict.items():
                res[key] = val
            res[other[0]] = other[1]
            return res
        else:
            raise ArithmeticError("Operation is not supported!")

    def __sub__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Operation is not supported!")

        res = ProtectedDictInt()
        for key, val in self._dict.items():
            if key != other:
                res[key] = val
        return res

    def __iter__(self):
        return ProtectedDictIntIncreasingIterator(self._dict.keys())
        # return iter(self._dict)


class ProtectedDictIntIncreasingIterator:
    def __init__(self, collection):
        self.keys = list(collection)
        self.keys.sort()
        self.marker = 0

    def __next__(self):
        # if self.marker >= len(self.keys):
        #     raise StopIteration
        try:
            res = self.keys[self.marker]
            self.marker += 1
            return res
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = 34
    d[22] = 22
    d[15] = 1111
    d[17] = 12311

    for key in d:
        print(key)
    # my_iterator = iter(d)
    # key = next(my_iterator)
    # print(key)
    # key = next(my_iterator)
    # print(key)
    # key = next(my_iterator)
    # print(key)
    # key = next(my_iterator)
    # print(key)

