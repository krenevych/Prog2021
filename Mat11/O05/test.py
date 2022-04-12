# микола = лікар()
# isinstance(микола, лікар)
# клас хірург(лікар)...
# іван = хірург()...
# isinstance(іван, лікар)
# type(іван) == лікар\

class MyInt(int):
    pass

mi = MyInt(10)

print(type(mi))
print(type(mi) == int)
print(isinstance(mi, int))

pass