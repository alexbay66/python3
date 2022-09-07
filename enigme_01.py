
resultats = []

# carré de 2 chiffres : 4 à 9

carres_2_chiffres = [] 

for i in range(4, 10):
    carres_2_chiffres.append(i ** 2)

print(carres_2_chiffres)
# carré de 4 chiffres : 32 à 99

carres_4_chiffres = []

for i in range(32, 100):
     carres_4_chiffres.append(i ** 2)

     print(carres_4_chiffres)

    

    # constructions des nombres à 4 chiffres
#construissons des nombres à 4 chiffres

for i in carres_2_chiffres:
    for j in carres_2_chiffres:
        nombre= i * 100 + j

        if nombre in carres_4_chiffres:
            resultats.append(nombre)

print(resultats)

#Solutions 1:
# L1 = [ n**2 for n in range (4,9+1)] #liste des carrés à 2 chiffres
# L2 = [ n**2 for n in range (32,99+1)] #liste des carrés à 4 chiffres


# reponse = []

# for i in L2:
#     i = str(i)
#     if int(i[:2]) in L1 and int(i[2:4]) in L1:
#         reponse.append(int(i))
# print(reponse)

# Solutions 2 : 
# for i in range(1000, 9999):
#     if (int(i**(1/2)) == (i**(1/2))) and (int((i//100)**(1/2)))== ((i//100)**(1/2)) and int((i%100)**(1/2)) ==(i%100)**(1/2) and i%100 !=0:
#         print (i)

#Solutions 3:
# carreDeuxChiffres=[]
# i=1
# while i**2<100:
#     if len(str(i**2))==2:
#         carreDeuxChiffres.append(str(i**2))
#     i+=1

# listeCarré=[]
# for i in carreDeuxChiffres:
#     for j in carreDeuxChiffres:
#         if (int(i+j)**0.5)==int(int(i+j)**0.5):
#             listeCarré.append(int(i+j))