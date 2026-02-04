# Sitema de Fucionario
from abc import ABC, abstractmethod

#Classe Pai
class Fucionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self._nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self) -> float:
        pass
    
    @abstractmethod
    def salario_total(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Nome: {self._nome}\nSalario: {self.salario}"
    
    @property
    def nome(self) -> str:
        return self._nome
    
# classe filha Gerente

class Gerente(Fucionario):

    def calcular_bonus(self) -> float|bool:
        if (self.salario < 0):
            return False
        else:
            decimal = 20 / 100
            bonus = self.salario * decimal
            return bonus
            
    
    def salario_total(self) -> float:
        if (self.salario < 0):
            return False
        else:
            self.salario += self.calcular_bonus()
            return self.salario
            

# classe filha Programador

class Programador(Fucionario):

    def calcular_bonus(self) -> float|bool:
        if (self.salario < 0):
            return False
        else:
            decimal = 10 / 100
            bonus = self.salario * decimal
            return bonus
            
    
    def salario_total(self) -> float:
        if (self.salario < 0):
            return False
        else:
            self.salario += self.calcular_bonus()
            return self.salario
            

g = Gerente("Guilherme", 5000)
p = Programador("Gabriel", 3000)

fucionarios = [g, p]
for d in fucionarios:
    print(f"Nome: {d.nome}, Bonus: {d.calcular_bonus()}")


#print(g)
#print("Bônus:", g.calcular_bonus())
#print(f"Salario total: {g.salario_total()}\n")

#print(p)
#print("Bônus:", p.calcular_bonus())
#print(f"Salario Total: {p.salario_total()}")
