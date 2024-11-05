class Book:
    def __init__(self, pages=None, author=None, price=None):
        self.__pages = pages
        self.__author = author
        self.price = price

    def get_pages(self):
        return self.__pages

    def get_author(self):
        return self.__author

    def __repr__(self):
        return (f'Кількість сторінок: {self.__pages} '
                f'\nАвтор: {self.__author} '
                f'\nЦіна: {self.price} грн\n')

    def __del__(self):
        print(f"{self.__str__()}")


def main():
    book1 = Book(300, 'Тарас Шевченко', 120)
    book2 = Book(250, 'Ліна Костенко', 200)
    book3 = Book(500, 'Леся Українка', 150)

    books = [book1, book2, book3]

    for book in books:
        print(repr(book))


main()

