#editar un script de python para hacer envios de paquetes
userReply = input("Do you need to ship a package? (Enter yes or no)") #aquí el input es para la entrada del usuario
#ahora iniciamos una condicional if
if userReply == "yes": #== es un opersdor de comparación significa "es igual a"
    print("We can help you ship that package!")
#cuando tenemos varias condicionales utilizamos el "elif"

userReply = input("Would you like to by stamps, buy an envelope or make a copy? (Enter stamps, envelope, copy)")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    