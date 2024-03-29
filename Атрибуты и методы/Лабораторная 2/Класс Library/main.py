BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        if not isinstance(id_, int):
            raise TypeError('Id должен быть типом int')
        if id_ <= 0:
            raise ValueError('Id должен быть больше нуля')
        self.id = id_

        if not isinstance(name, str):
            raise TypeError('Name должен быть типом str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Pages должен быть типом int')
        if pages <= 0:
            raise ValueError('Pages должен быть больше нуля')
        self.pages = pages


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None):
        if books:
            self.books = books
        else:
            self.books = []

    def get_next_book_id(self):
        if not self.books:
            return 1
        list_ = []
        for each in self.books:
            list_.append(each.id)
        return max(list_) + 1

    def get_index_by_book_id(self, id_):
        for i, each in enumerate(self.books):
            if each.id == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
