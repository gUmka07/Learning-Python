# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
max=100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
kef=[randint(0,max) for i in range(k)]+[randint(1,max)]
mnogochlen='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(kef) if j][::-1])

mnogochlen=mnogochlen.replace('x^1+', 'x+')
mnogochlen=mnogochlen.replace('x^0', '')
mnogochlen+=('','1')[mnogochlen[-1]=='+']
mnogochlen=(mnogochlen, mnogochlen[:-2])[mnogochlen[-2:]=='^1']
print(mnogochlen)
