import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    ...  # TODO определить конструктор и перегрузить метод area

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return(self.a * self.b)

class Circle(Figure):
    """ Производный класс. Круг. """

    ...  # TODO определить конструктор и перегрузить метод area
    def __init__(self, r):
        if not isinstance(r, (int, float)):
            raise TypeError('Тип должен быть int или float')
        if r <= 0:
            raise ValueError('Значение должно быть больше 0')
        self.r = r

    def area(self):
        super().area()
        return(self.r ** 2 * math.pi)


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
