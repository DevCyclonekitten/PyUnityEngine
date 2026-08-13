class MyClass():
    def __init__(self):
        self.value = 5
    def FunctionA(self):
        self.value *= 2


a = MyClass()
a.value = 7
a.FunctionA()


b= MyClass()
b.value = 9

print(b.value)
print(a.value)
