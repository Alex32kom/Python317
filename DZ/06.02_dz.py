prodavets = {
    'John': {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694,
    },
    "Tom": {
        "N": 4832,
        "S": 6786,
        "E": 4737,
        "W": 3612,
    },

    "Anne": {
        "N": 5239,
        "S": 4802,
        "E": 5820,
        "W": 1859,

    },

    "Fiona": {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451,

    },

}

for x in prodavets:
    print(x)
    for y in prodavets[x]:
        print("\t", y, ":", prodavets[x][y])

prod = str(input("ВВедите продавца: "))
if prod == 'John':
    print("John: ", prodavets['John']),
    elif:
        prod == "Tom":
            print(""Tom": ", prodavets['"Tom"']),
#             elif:
#         prod == "Anne":
#             print({prodavets["Anne"}),
#          elif:
#         prod == "Fiona":
#         print({prodavets["Fiona"]}),
#  else:
# print("Такого продавца нет!")


# print(prodavets)
# print(prodavets.keys())
# prod = str(input("Введите имя продавца(John,Tom,Anne,Fiona: ->"))
# print("Имя продавца: ", prod)
#
#
# print(prod.items())

# print(prodavets[x])

# for key, value in prod.items():
#     print(key, "->", value)
