
# 2. Carré formé de deux nombres consécutifs

#183 184 est le carré à six chiffres de 428. On remarque que ses
#premiers chiffres et ses trois derniers forment deux nombres conséquente
#183 184
#trouver l'unique carré à huit chiffres tel que ses quatre premiers
#chiffres et ses quatre derniers représentent deux nombres consécutifs

# Commande d'affichage du résultat dans le terminal.
#python3 enigme-02.py | less

for i in range(1000, 10000):
    print(i, i ** 2)

#inférieur
# 3163 * 3163 = 10004569 
#supérieur 
#9999 * 9999 = 99980001

for i in range(1000, 9999 + 1):
    carre = i ** 2

    premier_nombre = carre // 10000
    dernier_nombre = carre % 10000

    #@debug
    # print(carre, premier_nombre, dernier_nombre)

    if dernier_nombre -premier_nombre ==1:
        print(i, carre, premier_nombre, dernier_nombre)