resultats= []

#carré de 2 chiffres : 4 à 9
liste_carres_2 = []
for i in range(4, 10):
    liste_carres_2.append(i ** 2)

print(liste_carres_2)

#carré de 4 chiffres : 32 à 99

liste_carres_4 = []

for i in range(32, 100):
     liste_carres_4.append(i ** 2)

print(liste_carres_4)

#construissons des nombres à 4 chiffres

for i in liste_carres_2:
    for j in liste_carres_2:
        nombre= i * 100 + j

        if nombre in liste_carres_4:
            resultats.append(nombre)

print(resultats)
