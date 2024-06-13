'''
Создать телефонный справочник с возможностью импорта и экспорта
данных в формате .txt. Фамилия, Имя, Отчество, номер телефона - данные,
которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранить данные в текстовом файле
3. Пользователь может вывести одну из характеристик для поиска
определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной.
'''

from csv import DictReader, DictWriter

def get_info():
    first_name = 'Иван'
    second_name = 'Иванов'
    phone_number = 89123456789
    return [first_name, second_name, phone_number]


# Создание файла

def create_file(file_name):
    with open(file_name, 'w', encoding='utf - 8') as data: # Контекстный менеджер, data - поток данных
        f_w = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон']) # Это шапка
        f_w.writeheader()

def write_file(file_name):
    res = read_file(file_name)

# Чтение файла

def read_file(file_name):
    with open(file_name, encoding='utf - 8') as data:
        f_r =DictReader(data)
        return list(f_r) # список со словарями