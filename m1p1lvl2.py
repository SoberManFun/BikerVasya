# Модуль1.Часть1.Уровень2.начало
mkad1 = 109
speed1 = abs(int(input('Введите скорость Байкера Васи: ')))
time1 = abs(int(input('Введите время Байкера Васи до остановки в часах: ')))
s1 = speed1 * time1
rcount1 = s1 / mkad1
if rcount1 < 1:
	s1 = rcount1 * mkad1
	s1 = round(s1)
	print('Байкер Вася остановится на: ', s1, 'км')
else:
	s1 = (rcount1 - int(rcount1)) * mkad1
	s1 = round(s1)
	print('Байкер Вася остановится на: ', s1, 'км')
# Модуль1.Часть1.Уровень2.конец