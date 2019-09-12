from random import *
def prog():
    

    nombre = randint(1,101)
    nom = 0
    joueur = 0
    coup = 0
    diff = 0

    print("On va jouer à un jeu ! ")

    joueur = int(input("Vous êtes seul ? Ou deux ? (répondre par le chiffre) ")) #Le jeu demande le nombre de joueurs

    if joueur == 1: #Si il y a un seul joueur alors..
        diff = int(input("Quelle difficultée ? (de 1 à 3) ")) #le jeu demande la difficulté (de 1 à 3)
        if diff == 1: #Si la difficulté est à 1 alors..
            nombre = randint(1,101) #le jeu crée un nombre aléatoire entre 1 et 100
            print("Tu dois maintenant un nombre entre 0 et 100 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1 #On ajoute un coup au compteur
                if nom < nombre: #Si le nombre du joueur est inférieur au nombre du jeu alors..
                    print("C'est plus !")
                elif nom > nombre: #Si le nombre du joueur est supérieur au nombre du jeu alors..
                    print("C'est moins !")
                else: #Si le jouer trouve le nombre du jeu alors..
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
        elif diff == 2:
            nombre = randint(1,1001)
            print("Tu dois maintenant chercher un nombre entre 0 et 1 000 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1
                if nom < nombre:
                    print("C'est plus !")
                elif nom > nombre:
                    print("C'est moins !")
                else:
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
        elif diff == 3:
            nombre = randint(1,10001)
            print("Tu dois maintenant chercher un nombre entre 0 et 10 000 !")
            while nom != nombre:
                nom = int(input("Un nombre ? "))
                coup = coup + 1
                if nom < nombre:
                    print("C'est plus !")
                elif nom > nombre:
                    print("C'est moins !")
                else:
                    print("GGWP, vous l'avez trouvé en ", coup, " coups !")
        else:
            print("Impossible de jouer dans une difficulté supérieur à 3..")

    elif joueur == 2:
         nombre = int(input("Joueur 1, mettez un nombre dans l'espace suivant (redonne le clavier à ton ami juste après): "))

         for vide in range(50):
            print()

         print("Tu dois maintenant chercher le nombre ! ")
         while nom != nombre:
             nom = int(input("Un nombre ? "))
             coup = coup + 1
             if nom < nombre:
                print("C'est plus !")
             elif nom > nombre:
                print("C'est moins !")
             else:
                   print("GGWP, vous l'avez trouvé en ", coup, " coups !")
    

    restart = input("Veux-tu recommencer à jouer ? o/n")
    if restart == "o":
        prog()
    else:
        exit()

prog()

