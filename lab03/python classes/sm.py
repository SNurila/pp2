import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def len_circle(self):
        self.len_circle = math.pi * 2 * self.radius
        print(f"{self.len_circle:.2f}")

circle = Circle(4)
circle.len_circle()