class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str) -> object:
        if not isinstance(name, str):
            raise TypeError('Название должно быть типом str')
        self.__name = name
        if not isinstance(author, str):
            raise TypeError('Автор должен быть типом str')
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):      # def__init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типом int')
        if pages < 3:
            raise ValueError('Количество страниц должно быть не меньше четырех')
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        self.__pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: [int, float]):
        super().__init__(name, author)
        if not isinstance(duration, int or float):
            raise TypeError('Продолжительность должна быть типом int или float')
        if duration < 1:
            raise ValueError('Продолжительность не может быть меньше 1 часа')
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"


if __name__ == '__main__':

    p_book = PaperBook('Молодой негодяй', 'Лимонов', 500)
    print(p_book.__repr__())
    print(p_book)
    p_book.pages = 400
    print(p_book)

    a_book = AudioBook('Молодой негодяй', 'Лимонов', 9)
    print(a_book.__repr__())
    print(a_book)
    a_book.duration = 8.5
    print(a_book)