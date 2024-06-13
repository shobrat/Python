my_list = [2, 4, 8, 9, 10, 11]

# print(my_list[:-1])
# print(my_list[::-1])
# print(my_list[:-1:])
# print(my_list[2:])

# print(my_list[0] + my_list[-1])

# text='String'
# print(list(text))
#
# text2='String2'
# new_list = []
# for i in text2:
#     new_list.append(i)
# print(new_list)
#
# text3='String3'
# new_list2=[i for i in text3]
# print((new_list2))

# def change(lst):
#     new_start = lst.pop()
#     new_end = lst.pop(0)
#     lst.append(new_end)
#     lst.insert(0, new_start)
#     return lst
# print(change([1, 2, 3, 4, 5]))

# def change(list):
#     list[0], list[-1] = list[-1], list[0]
#     return list
# print(change([1, 2, 3, 4, 5]))
#
# print(change(['н', 'е', 'у', 'ы', 'в']))

def to_list(*args):
    return list(args)

print(list(['н', 'е', 'у', 'ы', 'в']))