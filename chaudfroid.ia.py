from random import *
from time import *

nombre = 70
nombreJ = 0
nombreB = 0
neuf = 9
GGJ = 0
GGB = 0

print("Jouer avec un bot")
while neuf != 0:
    nombreJ = int(input("Joueur 1 : "))
    nombreB = int(input("BOT : "))
    if nombreJ == 70:
        neuf = 0
        GGJ = GGJ + 1
    elif nombreB == 70:
        neuf = 0
        GGB = GGB + 1

if GGJ == 1:
    print("Bien joué ! Vous avez gagné !")
elif GGB == 1:
    print("Dommage.. retentez une prochaine fois !")
