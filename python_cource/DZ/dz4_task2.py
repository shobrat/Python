# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки.
# Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.
# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом,
# и он может выбирать, с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход,
# находясь перед некоторым кустом грядки.
#
# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
#
# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
#
# Пример использования На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе: 19
#
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# sum = 0
# for item in arr:
#     sum = sum + item
# print(sum)


arr = [5, 8, 6, 4, 9, 2, 7, 3]

max = 0
for i in range(len(arr)):
    if max > arr[i]:
        max = max
    else:
        max = arr[i]
        #print(max)
print(max)

# print([i for i in range(len(arr)) if max > arr[i] max = max else max = arr[i]])
# arr = [15, 8, 6, 4, 9, 2, 7, 23]
# max = 0
#
# for i in range(len(arr) - 1):
#     if max < arr[i]:
#         max = arr[i]
#     #else:
#         #arr[i] = max
#
# print(max)
