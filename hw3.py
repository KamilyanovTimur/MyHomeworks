"""
Проверка на Палиндром
"""

uzer_input = input("Введите слово или строку:")
uzer_input_lower = uzer_input.lower().replace(' ', '')  # Приведение строки к нижнему регистру и удаление пробелов
uzer_input_lower_reverse = uzer_input_lower[slice(None, None,-1)]  #  Делаем чтобы строка читалась наоборот
if uzer_input_lower == uzer_input_lower_reverse:
    print(f'Поздравляю! "{uzer_input}" - палиндром!')
else:
    print(f'Увы, "{uzer_input}" - не палиндром!')