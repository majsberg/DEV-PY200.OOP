class Figure:
    def __init__(self, name=None):
        self._name = name

    def print_name(self):
        print(self._name)


class Rectangle(Figure):
    def __init__(self, a, b, name=None):
        # TODO вызвать конструктор базового класса с помощью super
        self.a = a
        self.b = b
        super().__init__(name)


if __name__ == "__main__":
    rect = Rectangle(5, 10, 'rect_fig')
    rect.print_name()
    # figure = Figure('Просто Мария + Марина')
    # print(figure._name)
