
def find_common_participants(str1,str2,divider=','):
    str11 = str1.split(divider)
    str21 = str2.split(divider)
    common_names = list(set(str11).intersection(str21))
    common_names.sort()
    return common_names


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, divider='|'))