class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError("Key in not integer")
        if key in self:
            raise KeyError("Dictionary contains key")
        super().__setitem__(key, value)

if __name__ == '__main__':
    d = ProtectedDictInt()
    d[23] = 34
    d[22] = 22
    d[15] = 1111
    print(d)

    print(23 in d)
    print(len(d))
