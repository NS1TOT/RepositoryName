
class Notebook:
    def __init__(self, num_pages: int, current_page: int):
        """
        Создание и подготовка к работе объекта "Блокнот"

        :param num_pages: Количество страниц в блокноте
        :param current_page: Текущая страница, на которой находится пользователь
        """
        if not isinstance(num_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if num_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.num_pages = num_pages

        if not isinstance(current_page, int):
            raise TypeError("Текущая страница должна быть целым числом")
        if current_page < 1 or current_page > num_pages:
            raise ValueError("Текущая страница должна быть в пределах от 1 до количества страниц")
        self.current_page = current_page

    def turn_to_page(self, page_number: int) -> None:
        """
        Переход к указанной странице
        :param page_number: Номер страницы, на которую нужно перейти
        Примеры:
        >>> notebook = Notebook(100, 1)
        >>> notebook.turn_to_page(50)
        """
        ...

    def write_on_page(self, text: str) -> None:
        """
        Запись текста на текущей странице
        :param text: Текст для записи
        Примеры:
        >>> notebook = Notebook(100, 1)
        >>> notebook.write_on_page("Hello, World!")
        """
        ...
    def tear_out_page(self) -> None:
        """
        Вырвать текущую страницу из блокнота
        Примеры:
        >>> notebook = Notebook(100, 1)
        >>> notebook.tear_out_page()
        """
        ...

    def get_current_page_number(self) -> int:
        """
        Получить номер текущей страницы
        :return: Номер текущей страницы
        Примеры:
        >>> notebook = Notebook(100, 1)
        >>> notebook.get_current_page_number()
        """
        ...
if __name__ == "__main__":
    import doctest
    doctest.testmod()