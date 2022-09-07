
# un artilleur dispose de boule"ts de canon répartis dans un carré parfait. 
# Pour réduire l'encomrement au sol, l'artilleur réussit à empiler ses boulets pour former une belle pyramyde à base carré 
# quel est le plus petit nombre de boulets possible dont dispose l'artilleur ?

#Compléxité algorithimique
#O( n + n²) == O(n * (1 + n))

#liste en compréhension
#On démarre à 2 pour éviter que la boucle for principale
# trouve 1 comme résultat
# de plus ça nous évite de faire un if à chaque itération qui
#vérifie que le résultat est différent de 1.
#liste de compréhension
squares = [i ** 2 for i in range(2, 100)]

#fait la meme chose avec une boucle for
# squares = []
# for i in range(1, 101):
#     squares.append(i ** 2)


#Comme les carrées précalculés démarrent à 1, il faut pré-compter
#ce boulet dans la pyramide.
pyramid = 1

for bullet in squares:
    pyramid += bullet
    
    if pyramid in squares:
        print(pyramid)
        break