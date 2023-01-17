class Number:
    def __init__(self, number, word):
        alias = {'Bin': bin,
                 'Oct': oct,
                 'Hex': hex}
        self.func = word
        if word in alias.keys():
            self.value = alias[word](number)[2:]
        else:
            self.value = 'Неправильная система исчисления'

    def __str__(self):
        return f'{self.func.capitalize()}: {self.value.upper()}'


print(bin(65-59))
print(oct(65-59))
print(hex(65-59))
# n1 = 65
# n2 = 59
# n = 'Hex'
# print(Number(n1 + n2, n))
# print(Number(n1 - n2, n))
# print(Number(n1 * n2, n))
# print(Number(n1 // n2, n))