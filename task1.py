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
        return round(3.14 * self.r ** 2)

    def get_perimeter(self):
        return round(2 * 3.14 * self.r)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)

    def get_perimeter(self):
        return self.a + self.b + self.c


class RightTriangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return round(self.a * self.b / 2)

    def get_perimeter(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return round(self.a + self.b + c)


s = input()
if s == 'Rectangle':
    a, b = map(int, input().split())
    shape = Rectangle(a, b)
elif s == 'Circle':
    r = int(input())
    shape = Circle(r)
elif s == 'Triangle':
    a, b, c = map(int, input().split())
    shape = Triangle(a, b, c)
else:
    a, b = map(int, input().split())
    shape = RightTriangle(a, b)

print(shape)
print(shape.get_area())
print(shape.get_perimeter())
