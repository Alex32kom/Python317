k = int(input("Введите колличество копеек: "))
if 1 <= k <= 99:
    if k == 11 or k == 12 or k == 13 or k == 14 or 5<= k%10<=9 or k%10==0:
        print(k, "копеек")
    else:
        if k % 10 == 1:
            print(k, "Копейка")
        if k % 10 == 2 or k % 10 == 3 or k %10 ==4:
            print(k, "копейки")
        else:
            print("Ошибка ввода")
