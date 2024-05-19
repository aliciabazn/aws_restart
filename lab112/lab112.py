### Clasificación de valores
myMixedTypeList = [45, 19962024, 1.02, True, "My dog id on the bed.", "45"]
for item in myMixedTypeList:
#### los {} se utilizan como marcadores de posición dentro de una cadena
#### de texto. esto serán reemplazados por los valores que añadamos al
#### método .format()
    print("{} is of the data type {}".format(item,type(item)))

    myList = ["Alicia", 28, 1.60, "tres perros", "3"]

for valor in myList:
    print("Yo soy {}".format(valor))
