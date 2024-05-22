#mientras pase A hagamos


# Trabajo con bucles
# vamos a incluir el codigo que escribió otra persona
# mportamos otro codigo
import random
# bucle while hace que la sección se repita hasta que se
# cumpla una determinada condición
print("Welcome to Guess the Number")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#randint() es una de las funciones del modulo random
# y generará un numero aleatorio entre 1 y 10.
number = random.randint(1,10)
print(number)
isGuessRight = False
#" != " no igual a
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    print(guess)
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))