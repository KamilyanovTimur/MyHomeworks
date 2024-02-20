# 1.
from pprint import pprint

from marvel import full_dict
# 2.
user_input_number = input("Введите пожалуйста цифры через пробел: ")
input_number_list = user_input_number.split(" ")
number_map = list(map(lambda number: int(number) if (number.isdigit()) else None, input_number_list))
print(f'Второе задание {number_map}')
# 3
full_dict_id = [{'id': id_film, **film} for id_film, film in full_dict.items()]
input_id = list(filter(lambda film: film if (film["id"] in number_map) else None, full_dict_id))
pprint(f'Третье задание {input_id}')
# 4
director_set = {film['director'] for film in full_dict.values()}
pprint(f'Четвертое задание {director_set}')
# 5
full_dict_copy = full_dict.copy()

full_dict_copy = {key:{str(v) if k == "year" else v for k,v in value.items()} for key, value in full_dict_copy.items()}
pprint(f'Пятое задание {full_dict_copy}')
# 6
marvel_list = [film for film in full_dict.values()]
films_ch = list(filter(lambda film: film if (film['title'] != None and film['title'].lower().startswith("ч"))else None, marvel_list))
pprint(films_ch, sort_dicts=False)
# 7 Возвращает словарь, с сортированными ключами по возрастанию
sorted_dict = dict(sorted(full_dict.items(), key=lambda x: x[0]))
pprint(sorted_dict, sort_dicts=False)
# 8 Возвращает словарь словарей, с сортировкой по ключу в обратном порядке
sorted_dict = dict(sorted(full_dict.items(), key=lambda x: x[0], reverse = True))
pprint(sorted_dict, sort_dicts=False)
# Как sort_dicts писать в f строке я не знаю, поэтому без красивого принта

