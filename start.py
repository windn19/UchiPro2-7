class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rectangle_area(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return 3.14 * self.r ** 2


r = Rectangle(5, 6)
c = Circle(4)
print(r.get_rectangle_area())
print(c.get_circle_area())