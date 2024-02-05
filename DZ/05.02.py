matem = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
phys = {"Максим", "Матвей", "Александр"}
prizery = list(matem | phys)
obsh_pryzery = matem & phys
matem_novye = (matem) & (phys)
print(matem)
print(phys)
print("Все призёры олимпиад: ", prizery)
print("Призёры обоих олимпиад : ", obsh_pryzery)
print("Обновлённый список призёров по математике: ", matem_novye)
