class Teste:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__imprimir()
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    
    def __imprimir(self) -> str:
        print(self.__nome)
    

teste = Teste("Monteiro")
teste.nome = "Guilherme"
print(teste.nome)