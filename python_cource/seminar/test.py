#
# list1 = 'red'
# a = list(list1)
# b = list1.split()
# # for i in a:
# #     if i == a[0]:
# #         print(i)
# print(len(list1))
# print(len(a))
# print(len(b))
#
# for i in b:
#     if len(b) == 1:
#         print(i)

# import copy
#
# original_list = [1, 2, [3, 4]]
# shallow_copy = copy.copy(original_list)
# original_list[2][0] = 99
# print((original_list))
# print((shallow_copy))
#
#
# original_list2 = [2, 2, [3, 10]]
# deep_copy = copy.deepcopy(original_list2)
#
# print(deep_copy)
#
# search = int(input('Введите номер строки для удаления: '))
# res = read_file(original_list)
# if search <= len(res):
#     res.pop(search - 1)
#     standart_write(file_name, res)


import csv
from csv import DictWriter, DictReader
from os.path import exists


class NamesError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NamesError('Слишком короткое имя!')
            second_name = input('Фамилия: ')
            if len(second_name) < 4:
                raise NamesError('Слишком короткое имя!')
            phone_numbers = input('Телефон: ')
            if len(phone_numbers) < 11:
                raise NamesError('Слишком короткий номер телефона!')
        except NamesError as err:
            print(err)
        else:
            return [first_name, second_name, phone_numbers]


def created_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_numbers'])
        f_w.writeheader()


def write_file(file_name):
    res = read_file(file_name)
    user_info = get_info()
    new_obj = {'first_name': user_info[0], 'second_name': user_info[1], 'phone_numbers': user_info[2]}
    res.append(new_obj)
    standard_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def delete_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standard_write(file_name, res)
    else:
        print(f'Строка {search} отсутствует!')


def copy_row(file_name, new_file, row_number):
    with open(file_name, 'r', newline='', encoding='utf-8') as data:
        reader = csv.reader(data)
        rows = list(reader)
        if row_number >= len(rows):
            print(f"Строка {row_number} не существует!")
        else:
            row_to_copy = rows[row_number]
            with open(new_file, 'a', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(row_to_copy)


def standard_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_numbers'])
        f_w.writeheader()
        f_w.writerows(res)


file_name = 'phone.csv'
new_file = 'phone2.csv'


def main():
    while True:
        command = input(f"Список команд: \nr - чтение данных в файле \nR - чтение данных в новом файле"
                        f"\nw - запись данных в файл \nc - копирование строк в новый файл \nd - удаление строк в файле"
                        f"\nq - выход из программы \n\nВведите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                created_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл не существует, создайте файл!')
                continue
            print(*read_file(file_name))
        elif command == 'R':
            if not exists(file_name):
                print('Файл не существует, создайте файл!')
                continue
            print(*read_file(new_file))
        elif command == 'd':
            if not exists(file_name):
                print('Файл не существует, создайте файл!')
                continue
            delete_row(file_name)
        elif command == 'c':
            if not exists(new_file):
                created_file(new_file)
                print('Так как файл не существует, будет создан новый файл, введите команду С еще раз!')
                continue
            row_number = int(input('Введите номер строки для копирования: '))
            copy_row(file_name, new_file, row_number)
main()