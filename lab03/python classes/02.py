class Shape:
    length = 0

    def __init__(self):
        self.length = 0

    def printArea(self): 
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def printArea(self):
        print(self.length * self.length)



square = Square(4)
square.printArea()
