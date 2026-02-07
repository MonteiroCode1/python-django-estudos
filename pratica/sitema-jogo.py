from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome: str, vida: int, ataque: int) -> None:
        self._nome = nome
        self._vida = vida
        self._ataque = ataque
        if (vida < 0):
            print("Vida Nao Pode ser Negativo...")
    
    @abstractmethod
    def ataque(self) -> int:
        pass
    
    def mostrar_estatus(self) -> str:
        return f"Nome: {self._nome}\nVida: {self._vida}\nAtaque {self._ataque}"
        
    @abstractmethod    
    def receber_dano(self, dano: int) -> None:
        pass
    
class Mago(Personagem):
    def __init__(self, nome: str, vida: int, ataque: int) -> None:
        super().__init__(nome, vida, ataque)
    
    def ataque(self) -> int: #ataque especia
        bonus = self._ataque * 0.4
        dano = self._ataque + bonus
        return dano
    
    def receber_dano(self, valor: int) -> str:
        self._vida -= valor
        if (self._vida <= 0):
            return "O Mago supremo morreu na batalha..."
        else:
            return "sangramento..."
    
    def lancar_magia(self): # ataque Normal
        return self._ataque

tony = Mago("Doutor Estranho", 100, 40)
print(tony.receber_dano(50))
print(tony.mostrar_estatus())
print(tony.ataque())
print(tony.lancar_magia())