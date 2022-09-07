class Vehicule: 
    """
    cette classe represente un véhicule.
    Attention, c'est une classe abstraite.
    elle est destinée a etre étendue par des classes enfants.
    """
# le _ indique que la variable est privé
_acceleration = 10 


def __init__(self, marque: str, modele: str,  carburant: str, vitesse: int):
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        self.set_vitesse(vitesse)

def __str__(self):
        return f"{self._marque} {self._modele} {self._carburant} {self._vitesse}"

def get_marque(self) -> str:
        return self._marque

def get_modele(self) -> str:
        return self._modele

def get_carburant(self) -> str:
        return self._carburant
        
def get_vitesse(self) -> int:
        return self._vitesse

def set_vitesse(self, vitesse: int):
        if type(vitesse) is not int:
            raise Exception("la vitesse doit etre un int")
        elif vitesse > 220:
            raise Exception("la vitesse max est de 200")
        elif vitesse <-10:
            raise Exception("la vitesse min est de -10")
            
        self._vitesse = vitesse
    
def accelerer(self):
        vitesse = self.get_Vitesse()
        vitesse += self._acceleration
        self.set_vitesse(vitesse)

def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -= self._acceleration
        self.set_vitesse(vitesse)
