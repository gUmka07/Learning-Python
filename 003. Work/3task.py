# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import *
n=int(input("Введите длинну массива: "))
array = [round(uniform(1.0, 10.5), 2) for _ in range(n)]
fractional_part = []
for item in array:
    if isinstance(item, float):
        fractional_part.append(item % 1)
result = round(max(fractional_part) - min(fractional_part), 2)
print(f'Созданный список: {array}.\nРазница между максимальной и минимальной дробной частью: {result}')