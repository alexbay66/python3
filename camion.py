from vehicule import Vehicule
class Camion(Vehicule):
    def __init__(self, marque: str, modele: str,  carburant: str, vitesse: int):
        super().__init__(marque, modele, carburant, vitesse)


    def __str__(self):
            return super().__str__() + f"{self._ptac}"

    def get_ptac(self) -> float:
            return self.ptac
        
    def set_place(self, ptac: float):
        if type(ptac) != float:
                raise Exception("le ptac doit etre un float")
            
        self._ptac = ptac

