from pessoa import Pessoa
from estudante import Estudante

class Residente(Pessoa, Estudante):
    def __init__(self, nome: str, idade: int, matricula: int) -> None:
        Pessoa.__init__(self, nome, idade)
        Estudante.__init__(self, matricula)
    
    def __str__(self) -> str:
        resultado = Pessoa.__str__(self)
        resultado += Estudante.__str__(self)
        return resultado