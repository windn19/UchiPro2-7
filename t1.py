import math


class Shape:
    def __str__(self):
        return self.__class__.__name__


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(math.pi * self.r ** 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.r)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def get_perimeter(self):
        return self.a + self.b + self.c


class RightTriangle(Triangle, Shape):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a ** 2 + b ** 2))

    def get_area(self):
        return self.a * self.b / 2


# tr = RightTriangle(3, 4)
# print(tr)
# print(tr.get_area())
# print(tr.get_perimeter())
name = input()
match name:
    case 'Rectangle':
        a, b = map(int, input().split())
        shape = Rectangle(a, b)
    case 'Circle':
        r = int(input())
        shape = Circle(r)
    case 'Triangle':
        a, b, c = map(int, input().split())
        shape = Triangle(a, b, c)
    case 'RightTriangle':
        a, b = map(int, input().split())
        shape = RightTriangle(a, b)
    case _:
        print('Введено неправильное название')
        exit(10)
print(shape)
print(round(shape.get_area()))
print(round(shape.get_perimeter()))