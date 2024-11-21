numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers1 = [x for x in numbers if x is not None]
unique_numbers = set(numbers1)
sum_numbers = sum(unique_numbers)
count_numbers = len(numbers1)+1 #тк в новом списке нет none
average = sum_numbers / count_numbers
numbers = [average if x == None else x for x in numbers]

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)