
a = [int(input("->")) for i in range(int(input("Количество элементов списка n = ")))]
print(a)
x = int(input("Введите число: "))
k = int(input("Введите число k, индекс расположения:"))
a.insert(k, x)
print(a)