
a = int(input('Введите число: '))
n = a
num_list = []
while n > 0:
    num = n % 2
    num_list.append(str(num))
    n = n // 2
num_list.reverse()
num = int(''.join(num_list))
print(f'Число {a} в десятичной системе = {num} в двоичной системе')