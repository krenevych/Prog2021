class ProtectedDictIntError(KeyError):

    def __init__(self, message=""):
        self.message = str(message)


class ErrorKeyExist(ProtectedDictIntError):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "Dictionary contains key: " + self.message



class ErrorKeyNotInteger(ProtectedDictIntError):
    def __str__(self):
        return "Key in not integer: " + self.message