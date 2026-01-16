from abc import ABC, abstractmethod

class Fucionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self._nome = nome
        self._salario = salario
    
    def __str__(self) -> str:
        resultado = f"Nome: {self._nome}\n"
        resultado += f"Salario: {self._salario}"
        return resultado
    
    @classmethod
    @abstractmethod
    def calcular_salario(self) -> float:
        pass
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class FucionarioCLT(Fucionario):
    def __init__(self, nome, salario):
        super().__init__(self, nome, salario)
    
    def calcular_salario(self) -> float:
        salario_final = salario * 1.1