class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.year = year
        self.month = month
        self.day = day

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod
    # TODO какой декоратор следует применить?
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        ...  # TODO записать условие проверки високосного года

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  # TODO вернуть количество дней указанного месяца
        if cls.is_leap_year(year):
            new_days = cls.DAY_OF_MONTH[1]
        else:
            new_days = cls.DAY_OF_MONTH[0]
        return new_days[month - 1]

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        ...  # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
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
        return f'Дата: {self._day}/{self._month}/{self._year}'

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError()
        condition_1 = self.is_leap_year(self._year) and day < 1 or day > self.DAY_OF_MONTH[1][self._month - 1]
        condition_2 = not self.is_leap_year(self._year) and day < 1 or day > self.DAY_OF_MONTH[0][self._month - 1]
        if condition_1 or condition_2:
            raise ValueError
        self._day = day

    # TODO записать getter и setter для месяца
    @property
    def month(self):
        return self.month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError()
        if month < 1 or month > 12:
            raise ValueError()
        self._month = month

    # TODO записать getter и setter для года
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError()
        if year < 1:
            raise ValueError()
        self._year = year




if __name__ == '__main__':
    date = Date(30, 12, 2023)
    print(date)
    date.month = 2
    date.day = 28
    print(date)