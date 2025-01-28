class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация атрибутов книги
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self):
        """
        Метод для представления книги в виде строки
        :return: Строка с названием книги
        """
        return f'Книга "{self.name}"'
    def __repr__(self):
        """
        Метод для представления книги в виде валидной строки Python
        :return: Строка для инициализации точно такого же экземпляра
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
# База данных книг
BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# Создание экземпляров книг из базы данных
books = [Book(book_data["id_"], book_data["name"], book_data["pages"]) for book_data in BOOKS_DATABASE]

# Вывод информации о книгах
for book in books:
    print(book)  # Вывод: Книга "test_name_1", затем Книга "test_name_2"
output = []
for book_data in BOOKS_DATABASE:
    book = Book(book_data["id_"], book_data["name"], book_data["pages"])
    output.append(repr(book))
print(f"[{', '.join(output)}]")