"""
ЗАДАНИЕ №1
"""

uzer_time = int((input("Введите количество секунд:")))  # Вводим данные вещественного числа
#  в большую сторону
hour = uzer_time//3600  # Находим целое количество часов
min = (uzer_time - hour*3600)//60  # Находим целое количество минут
sec = uzer_time - hour*3600 - min*60  # Находим количество секунд
print(f"В указанном количестве секунд {uzer_time}:\n"
      f"Часов:{hour}\n"
      f"Минут:{min}\n"
      f"Секунд:{sec}")
"""
ЗАДАНИЕ №2
"""


degrees_celcium = float(input("Введите градусы Цельсия:"))  # Вводим вещественное число
degrees_kelvin = round(degrees_celcium + 273.15, 2)  # Находим Кельвины и округляем результат по правилам математики
degrees_farengeyt = round(degrees_celcium*1.8 + 32, 2)  # Находим Фаренгейт
degrees_reomure = round(degrees_celcium*0.8, 2)  # Находим Реомюре
print(f"В указанном количестве градусов цельсия:{degrees_celcium}:\n"
      f"Градусов Кельвина:{degrees_kelvin}\n"
      f"Градусов Фаренгейта:{degrees_farengeyt}\n"
      f"Градусов Реомюра:{degrees_reomure}")