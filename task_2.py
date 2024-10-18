# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
pages = 100
lines = 50
letters = 25
one = 4
volume_in_bites = volume*1024*1024
letters_in_whole_book = letters * lines * pages
memory = letters_in_whole_book * one
result = (volume_in_bites) // memory
results1 = int(result)
print("Количество книг, помещающихся на дискету:", results1)
