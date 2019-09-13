from random import *
from time import *

nombre = randint(1,101)
nombreJ = 0
nombreB = 0
neuf = 9
GGJ = 0
GGB = 0

print("Jouer avec un bot")
while neuf != 0:
    
    nombreB = randint(1,101)
    nombreJ = int(input("Joueur 1 : "))
    
    if nombreJ < nombre:
        print("C'est plus !")
    elif nombreJ > nombre: 
        print("C'est moins !")
        
    if nombreJ == nombre:
        neuf = 0
        GGJ = GGJ + 1
    elif nombreB == nombre:
        neuf = 0
        GGB = GGB + 1

if GGJ == 1:
    print("Bien joué ! Vous avez gagné !")
elif GGB == 1:
    print("Dommage.. retentez une prochaine fois !")
