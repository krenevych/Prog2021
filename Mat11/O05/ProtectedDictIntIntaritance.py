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
    # d[23] = 222
    d["hello"] = "hello"
    print(d[23])
    print(d)
    print(len(d))

    # d1 = {}
    # d1[23] = 34
    # d1[34] = "Hello!"
    # d1[23] = 222  # !!!Error
    # # d1["hello"] = "Hello" #!!!Error
    # print(d1)