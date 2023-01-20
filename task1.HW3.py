# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

# Было:
# num_list = []
# for _ in range(10):
#     num_list.append(random.randint(1, 10))

# Стало:
num_list = [random.randint(1, 10) for _ in range(10)]

print(num_list)
sum_num = 0
for i in range(1, len(num_list), 2):
    sum_num += num_list[i]
print(f"Сумма элементов с нечетными индексами =  {sum_num}")
