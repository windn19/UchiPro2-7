class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


# shapes = [Rectangle(5, 6), Circle(4), Square(3)]
# for shape in shapes:
#     print(shape.get_area())
x = 0; y= 5
print(x, y)