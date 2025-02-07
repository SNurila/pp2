class Shape:
    length = 0
    def __init__(self):
        self.length = 0
    def printArea(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def printArea(self):
        print(self.length * self.width)

rec_area = Rectangle(12, 13)
rec_area.printArea()