class MyClass:
    def __init__(self):
        self.string = ''
    def getString(self):
        self.string = input("Input text ")

    def printString(self):
        print(self.string.upper())

ob = MyClass()
ob.getString()
ob.printString()