# def s_paralrp():
#
#
#
#
#     def s_prymoug():
#         # nonlocal s_prymoug
#         a = (int(input("Введите длину прямоугольника: ", )))
#         b = (int(input("Введите ширину прямоугольника: ", )))
#
#         s_prymoug = a * b
#         return s_prymoug
#
#     print(s_prymoug())
#
#     return s_prymoug
# s=s
#
# plosh=s_paralrp()
# print(plosh())







def pryamoug(proizv):

    def inner():
        a = int(input("Введите длину прямоугольника: "))
        b = int(input("Введите ширину прямоугольника: "))
        return (a*b)

    # return inner
    inner()
    return inner()
    c=2*inner
pryamoug()
return pryamoug()

print()

# plosh=pryamoug()
# print(pryamoug)


