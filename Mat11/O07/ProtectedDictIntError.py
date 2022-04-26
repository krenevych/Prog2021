class ProtectedDictIntError(KeyError):

    ErrorKeyNotInteger = 0
    ErrorKeyExist = 1

    def __init__(self, errorCode, message=""):
        self.errorCode = errorCode
        self.message = str(message)

    def __str__(self):
        if self.errorCode == ProtectedDictIntError.ErrorKeyNotInteger:
            return "Key in not integer: " + self.message
        elif self.errorCode == ProtectedDictIntError.ErrorKeyExist:
            return "Dictionary contains key: " + self.message