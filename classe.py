from voiture import Voiture 
from camion import Camion

c1 = Camion("Scania", "?", "diesel",  0)
print(c1)
c2 = Camion("Mercedes", "?", "diesel", 0)
print(c2)


v1 = Voiture("BMW", "Série 5 ", "Diesel", 0, "Berline")
# v1 affiche "<voiture.Voiture objet at 0x7fef1ecfc910>" si la fonction __str__() n'a pas été définie
print(v1)
# Il ne faut pas afficher directement ces vériables car elles sont considérés
# Cest-à-dire qu'elles sont toutes préfixées d'un underscore "_" 
#print(v1.marque, v1.modele, v1.carburant, v1.type_carrosserie, v1.get_vitesse())
print(v1.get_marque())
print(v1.get_modele())
print(v1.get_carburant())
print(v1.get_type_carroserie())

print(v1.get_vitesse())
v1.set_vitesse (10)
print(v1.get_vitesse)

print(v1.get_marque)
v1.get_marque = "laba"
print(v1.get_vitesse())

v2 = Voiture("Ford", "Mustang 68", "essence", 0,"muscle car")
print(v2)
print(v2.get_vitesse())
#transmettre une valeur de type autre que int génère l'erreur "Exception"
v2.set_vitesse (50)
print(v2.get_vitesse())
print(v1.get_vitesse())
