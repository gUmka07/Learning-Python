# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101,  3 -> 11,  2 -> 10.

                # Изначальное решение
# a = int(input('Введите число: '))
# n = a
# num_list = []
# while n > 0:
#     num = n % 2
#     num_list.append(str(num))
#     n = n // 2
# num_list.reverse()
# num = int(''.join(num_list))
# print(f'Число {a} в десятичной системе = {num} в двоичной системе')

                #Вариант 1
# a = int(input('Введите число: '))
# print(bin(a))

                #Вариант 2
# a = int(input('Введите число: '))
# print(f"Число {a} в двоичной системе = {format(a,'b')}")
