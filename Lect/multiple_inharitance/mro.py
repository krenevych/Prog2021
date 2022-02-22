class Class4(object): pass
class Class5:
    pass
class Class6:
    def method(self): print("Hello 6!")
class Class2(Class4, Class5): pass
class Class3(Class6):
    def method(self): print("Hello 3!")
class Class1(Class2, Class3):
    """ Class1 клас, що успадкований від класів Class2, Class3

    Ось такі справи
    """
    pass

print(Class1.__name__)
print(Class1.__dict__)

pass







