class Number:
    ALPHABET = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def __init__(self, number, base):
        result = ''
        while number != 0:
            digit = number % base
            if digit >= 10:
                digit = self.ALPHABET[digit]
            result += str(digit)
            number //= base
        self.value = result[::-1]

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'

    def __add__(self, other):
        return self.__class__(self.to_dec() + other.to_dec())

    def __sub__(self, other):
        return self.__class__(self.to_dec() - other.to_dec())

    def __mul__(self, other):
        return self.__class__(self.to_dec() * other.to_dec())

    def __floordiv__(self, other):
        return self.__class__(self.to_dec() // other.to_dec())


class Bin(Number):
    def __init__(self, number):
        super().__init__(number, 2)

    def to_dec(self):
        return int(self.value, 2)


class Oct(Number):
    def __init__(self, number):
        super().__init__(number, 8)

    def to_dec(self):
        return int(self.value, 8)


class Hex(Number):
    def __init__(self, number):
        super().__init__(number, 16)

    def to_dec(self):
        return int(self.value, 16)


h = Hex(167)
print(h)
print(h.to_dec())
b1 = Bin(7)
b2 = Bin(15)
b3 = b2 + b1
print(b3)
print(b3.to_dec())