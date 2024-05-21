## definir diccionario
## primero leerás el archivo a traves de un modulo csv
## realizaras una copia profunda de los datos para
## almacenarlos en la memoria mediante el modulo copy
## un modulo es un archivo que tiene definiciones y declaraciones
## de funciones, clases y variables que pueden sr utilizada
## en diferenyes partes de un programa
import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
## vamos a recorrer las claves y valores del diccionario
## EL elemento .item() devuelve una vista de los pares key-value.
## item() le dice al bucle for que recorra la colección que pertenece al tipo
## de dato.
for key, value in myVehicle.items():
## imprimir key and value
    print(" para {} tenemos el valor: {}".format(key, value))
## crear una lista vacía
    myInventoryList = []

