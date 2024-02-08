class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):

        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @classmethod
    def is_leap_year(cls, year: int):
        """Проверяет, является ли год високосным"""
        # TODO реализовать метод
        try:
            if year > 0 and year % 4 == 0:
                return cls.DAY_OF_MONTH[1]
            elif year > 0 and year % 4 > 0:
                return cls.DAY_OF_MONTH[0]
        except ValueError:
            print("Такого года не существует")

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        try:
            return cls.is_leap_year(year)[month - 1]
        except ValueError:
            print("Ошибка на этом шаге")

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        # TODO проверить валидность даты
        if day > 0 and day <= cls.get_max_day(month, year):
            return print(f'День :{day}, Месяц :{month}, Год :{year}')
        else:
            return print('Ошибка')

date = Date(33, 2, -100)