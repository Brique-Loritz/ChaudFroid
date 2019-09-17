from random import *
import subprocess
def prog():
    
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

    print("Bienvenue dans Chaud Froid ! ")

    print("1/ Vous êtes seul ?")
    print("2/ Ou deux ?")
    print("(répondre par le chiffre)")

    joueur = int(input())

    if joueur == 1: 
        print("Quel type de jeu ?")
        print("1/ Facile")
        print("2/ Normale")
        print("3/ Difficile")
        print("4/ Contre un bot")
        print("(répondez par le chiffre)")
        diff = int(input())
        
        if diff == 1:
            print()
            nombre = randint(1,101) 
            print("Tu dois maintenant un nombre entre 0 et 100 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1 
                if nom < nombre:
                    print("C'est plus !")
                    print()
                elif nom > nombre: 
                    print("C'est moins !")
                    print()
                else: 
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
                    
        elif diff == 2:
            print()
            nombre = randint(1,1001)
            print("Tu dois maintenant chercher un nombre entre 0 et 1 000 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1
                if nom < nombre:
                    print("C'est plus !")
                    print()
                elif nom > nombre:
                    print("C'est moins !")
                    print()
                else:
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
                    
        elif diff == 3:
            print()
            nombre = randint(1,10001)
            print("Tu dois maintenant chercher un nombre entre 0 et 10 000 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1
                if nom < nombre:
                    print("C'est plus !")
                    print()
                elif nom > nombre:
                    print("C'est moins !")
                    print()
                else:
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
                    
        elif diff == 4:
            import subprocess
            subprocess.call(["C:\Python\Python.exe", "C:\ChaudFroid\chaudfroid.ia.py"])
    
        else:
            print("Impossible de jouer dans une difficulté supérieur à 4..")

    elif joueur == 2:
         nombre = int(input("Joueur 1, mettez un nombre (entre 1 et 100) dans l'espace suivant (redonne le clavier à ton ami juste après): "))

         for vide in range(50):
            print()

         print("Tu dois maintenant chercher le nombre ! ")
         while nom != nombre:
             nom = int(input("Un nombre ? "))
             coup = coup + 1
             if nom < nombre:
                print("C'est plus !")
                print()
             elif nom > nombre:
                print("C'est moins !")
                print()
             else:
                   print("GGWP, vous l'avez trouvé en ", coup, " coups !")
    

    restart = input("Veux-tu recommencer à jouer ? o/n ")
    if restart == "o":
        print()
        prog()
    else:
        exit()

prog()
