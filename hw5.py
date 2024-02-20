"""
Домашнее задание №5.
Расщифровка секретного послания
"""


# Секретное послание
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
['и$ #sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]
# Список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

decoding_letter = ''  # Создаем пустую строку для результата
for secret_list in secret_letter:  # Перебираем список из списка списков
    for secret_str in secret_list:  # Перебираем слово из списка
        decoding_letter += " "  # Пробелом в строке разделяем слова
        for secret_symbol in secret_str:  # Перебираем букву из слова
            if secret_symbol in small_rus:  # Смотрим, есть ли буква в списке маленьких русских букв
                decoding_letter += secret_symbol  # Добавляем символ в строку для результата

decoding_letter = decoding_letter.strip().capitalize()  # Удаляем первый пробел и делаем первую букву заглавной
print(decoding_letter)
input("\nНажмите Enter, чтобы выйти из программы:")



