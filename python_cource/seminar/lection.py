# Пример: 1 2 3 5 8 15 23 38
#
# Получить: [(2, 4), (8, 64), (38, 1444)]
#

# list_1 = '1 2 3 5 8 15 23 38'
# sum = 0
# s = set(map(int, list_1.split()))
# for el in s:
#     if el % 2 == 0:
#         sum = el * el
#         print(f'({el}, {sum})')

# data = [1, 2, 3, 5, 8, 15, 23, 38]
#
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2)) # Добавление данных в лист
# print(res)

# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
#
# res = select(int, data)
# print(res)
#
# res2 = where(lambda x: x % 2 == 0, res)
# print(res2)
#
# res3 = select(lambda x: (x, x ** 2), res2)
# print(res3)
#
# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
#
# print(list_1)

tables = [lambda x = x: x*10 for x in range(1, 11)]
for i in tables:
    print(i())