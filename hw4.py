"""
Задача 1

"""

phone_number = input("Введите номер телефона:")  # Берем данные у пользователя
phone_number_changed = ((phone_number.replace(' ', '').replace('+','')  # Убираем лишние знаки
                        .replace('(','')).replace(')','')  # для проверки
                        .replace('-',''))
phone_number_changed_plus = ((phone_number.replace(' ', '')  # Убираем лишние знаки
                        .replace('(','')).replace(')','')  # для проверки
                        .replace('-',''))
len_number = len(phone_number_changed)  # Измеряем длинну номера телефона
if len_number != 11:  # Решил сделать два условия на False. Проверяем равна ли длина 11 символов
    print(f"Длина вашего номера: {phone_number} - является недопустимой! ")
else:
    print(f"Длина номера: {phone_number} - совпадает с необходимой!")

if not phone_number_changed.isdigit():  # Проверяем содержит ли только символы номер телефона
    print(f"Кроме цифр вы написали что-то еще. Это недопустимо!")
else:
    print(f"Номер: {phone_number} - состоит только из цифр!")

if phone_number_changed_plus[0] == "8" or phone_number_changed_plus[0:2] == "+7":
    print(f"Номер {phone_number} начинается правильно!")
else:
    print(f"Номер {phone_number} не начинается на 8 или +7")

"""
Задача 2

"""

uzer_password = input("Введите пароль:")
len_password = len(uzer_password)  # Измеряем длину пароля
if uzer_password.count(" ") > 0:  # Проверяем, содержит ли 0
    print(f"Ваш пароль: {uzer_password} - содержит пробел. Пожалуйста, напишите пароль без пробела.")

if  len_password < 7:  # Проверяем, длиннее ли 7 символов пароль
    print(f"Ваш пароль: {uzer_password} - слишком короткий.")

if uzer_password.islower() or uzer_password.isupper():  # Проверяем, содержит ли только большие или только маленькие буквы
    print(f"Ваш пароль: {uzer_password} - состоит только из маленьких или больших букв.")

if uzer_password.isalnum():  # Проверяем состоит ли только из цифр и буквы
    print(f"Ваш пароль: {uzer_password} - не достаточно надежный! Введите спецзнак!")
if (not uzer_password.isalnum() and not (uzer_password.islower() or uzer_password.isupper()) and
        not len_password < 7 and not uzer_password.count(" ") > 0):
    print(f"Ваш пароль: {uzer_password} - надежный!")