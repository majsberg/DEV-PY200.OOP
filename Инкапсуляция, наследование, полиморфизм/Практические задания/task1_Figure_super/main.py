class Figure:
    def __init__(self, name='Общее название'):
        self._name = name

    def print_name(self):
        print(self._name)


class Rectangle(Figure):
    def __init__(self, a, b):
        # TODO вызвать конструктор базового класса с помощью super
        super().__init__()
        self.a = a
        self.b = b


if __name__ == "__main__":
    figure = Figure('Просто Мария + Марина')
    figure.print_name()
    rect = Rectangle(5, 10)
    rect.print_name()

