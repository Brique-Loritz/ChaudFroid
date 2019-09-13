from random import *
from time import *

nombre = randint(1,101)
nombreJ = 0
nombreB = 0
PVJ = 3
PVB = 3
gg = 0

print("Jouer avec un bot")
while gg != 1:
    
    nombreB = randint(1,101)
    nombreJ = int(input("Joueur 1 : "))
    
    if nombreJ < nombre:
        print("C'est plus !")
    elif nombreJ > nombre: 
        print("C'est moins !")
        
    if nombreJ == nombre:
        PVB = PVB - 1
        print("Vous avez infliger un de dégât à l'adversaire, il est à ", PVB)
        nombre = randint(1,101)
    elif nombreB == nombre:
        PVJ = PVJ - 1
        print("Vous avez perdu un point de vie, vous êtes à ", PVJ)
        nombre = randint(1,101)

    if PVJ == 0:
        gg = 1
    elif PVB == 0:
        gg = 1
        
if PVB == 0:
    print("Bien joué ! Vous avez gagné !")
elif PVJ == 0:
    print("Dommage.. retentez une prochaine fois !")
