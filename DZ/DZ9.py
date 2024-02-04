from math import pi

i = int(input("Выбор фигуры:\n 1- треугльник,\n 2 - прямоугольник\n 3- круг\n :"))
if i == 1:
    a = int(input("Введите сторону треугольника a: "))
    b = int(input("Введите высоту треугольника h: "))
    c = (a * b) * 1 / 2
    print(c)

elif i == 2:
    a = int(input("Введите длину прямоугольника"))
    b = int(input("Введите ширину прямоугольника"))
    c = a * b
    print(c)

else:
    i == 3
    a = int(input("Введите радиус круга: "))
    b = round(pi * (a ** 2), 2)
    print(b)
