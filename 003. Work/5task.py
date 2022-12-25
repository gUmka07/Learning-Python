# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
fib_list1, fib_list2 = [0, 1], [1]
fib1, fib2, fib_1, fib_2 = 0, 1, 0, 1
for _ in range(n-1):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list1.append(fib2)
    fib_1, fib_2 = fib_2, fib_1 - fib_2
    fib_list2.append(fib_2)
fib_list2.reverse()
fib_list = fib_list2.copy()
fib_list.extend(fib_list1)
print(f'Для числа {n} последовательность Фибоначчи и Негафибоначчи: {fib_list}')