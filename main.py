# TODO hacer un programa que elija un numero random (1-100)
# y en una venta le pedia al usuario que adivine el número,
# si no es el número elegido le diara que vuelva a intentarlo,
# con un número mayor o menor dependiendo de su respuesta

import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("What number am I thinking? "))

    if (guess < number):
        print("Sorry ＞﹏＜, try with a higher number")
    elif (guess > number):
        print("Sorry ≧ ﹏ ≦, try with a lower number")
    else:
        print("Woo Hoo \^o^/, you guessed the number")
