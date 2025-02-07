import math

class Point:
    x = 0
    y = 0
    x_1 = 0
    y_1 = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Show (self):
        print(f"({self.x}, {self.y})")
    
    def Move (self, a, b):
        self.x_1 = self.x + a
        self.y_1 = self.y + b
        print(f"({self.x_1}, {self.y_1})")

    def Dist (self):
        self.dist = math.sqrt((self.x - self.x_1) ** 2 + (self.y - self.y_1) ** 2)
        print(self.dist)

coord = Point(3, 5)
coord.Show()

new_point = Point(3, 5)
new_point.Move(4, -1)


dist = Point(3, 5)
dist.Dist()


