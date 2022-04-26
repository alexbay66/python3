# exercice-07-boucles.py

import random

# exo 7.1
# en utilisant une boucle for, affichez les nombre de 0 à 99 inclus

# réponse 7.1
for counter in range(0, 99+1):
    print('for ex1:', counter)
# exo 7.2
# en utilisant une boucle for, affichez les nombre de 0 à 100 inclus

# réponse 7.2
for counter in range(0, 100+1):
    print('for ex2:', counter)
# code 7.1
# affectation d'un nombre aléatoire compris entre 1 et 10 inclus
number = random.randint(1, 10)

# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1

# réponse 7.3
for r in range(100):
    r = random.randint(1, 10)
    if r == 1:
        print("ex3 =", r)


# exo 7.4
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus petit ou égal à 5

# réponse 7.4
for r in range(50):
    r = random.randint(1, 10)
    if r <= 5:
        print("ex4 =", r)
# exo 7.5
# en utilisant une boucle for, on tire 20 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6

# réponse 7.5
for r in range(20):
    r = random.randint(1, 10)
    if r >= 6:
        print("ex5 =", r)
# exo 7.6
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1 ou égal à 10

# réponse 7.6
for r in range(100):
    r = random.randint(1, 10)
    if r == 1 or r == 10:
        print("ex6 =", r)
# exo 7.7
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est compris entre 3 et 8 inclus

# réponse 7.7
for counter in range(100):
    r = random.randint(1, 10)
    if r >= 3:
        if r <= 8:
            print("ex7 =", r)

# exo 7.8
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est égal à 7
# affichez la variable `count`

# réponse 7.8
count = 0
for counter in range(50):
    r = random.randint(1, 10)
    if r == 7:
        count += 1
        print("ex8 =", count)

# exo 7.9
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 4
# affichez la variable `count`

# réponse 7.9
count = 0
for counter in range(10):
    r = random.randint(1, 10)
    if r <= 4:
        count += 1
        print("ex9 =", count)
# exo 7.10
# en utilisant une boucle for, on tire 33 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count`

# réponse 7.10
count = 0
for counter in range(33):
    r = random.randint(1, 10)
    if r >= 7:
        count += 1
        print("ex10 =", count)
# exo 7.11
# en utilisant une boucle for, on tire 66 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 2, ou plus grand ou égal à 9
# affichez la variable `count`

# réponse 7.11
count = 0
for counter in range(66):
    r = random.randint(1, 10)
    if 2 < r > 9:
        count += 1
        print("ex11 =", count)
# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count`

# réponse 7.12
count = 0
for counter in range(66):
    r = random.randint(1, 10)
    if 2 <= r >= 9:
        count += 1
        print("ex12 =", count)
# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus

# réponse 7.13
for pair in range(0 ,99 +1):
    if (pair % 2) == 0:
        print(pair)
# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14
for pair in range(1 ,100 +1):
    if (pair % 2) == 0:
        print(pair)
# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15
for pair in range(1 ,99 +1):
    if (pair % 3) == 0:
        print(pair)
# code 7.2
# pour calculer la puissance 2 d'un nombre, on peut le multiplier par lui-même
number = random.randint(3, 10)
print(number * number)
# mais on peut aussi l'élever à la puissance 2 avec l'opérateur puissance `**`
print(number ** 2)

# exo 7.16
# en utilisant une boucle for, affichez la puissance 2 des nombres de 0 à 99 inclus

# réponse 7.16
for puissance in range(0, 99 +1):
    print(puissance ** 2)
# code 7.3
# pour calculer la puissance 3 d'un nombre, on peut l'élever à la puissance 3 avec l'opérateur puissance `**`
number = random.randint(3, 10)
print(number ** 3)

# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus

# réponse 7.17
for puissance in range(0, 100 +1):
    print(puissance ** 3)
# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

# réponse 7.18
count= 0
while r:
    count += 1
    r = random.randint(1, 100)
    if r == 100:
        print(count)
        print(r)
        break