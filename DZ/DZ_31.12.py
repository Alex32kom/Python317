a = [0] * int(input("Введите колличество элементов cписка: "))
print(a)
for i in range(len(a)):
    a[i] = float(input("->"))
print(a)

print("Минимальное число:", float(min(a)):
print("Минимальное число:", float(max(a))

total=0
for num in a:
    total += num
print("Среднее арифметическое: ", (total/a))
