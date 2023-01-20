# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def creat_float_list(lenght):  # функция для создания списка вещественных чисел
    import random
    #Было:
    # num_float = []
    # for _ in range(lenght):
    #     amount = random.randint(0, 4)
    #     num_float.append(round(random.uniform(0, 2), amount))
    #Стало:
    num_float = [round(random.uniform(0, 2),random.randint(0, 4)) for _ in range(lenght)]
    return num_float


def maximum_element(my_list: list):  # функция поиска максимального элемента
    maximum = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
    return maximum


def minimun_element(my_list: list):  # функция поиска мин элемента
    minimum = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < minimum:
            minimum = my_list[i]
    return minimum


num_float = creat_float_list(5)
print(num_float)
len_list = len(num_float)

#Было:
# for i in range(len_list): #обнуляем целую часть всех чисел
#     length = len(str(num_float[i])) - 2
#     num_float[i] = round((num_float[i] + 1) % (int(num_float[i]) + 1), length)  # +1, чтобы избежать деления на 0.

# Cтало:
def fraction (num):
    length = len(str(num)) - 2
    num = round((num + 1) % (int(num)+1), length)
    return num
num_float = [fraction(num_float[i]) for i in range (len_list)]

print(num_float)
#Было:
# for _ in range(num_float.count(0.0)):  # убираем числа с нулевой дробной частью
#     num_float.remove(0.0)

#Стало:
num_float = [num_float[x] for x in range(len(num_float)) if num_float[x] != 0.0]
print(num_float)
if len(num_float) > 0:
    max_element = maximum_element(num_float)
    min_element = minimun_element(num_float)
    print(round(max_element - min_element, 3))
else:
    print("В списке нет чисел с дробной частью")
