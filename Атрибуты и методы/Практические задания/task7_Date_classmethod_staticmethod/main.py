class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.is_valid_date(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        # TODO реализовать метод
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году
        if cls.is_leap_year(year):
            new_days = cls.DAY_OF_MONTH[1]
        else:
            new_days = cls.DAY_OF_MONTH[0]
        return new_days[month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        # TODO проверить валидность даты
        if not isinstance(day, int):
            raise TypeError('')
        if not isinstance(month, int):
            raise TypeError('')
        if not isinstance(year, int):
            raise TypeError('')
        if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError('Значения выходят за границу допустимого диапазона')
        max_day = self.get_max_day(month, year)
        if day > max_day:
            raise ValueError(f'В месяце не может быть больше {max_day}')

    def __str__(self):
        return f'Дата: {self.day}/{self.month}/{self.year}'


if __name__ == '__main__':
    date = Date(29, 2, 2024)
    print(date)