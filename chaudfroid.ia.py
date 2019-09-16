from random import *
from time import *

nombre = randint(1,101)
nombreBot = randint(1,101)
nom = 0
joueur = 0
coup = 0
diff = 0
nombreJ = 0
nombreB = 0
PVJ = 3
PVB = 3
gg = 0

print()
print("Vous allez jouer contre un bot, vous devez trouver le nombre (entre 1 et 100).")
print("Chaque nombres trouvés enlève 1 point de vie à l'adversaire.")
print("Vous avez trois vies, bonne chance !")
while gg != 1:

    nombreB = randint(1,101)
    nombreJ = int(input("Un nombre ? "))

    if nombreJ < nombre:
        print("C'est plus !")
        print()
    elif nombreJ > nombre: 
        print("C'est moins !")
        print()

    if nombreJ == nombre:
        PVB = PVB - 1
        print("Vous avez infliger un de dégât à l'adversaire, il est à ", PVB)
        print()
        nombre = randint(1,101)
    elif nombreB == nombreBot:
        PVJ = PVJ - 1
        print("Vous avez perdu un point de vie, vous êtes à ", PVJ)
        print()
        nombreBot = randint(1,101)

    if PVJ == 0:
        gg = 1
    elif PVB == 0:
        gg = 1

if PVB == 0:
    print("Bien joué ! Vous avez gagné !")
elif PVJ == 0:
    print("Dommage.. retentez une prochaine fois !")

