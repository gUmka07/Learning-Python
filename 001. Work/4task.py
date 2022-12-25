#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер плоскости (от 1 до 4)')
num = int(input())

if num == 1:
    print('Доступные координаты на плоскости №1:')
    print('X = от нуля до плюс бесконечности и Y = от нуля до плюс бесконечности.')
elif num == 2:
    print('Доступные координаты на плоскости №2:')
    print('X = от минус бесконечности до нуля и Y = от нуля до плюс бесконечности.')
elif num == 3:
    print('Доступные координаты на плоскости №3:')
    print('X = от минус бесконечности до нуля и Y = от минус бесконечности до нуля.')
elif num == 4:
    print('Доступные координаты на плоскости №4:')
    print('X = от нуля до плюс бесконечности и Y = от минус бесконечности до нуля.')
elif num > 4: 
    print('Такой плоскости не существует! Попробуйте снова.')
