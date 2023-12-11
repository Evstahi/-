numb_of_pages = 100
numb_of_lines = 50
numb_of_symbols = 25
weight_of_symbol = 4
size_of_disk = 1.44
size_of_book = numb_of_pages*(numb_of_lines*(numb_of_symbols*weight_of_symbol))
mb_of_book = size_of_book/(1024**2)
number_of_books = size_of_disk // mb_of_book

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(number_of_books))
