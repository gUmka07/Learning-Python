#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

from random import randint as ri
n=int(input("Введите длинну массива: "))
array = [ri(1, 100) for _ in range(n)]
otvet = []
for i in range((len(array) // 2 + len(array) % 2)):
    end = array[i] * array[-i-1]
    otvet.append(end)
print(f'Созданный массив: {array} => произведение пар чисел: {otvet}')