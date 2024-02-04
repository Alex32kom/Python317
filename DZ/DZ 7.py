s = []
n = int(input("Колличество элементов списка: "))
for i in range(n):
    x = int(input("Введите число кратное  3: "))
    if x % 3 == 0:
        s.append(x)
    else:
        print(x, "Не делится на 3 без остатка")
print(s)