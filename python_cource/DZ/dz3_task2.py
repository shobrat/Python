# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k
# и вывести его.
# Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.
#
# Пример:
#

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
# # list_1 = [1, 2, 3, 4, 5]
# # k = 6
#
# equals = 0
# more = 0
# less = 0
#
# for el in list_1:
#
#     if el == k:
#         equals = el
#
#     if el == k + 1:
#         more = el
#
#     if el == k - 1:
#         less = el
#
# if equals > less and equals < more:
#     print(equals)
# if equals == 0 and more == 0:
#     print(less)
# if equals == 0 and less == 0:
#     print(more)

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)






 # if el == k or el == k and el == k + 1 or el == k and el == k - 1 or el == k and el == k - 1 and el == k + 1:
#
# import sys
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 7
#
# equals = 0
# more = 0
# less = 0
#
# for el in list_1:
#     if el == k:
#         equals = el
#         print(equals)
#         sys.exit()
#     if el == k + 1:
#         more = el
#         print(more)
#     if el == k - 1:
#         less = el
#         print(less)



# for el in list_1:
#     if el == k:
#         equals = el
#     if el == k + 1:
#         more = el
#     if el == k - 1:
#         less = el
# if equals > less:
#     print(equals)
# else:
#     print(less)
# if equals < more:
#     print(equals)
# else:
#     print(more)