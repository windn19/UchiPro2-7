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


shapes = [Rectangle(5, 6), Circle(4)]
for shape in shapes:
    if isinstance(shape, Rectangle):
        print(shape.get_rectangle_area())
    elif isinstance(shape, Circle):
        print(shape.get_circle_area())
