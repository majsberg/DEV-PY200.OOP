from datetime import datetime, date
import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Flat:
    def __init__(self, square: float, rooms: int, balcony: bool, repair_date: date, residents: dict):
        """
                Создание и подготовка к работе объекта "Квартира"

                :param square: площадь квартиры
                :param rooms: количество комнат
                :param balcony: наличие балкона
                :param repair_date: дата ремонта
                :param residents: жильцы квартиры

        """
        if not isinstance(square, (int, float)):
            raise TypeError('Площадь квартиры должна быть типа int или float')
        if square <= 0:
            raise ValueError('Площадь квартиры должна быть больше нуля')
        self.square = square

        if not isinstance(rooms, int):
            raise TypeError('Количество комнат должно быть типа int')
        if rooms <= 0:
            raise ValueError('Количество комнат должно быть больше нуля')
        self.rooms = rooms

        self.balcony = balcony
        self.repair_date = repair_date
        self.residents = residents

    def make_repair(self) -> datetime:
        """
               Метод, который обновляет дату ремонта в квартире
               :return: дата последнего ремонта
        """
        ...

    def change_residents(self, name: str) -> dict:
        """
                Метод, который меняет состав жильцов в квартире
                :return: возвращает информацию обо всех жильцах
        """
        ...


class PC:
    def __init__(self, name: str, CPU: str, RAM_size: int, SSD_size: int, GPU: str):
        """
                Создание и подготовка к работе объекта "Компьютер"

                :param name: название компьютера
                :param CPU: название процессора
                :param RAM_size: размер оперативной памяти в МБ
                :param SSD_size: размер диска в ГБ
                :param GPU: название видеокарты

        """
        if not isinstance(name, str):
            raise TypeError('Название компьютера должно быть типом str')
        self.name = name

        if not isinstance(CPU, str):
            raise TypeError('Название CPU должно быть типом str')
        self.CPU = CPU

        if not isinstance(RAM_size, int):
            raise TypeError('Размер оперативной памяти должен быть типом int')
        if RAM_size < 1024:
            raise ValueError('Размер оперативной памяти не может быть меньше 1024Мб')
        self.RAM_size = RAM_size

        if not isinstance(SSD_size, int):
            raise TypeError('Размер диска должен быть типом int')
        if SSD_size < 64:
           raise ValueError('Размер диска не может быть меньше 64Гб')
        self.SSD_size = SSD_size

        if not isinstance(GPU, str):
            raise TypeError('Название видеокарты должно быть типом str')
        self.GPU = GPU

    def turn_on(self) -> bool:
        """
                Метод, который включает компьютер
                :return: рабочее состояние компьютера
        """

    def turn_off(self) -> bool:
        """
                Метод, который выключает компьютер
                :return: нерабочее состояние компьютера
        """


class Priceless:
    """
            Создание и подготовка к работе служебного класса для стоимости бесценных объектов
            Необходим для применения в следующем классе, где экземпляр может оказаться "бесценным"
    """
    def __init__(self, priceless: bool = True):
        if priceless:
            self.priceless = True

    def __str__(self):
        if self.priceless:
            return f'{"Бесценна"}'


priceless = Priceless(True)


class Book:
    def __init__(self, name: str, author: str, year: date, ISBN: [str, None], pages: int, price: [float, priceless]):
        """
                Создание и подготовка объекта "Книга"

                :param name: название книги
                :param author: имя автора
                :param year: дата издания
                :param ISBN: номер ISBN
                :param pages: количество страниц
                :param price: цена в рублях с копейками

                """
        if not isinstance(name, str):
            raise TypeError('Название должно быть типом str')
        self.name = name

        if not isinstance(author, str):
            raise TypeError('Автор должен быть типом str')
        self.author = author

        if not isinstance(year, date):
            raise TypeError('Год издания должен быть типом date')
        if year < date(1457, 8, 14):
            raise ValueError('Книга не может быть издана раньше 1457 года')
        self.year = year

        if not isinstance(ISBN, str | None):
            raise TypeError('ISBN должен быть типом str или None')
        self.ISBN = ISBN

        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типом int')
        if pages < 4:
            raise ValueError('Страниц в книге не может быть меньше четырех')
        self.pages = pages

        if not isinstance(price, float | Priceless):
            raise TypeError('Цена должна быть типом float или priceless')
        if type(price) == float and price <= 0:
            raise ValueError('Цена не может быть меньше либо равняться нулю')
        self.price = price

    def take_book(self) -> bool:
        """
                Метод, который позволяет приобрести книгу
                :return: добавляет книгу в список личных книг
        """

    def read_book(self) -> bool:
        """
                Метод, который позволяет читать книгу
                :return: состояние книги
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    flat1 = Flat(30.1, 1, False, date(2011, 11, 11), {1: "Иванов Иван Иванович"})
    print(flat1.square, flat1.rooms, flat1.balcony)

    home_PC = PC('Gaming PC', 'Intel i7', 16384, 512, 'GTX 1080')
    print(home_PC.name, home_PC.CPU, home_PC.RAM_size, home_PC.SSD_size, home_PC.GPU)

    first_book = Book('Библия', 'Иоганн Гутенберг', date(1457, 8, 14), None, 1282, priceless)
    print(first_book.name, first_book.author, first_book.year, first_book.ISBN, first_book.pages, first_book.price.__str__())