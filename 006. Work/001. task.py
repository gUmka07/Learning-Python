# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

                    # Изначальное решение
from random import randint as ri
# n=int(input("Введите длинну массива: "))
# array = [ri(1, 100) for _ in range(n)]
# total = 0
# for i in range(1, len(array), 2):
#     total += array[i]
# print(f'Созданый список: {array}\nСумма элементов на позиции с нечетным индексом: {total}')

                    # Вариант 1: Не отображается список

# print(sum([[ri(1,10) for _ in ] if x%2 ==1]))


                    # Вариант 2: Хочу чтобы отображался список

# list = [x for x in [ri(1,10) for _ in range(10)] if x%2 ==1]
# print(list)
# res = sum(list)
# print(res)

                    # Вариант 3: Уже введенный список

# data = [1,2,3,4]
# print(sum(list(filter(lambda x: x%2==1, data))))

                    # Вариант 4: Хз зачем. Пусть будет

# data = [x for x in range(10) if x%2 == 0]
# print(sum(data))

