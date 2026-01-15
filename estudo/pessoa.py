class Pessoa:
    
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
    
    def __str__(self) -> str:
        resultado = f"Nome: {self._nome}\n"
        resultado += f"Idade: {self._idade}\n"
        return resultado
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade