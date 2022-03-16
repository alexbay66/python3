from hashlib import algorithms_available
import random
from tabnanny import check


has_cash = bool(random.randint(0, 1))
has_card = bool(random.randint(0, 1))
has_check = bool(random.randint(0, 1))

print('has_casd:' , has_cash)
print('has_card:' , has_card)
print('has_check:' , has_check)

if has_cash or has_card or has_check:
 print("oui courses") 
 if has_cash:
     print("oui cash")
     if has_card:
         print("oui carte")
         if has_check:
             print("oui cheque")
else:
 print("non courses")






 age = random.randint(0, 100)

 # 0-5 bébé
 #6-11 enfant
 #12-25 junior
 #26-59 adulte
 #60+ senior

if age <= 5:
     print('bébé')
if 6 <= age <= 11:
    print('enfant')
if 12 <= age <= 25:
     print('junior')
if 26 <= age <= 59:
         print('adulte')
    # on peut aussi faire un "else" pour interceder les cas ou l'age >= 60
if 60:
      print('senior')