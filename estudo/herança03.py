from herança01 import Animal
from herança02 import Cachorro

class Gato(Animal):
    
    def falar(self):
        metodo_pai = super().falar()
        return metodo_pai + ". O gato miou"

a = [Cachorro("Bolinha"), Gato("René")]
for e in a:
    print(e.falar())