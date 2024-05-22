## definir diccionario
## primero leerás el archivo a traves de un modulo csv
## realizaras una copia profunda de los datos para
## almacenarlos en la memoria mediante el modulo copy
## un modulo es un archivo que tiene definiciones y declaraciones
## de funciones, clases y variables que pueden sr utilizada
## en diferenyes partes de un programa
import csv
import copy #se usa para copias profundas (deep copies) de objetos.
#tenemos un diccionario plantilla para los atributos de un auto.
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
## crear una lista vacía, almacenará dicc de autos.
    myInventoryList = []

## with open es una manera segura de abrir archivos para lectura
## o escritura. Garantiza que un archivo se cerrará automáticamente
## una vez se complete el bloque de código.
##previene:fugas de recursos y prevenir errores.
##as csvFile nombre de la variable(objeto)
with open("car_fleet.csv") as csvFile:
## csv.reader(argu1, argu2) funcion del modulo csv en python que se utiliza para leer archivos csv.
## toma dos argumentos argu1 el objeto del archivo que queremos leer
## argu2 delimitador de campos 
##csvReader esta variable ahora tiene un objeto que se pude iterar para leer las filas del archivo csv
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0 # para iniciar el contador de lineas
    for row in csvReader: #iterar sobre cada row del archivo csv
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1 #incrementamos el contador de líneas.
        else: #para todas las demas lineas, imprime los datos del vehiculo
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage:{row[7]}')    
            #creamos una copia independiente de myvehicle, de modo que cualquier cambio no afectará al archivo original
            currentVehicle = copy.deepcopy(myVehicle) #cla función opy.deepcopy del modulo copy, crea una copia profunda de un objeto, garantiza que se creen nuevas cajas
            # de almacenamiento para los nuevos datos.
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            
        lineCount += 1 #mantiene un conteo de linea. incrementa el valor de linecount
        #lineCount = lineCount + 1 <-- "ejemplo"
    print(f'Processed {lineCount} lines.') #imprimimos el valor actual de linecount
    currentVehicle = copy.deepcopy(myVehicle)
    #iniciamos bucle que recorre los elementos de myinvertorylist
    #a este elemento le asignamos una variable mycarproperties en cada iteración
    for myCarProperties in myInventoryList: 
        for key, value in myCarProperties.items(): #segunda iteración, item devuelve una vista de pares(clave valor)
            #item le indica al bucle que la iteación se haga dependiendo al tipo de dato que es: clave valor
            print("{} : {}".format(key,value))
            print("-----")