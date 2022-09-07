from vehicule import Vehicule

class Voiture(Vehicule):

    _accelaration = 20

def __init__(self, marque: str, modele: str, carburant: 
        str, vitesse: int, type_carrosserie: str):
        super().__init__(marque,modele,carburant,vitesse)
        self._type_carrosserie = type_carrosserie
        


def __str__(self):
    return super().__str__() + f" {self._type_carrosserie} "
    
    

def get_type_carroserie(self) -> str:
        return self._type_carrosserie

