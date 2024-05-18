######tipo de dato cadena
myString= "This is my string"
print(myString)
print(type(myString))
print(str(myString) + ". is of the data type " + str(type(myString)))

#######cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)

name = input("what is your name?")
print(name)

color = input("What is you favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
