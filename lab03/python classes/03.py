class Shape():
    def __init__(self):
        self.area_value = 0
    def area(self):
        print(self.area)

class Rectangle(Shape):
    def area(self, length, width):
        self.area = self.length * self.width
        print(self.area)

rec_area = Rectangle(12, 13)
rec_area.area()