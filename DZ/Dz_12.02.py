
students = {}
n = int(input("Кол-во студентов: "))
s = 0
for key in range(n):
    name = input(str(key + 1) + "- студент: ")
    point = int(input("Балл: "))
    students[name] = point
    s += point

average = s / n
print("Средний бал: ", average)
for key in students:
    if students[key] > average:
        print(key)

