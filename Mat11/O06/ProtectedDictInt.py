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



if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = 34
    d[22] = 22
    d[15] = 1111
    # print(d)
    # print(23 in d)
    # print(len(d))

    # d2 = ProtectedDictInt()
    # d2[55] = 45
    # d2[65] = 65
    # # d2[15] = 222
    # d3 = d + d2
    # print(d3)

    d1 = d + (55, 199)
    # d1 = d + ("23", 199)
    print(d1)

    d3 = d1 - 55
    # d3 = d - '55'
    print(d3)

