"""
Игра в города с компьютером
"""
from data.cities import cities_list
cities_set = set()
for city_dict in cities_list:
    cities_set.add(city_dict["name"])
for city_str in list(cities_set):
    if city_str[-1] == "ь" or city_str[-1] == "ы":
        cities_set.remove(city_str)
last_city = []
bool_flag = True
count = 0
print("---====ИГРА В ГОРОДА====---")
print('Напишите "стоп" для остановки')
while bool:
    user_input = input('Введите пожалуйста город, который не заканчивается на "ь", "ы" :')
    if user_input.lower() != "стоп":
        if user_input.title() in cities_set:
            cities_set.remove(user_input.title())
            if count == 0:
                for city in cities_set:
                    if city[0].lower() == user_input[-1].lower():
                        print(f'Компьютер: {city}')
                        last_city.append(city)
                        cities_set.remove(city)
                        count += 1
                        break
            elif count > 0 and last_city[0][-1].lower() == user_input[0].lower():
                last_city.clear()
                for city in cities_set:
                    if city[0].lower() == user_input[-1].lower():
                        last_city.insert(0, city)
                        print(f'Компьютер: {city}')
                        cities_set.remove(city)
                        break
                else:
                    print("Поздравляю, Вы выиграли!")
                    bool_flag = False
                    break
            elif count > 0 and last_city[0][-1].lower() != user_input[0].lower():
                print(f"Ваше слово {user_input} не начинается на последнюю букву предыдущего! Вы проиграли! ")
                bool_flag = False
                break
        else:
            print("Вы проиграли!Ваш город не в списке правильно-оканчивающихся городов РФ")
            bool_flag = False
            break
    else:
        print("Вы проиграли!")
        bool_flag = False
        break







