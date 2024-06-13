# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# Пример:
# k = 'ноутбук'
# 12


# a = input()
#
# str_1 = 'AE'
#
# num = 0
#
# for el in a:
#     if el == str_1:
#         num += 1
#
# print(num)

#
#
# # str_1 = "AE"
#
# a = input()
# list_1 = ('A', 'E')
#
# num = 0
#
# for i in list_1:
#     for el in a:
#         if el == list_1[i]:
#         num += 1
#
# print(num)

# k = input()
#
# cnt_en_1 = 0
# cnt_en_2 = 0
# cnt_en_3 = 0
# cnt_en_4 = 0
# cnt_en_5 = 0
# cnt_en_6 = 0
# cnt_en_7 = 0
#
# cnt_ru_1 = 0
# cnt_ru_2 = 0
# cnt_ru_3 = 0
# cnt_ru_4 = 0
# cnt_ru_5 = 0
# cnt_ru_6 = 0
# cnt_ru_7 = 0
#
# for el in k:
#     if el == 'a' or el == 'e' or el == 'i' or el == 'o' or el == 'u' or el == 'l' or el == 'n' or el == 's' or el == 't' or el =='r':
#         cnt_en_1 += 1
#     if el == 'd' or el == 'g':
#         cnt_en_2 += 2
#     if el == 'b' or el == 'c' or el == 'm' or el == 'p':
#         cnt_en_3 += 3
#     if el == 'f' or el == 'h' or el == 'v' or el == 'w' or el == 'y':
#         cnt_en_4 += 4
#     if el == 'k':
#         cnt_en_5 += 5
#     if el == 'j' or el == 'x':
#         cnt_en_6 += 8
#     if el == 'q' or el == 'z':
#         cnt_en_7 += 10
#     if el == 'а' or el == 'в' or el == 'е' or el == 'и' or el == 'н' or el == 'о' or el == 'р' or el == 'с' or el == 'т':
#         cnt_ru_1 += 1
#     if el == 'д' or el == 'к' or el == 'л' or el == 'п' or el == 'у':
#         cnt_ru_2 += 2
#     if el == 'б' or el == 'г' or el == 'ё' or el == 'ь' or el == 'я':
#         cnt_ru_3 += 3
#     if el == 'й' or el == 'ы':
#         cnt_ru_4 += 4
#     if el == 'ж' or el == 'з' or el == 'х' or el == 'ц' or el == 'ч':
#         cnt_ru_5 += 5
#     if el == 'ш' or el == 'э' or el == 'ю':
#         cnt_ru_6 += 8
#     if el == 'ф' or el == 'щ' or el == 'ъ':
#         cnt_ru_7 += 10
#
# num_en = cnt_en_1 + cnt_en_2 + cnt_en_3+ cnt_en_4 + cnt_en_5 + cnt_en_6 + cnt_en_7
# num_ru = cnt_ru_1 + cnt_ru_2 + cnt_ru_3+ cnt_ru_4 + cnt_ru_5 + cnt_ru_6 + cnt_ru_7
#
# print(num_en + num_ru)

k = input()

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                count = count + j
print(count)