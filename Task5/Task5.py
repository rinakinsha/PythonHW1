x1 = float(input('Введите координаты точки А: ax = '))
y1 = float(input('                            ay = '))

x2 = float(input('Введите координаты точки B: bx = '))
y2 = float(input('                            by = '))

from math import hypot                  #hypot - функция вычисления квадратного корня из суммы квадратов
result = hypot((x2 - x1),(y2 - y1))

print(round(result, 2))