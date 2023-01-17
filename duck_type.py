class Duck:
    def quack(self):
        print("Кряяяяя!")

    def feathers(self):
        print("У утки есть белые и серые перья")


class Person:
    def quack(self):
        print("Человек имитирует кряканье утки")

    def feathers(self):
        print("Человек берет перья с земли и показывает их")

    def name(self):
        print("Иван Иванов")


def in_the_forest(obj):
    obj.quack()
    obj.feathers()


donald = Duck()
john = Person()
in_the_forest(donald)
in_the_forest(john)