# Помогите Кате отгадать задуманные Петей числа
#
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах.
# В результате вы должны вывести все возможные пары чисел X и Y через пробел,
# такие что X <= Y.
#
# Пример На входе:
# s = 12
# p = 27
# На выходе:
# 3 9

s = 17
p = 72

x = 0
y = 0

for x in range(30):
    for y in range(30):
        if x + y == s and x * y == p:
            if x <= y:
                print(f'{x} {y}')
