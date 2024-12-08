# TODO Напишите функцию find_common_participants
def find_common_participants(list_1, list_2, symbol=','):
    set_1 = set(list_1.split(symbol))
    set_2 = set(list_2.split(symbol))
    common_list = sorted(list(set_1.intersection(set_2)))
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, symbol='|'))