# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
#
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
#
# На выходе:
#
# 1 2 3
# 2 4 6
# 3 6 9

def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))

print_operation_table(lambda x, y: x + y, 4, 4)



# def print_operation_table(operation, num_rows, num_columns):
#     list_list = []
#     for i in range(num_columns):
#         list_temp = []
#         for y in range(num_rows):
#             list_temp.append(operation(i+1, y+1))
#         list_list.append(list_temp)
#     return list_list
#
# list_list = print_operation_table(lambda x, y: x * y, 3, 3 )

#
# print(list(list_list))

# def print_operation_table(operation, num_rows, num_columns):
#     list_list = []
#     for i in range(num_columns):
#         list_temp = []
#         for y in range(num_rows):
#             list_temp.append(operation(i+1, y+1))
#         list_list.append(list_temp)
#     return list_list
#
# list_list = print_operation_table(lambda x, y: x * y)
#
# print("Введите номер строки: ")
# a = int(input())
# print("Введите номер столбца: ")
# b = int(input())
#
# print(list_list[b-1][a-1])

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     print(end="")
#     for i in range(1, num_rows + 1):
#         #print(end="")
#         for j in range(1, num_columns + 1):
#             print(f"{operation(i, j)}", end="")
#         print()
#
#
# print_operation_table(lambda x, y: x + y, 3, 3)

#
# def print_operation_table(operation, num_rows = 3, num_columns = 3):
#     for i in range(num_rows):
#         for j in range(num_columns):
#             operation = (i+1) * (j+1)
#             print(operation, end=" ")
#         print(end="\n")
#     return operation
#
# #
# print(print_operation_table(num_rows * num_columns, 3, 3))
# #
# def print_operation_table(operation, num_rows, num_columns):
#     for i in range(num_rows):
#         for j in range(num_columns):
#             operation = (i+1) * (j+1)
#             print(operation, end=" ")
#         print(end="\n")
#
# print(print_operation_table(0, 3, 3))

# operation = [lambda x: x for x in range(3)]
#
# for y in operation:
#     print(y)
#
# print_operation_table(lambda x, y: x * y, 3, 3)
