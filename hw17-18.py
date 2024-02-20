"""
Задание 1
"""
from typing import Callable, Any
import csv

user_password: str = input("Введите пароль: ")
def password_checker(func: Callable) -> Callable:
    """
    Функция принимает ссылку на функцию и возвращает ссылку на функцию
    :param func: Callable
    :return: func: Callable
    """
    def wrapper(*args: str) -> Callable:
        """
        Функция принимает аргументы и возввращает ссылку на функцию
        :param args: str
        :return: func: Callable
        """
        digit_count: int = 0
        upper_count: int = 0
        lower_count: int = 0
        special_simbol: int = 0
        if len(user_password) < 8:
            raise ValueError(f'Пароль {user_password} меньше 8 символов !')
        for user_symbol in user_password:
            if user_symbol.isdigit():
                digit_count += 1
        if digit_count < 1:
            raise ValueError(f"В вашем пароле {user_password} цифр меньше 1 !")
        for user_symbol in user_password:
            if user_symbol.isupper():
                upper_count += 1
        if upper_count < 1:
            raise ValueError(f"В вашем пароле {user_password} больших букв меньше 1 !")
        for user_symbol in user_password:
            if user_symbol.islower():
                lower_count += 1
        if lower_count < 1:
            raise ValueError(f"В вашем пароле {user_password} маленьких букв меньше 1 !")
        for user_symbol in user_password:
            if not user_symbol.isalnum():
                special_simbol += 1
        if special_simbol < 1:
            raise ValueError(f"В вашем пароле {user_password} специальных символов меньше 1!")
        result = func(*args)
        return result
    return wrapper

@password_checker
def register_user(user_password: str) -> None:
    """
    Функция принимает один аргумент и возвращает ничего
    :param user_password:
    :return: None
    """
    print("Пароль прошел проверку!")
register_user(user_password)

"""
Задание 2
"""
username_input: str = input("Введите имя пользователя: ")
password_input: str = input("Введите пароль: ")
def password_validator(length: int = 8, digit: int = 1, uppercase: int = 1, lowercase: int = 1,
                               special_chars: int = 1) -> Callable:
    """"
    Функция принимает параметры и возвращает ссылку на функцию
    :param: params
    :return:Сallable
    """
    def password_checker(func: Callable) -> Callable:
        """
        Функция принимает ссылку на функцию и возвращает ссылку на функцию
        :param func: Callable
        :return: func: Callable
        """
        def wrapper(username_input:str, password_input:str) -> Callable:
            """
            Функция принимает аргументы и возввращает ссылку на функцию
            :param username_input: str, password_input: str
            :return: func: Callable
            """
            digit_count: int = 0
            upper_count: int = 0
            lower_count: int = 0
            special_simbol: int = 0
            if len(user_password) < length:
                raise ValueError(f'Пароль {password_input} меньше {length}!')
            for user_symbol in password_input:
                if user_symbol.isdigit():
                    digit_count += 1
            if digit_count < digit:
                raise ValueError(f"В вашем пароле {password_input} цифр меньше {digit}!")
            for user_symbol in password_input:
                if user_symbol.isupper():
                    upper_count += 1
            if upper_count < uppercase:
                raise ValueError(f"В вашем пароле {password_input} больших букв меньше {uppercase}!")
            for user_symbol in password_input:
                if user_symbol.islower():
                    lower_count += 1
            if lower_count < lowercase:
                raise ValueError(f"В вашем пароле {password_input} маленьких букв меньше {lowercase}!")
            for user_symbol in password_input:
                if not user_symbol.isalnum():
                    special_simbol += 1
            if special_simbol < special_chars:
                raise ValueError(f"В вашем пароле {password_input} специальных символов меньше {special_chars}!")
            return func(username_input, password_input)
        return wrapper

    return password_checker

def username_validator(func: Callable) -> Callable:
    """
    Функция принимает ссылку на функцию и возвращает ссылку на функцию
    :param func: Calleble
    :return: Callabe
    """
    def wrapper(username_input:str, password_input: str) -> Callable:
        """
        Функция принимает строку, возвращает ссылку на функцию
        :param username_input:
        :return: Callable
        """
        if username_input.count(" ") > 0:
            raise ValueError(f"В вашем имени пользователя {username_input} есть пробел!")
        else:
            return func(username_input, password_input)

    return wrapper
@password_validator(length=8, digit=1, uppercase=1, lowercase=1, special_chars=1)
@username_validator
def register_user_for_csv(username_input: str, password_input: str) -> None:
    """
    Функция принимает 2 аргумента и записывает их в csv файл. Возвращает ничего
    :param username_input: str
    :param password_input:  str
    :return: None
    """
    with open("login_password.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username_input, password_input])
    print("Регистрация прошла успешно!")
# register_user_for_csv(username_input, password_input)
# Тестирование успешного случая
try:
    register_user_for_csv("JohnDoe","Password123!")
except ValueError as e:
    print(f"Ошибка: {e}")
# Тестирование ошибки по имени пользователя
try:
    register_user_for_csv("John Doe","Password123!")
except ValueError as e:
    print(f"Ошибка: {e}")
# Тестирование ошибки по паролю
try:
    register_user_for_csv("JohnDoe","Password123")
except ValueError as e:
    print(f"Ошибка: {e}")