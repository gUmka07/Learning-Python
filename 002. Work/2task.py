#Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06


n = int(input('Введите число: '))
p = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Для числа {n}: {p} \nСумма: {round(sum(p), 2)}')