# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume = 1.44 # информационный объем дискеты
number_of_pages = 100 # количество страниц в книге
number_of_str = 50 # число строк на странице
number_of_symbols = 25 # количество символов в стркое
one_volume_of_symbol = 4 # количество байтов для одного символа

volume_of_symbols_in_one_str = one_volume_of_symbol * number_of_symbols
volume_of_symbols_in_one_page = volume_of_symbols_in_one_str * number_of_str
volume_of_symbols_in_one_book = volume_of_symbols_in_one_page * number_of_pages
book_volume = disk_volume * 1024 * 1024 / volume_of_symbols_in_one_book

print("Количество книг, помещающихся на дискету:", round(book_volume))
