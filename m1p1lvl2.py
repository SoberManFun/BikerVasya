# Модуль1.Часть1.Уровень2.начало
mkad1 = 109
speed1 = abs(int(input('Введите скорость Байкера Васи: ')))
time1 = abs(int(input('Введите время Байкера Васи до остановки в часах: ')))
s1 = speed1 * time1 % mkad1
print('Байкер Вася остановится на: ', s1, 'км')
# Модуль1.Часть1.Уровень2.конец