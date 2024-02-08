from typing import Union

class Calculator:

    @staticmethod  # TODO написать статические методы
    def add(a: Union[int, float], b: Union[int, float]):
        if not isinstance(a, (int, float)):
            raise TypeError('Аргумент a должен быть int или float')
        if not isinstance(b, (int, float)):
            raise TypeError('Аргумент b должен быть int или float')
        return a + b

    @staticmethod
    def mul(a: Union[int, float], b: Union[int, float]):
        if not isinstance(a, (int, float)):
            raise TypeError('Аргумент a должен быть int или float')
        if not isinstance(b, (int, float)):
            raise TypeError('Аргумент b должен быть int или float')
        return a * b

    @staticmethod
    def add_(*args, **kwargs):
        sum_ = 0
        if args:
            for el in args:
                check_arg(el)
                sum_ += el
        if kwargs:
            for el in kwargs.values():
                check_arg(el)
                sum_ += el
        return sum_


def check_arg(a):
    if not isinstance(a, (int, float)):
        raise ('Аргумент должен быть int или float')


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30

    print(Calculator.add_(5,5,6))
