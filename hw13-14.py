"""
Игра в города с компьютером
"""

import json
CITIES = 'cities.json'
COUNT = 0
# from data.cities import cities_list
# cities_set = set()
# for city_dict in cities_list:
#     cities_set.add(city_dict["name"])
# # for city_str in list(cities_set):
# #     if city_str[-1] == "ь" or city_str[-1] == "ы":
# #         cities_set.remove(city_str)
# with open('cities.json', 'w', encoding='utf-8') as cities_file_json:
#     json.dump(list(cities_set), cities_file_json, ensure_ascii=False, indent=4)
def load_set_cities_from_json_file(cities: str = CITIES) -> set:
    """
    Функция принимает JSON строку и возвращает сет городов
    :param cities:
    :return: cities_json
    """
    with open('../../lesson15/hw15/cities.json', 'r', encoding='utf-8') as cities_file_json:
        cities_json = set(json.load(cities_file_json))
        return cities_json
def save_bad_letters(cities_set: set) -> set:
    """
    Функция принимает сет городов и возвращает сет с "плохими" буквами
    :param cities_set:
    :return: bad_letters_set_for_func
    """
    unique_letters_set = set(''.join(cities_set).lower())
    bad_letters_set_for_func = set()
    for letter in unique_letters_set:
        for city in cities_set:
            if letter == city[0].lower():
                break
        else:
            bad_letters_set_for_func.add(letter)
    return bad_letters_set_for_func
def computer_runing(cities_set: set, bad_letters_set: set) -> None:
    """
    Функция описывает ход компьютера
    :return: None
    """
    for city in cities_set:
        if city[0].lower() == user_input[-1].lower():
            if city[-1].lower() not in bad_letters_set:
                print(f'Компьютер: {city}')
                last_city.insert(0, city)
                cities_set.remove(city)
                global COUNT
                COUNT += 1
                break
            else:
                continue
    else:
        result_message("Поздравляю, Вы выиграли!")
def result_message(result: str) -> None:
    """
    Функция принимает строку в виде сообщения, которое нужно вывести и возвращает это сообщение. Добавил сюда Bool_flag,
    чтобы сэкономить место
    :param result:
    :return: None
    """
    if result == "Поздравляю, Вы выиграли!":
        print("Поздравляю, Вы выиграли!")
        bool_flag = False
    elif result == "Ваше слово не начинается на последнюю букву предыдущего! Вы проиграли! ":
        print("Ваше слово не начинается на последнюю букву предыдущего! Вы проиграли! ")
        bool_flag = False
    elif result == "Вы проиграли!Ваш город не в списке правильно-оканчивающихся городов РФ":
        print("Вы проиграли!Ваш город не в списке правильно-оканчивающихся городов РФ")
        bool_flag = False
    elif result == 'Вы проиграли, город не должен оканчиваться на "ь" или "ы" ':
        print('Вы проиграли, город не должен оканчиваться на "ь" или "ы" ')
        bool_flag = False
    elif result == "Вы проиграли!":
        print("Вы проиграли!")
        bool_flag = False
def main():
    """
    Точка входа в программу
    :return: None
    """
    global last_city
    last_city = []
    bool_flag = True
    print("---====ИГРА В ГОРОДА====---")
    print('Напишите любой город РФ. Город не должен оканчиваться на "ь" или "ы" ')
    print('Напишите "стоп" для остановки')
    cities_set = load_set_cities_from_json_file(cities=CITIES)
    bad_letters_set = save_bad_letters(cities_set)
    while bool_flag:
        global user_input
        user_input = input('Вы: ')
        if user_input.lower() != "стоп":
            if user_input[-1] not in bad_letters_set:
                if user_input.title() in cities_set:
                    cities_set.remove(user_input.title())
                    if COUNT == 0:
                        computer_runing(cities_set, bad_letters_set)

                    elif COUNT > 0 and last_city[0][-1].lower() == user_input[0].lower():
                        last_city.clear()
                        computer_runing(cities_set, bad_letters_set)
                    elif COUNT > 0 and last_city[0][-1].lower() != user_input[0].lower():
                        result_message("Ваше слово не начинается на последнюю букву предыдущего! Вы проиграли! ")
                        break
                else:
                    result_message("Вы проиграли!Ваш город не в списке правильно-оканчивающихся городов РФ")
                    break
            else:
                result_message('Вы проиграли, город не должен оканчиваться на "ь" или "ы" ')
                break
        else:
            result_message("Вы проиграли!")
            break

if __name__ == '__main__':
    main()