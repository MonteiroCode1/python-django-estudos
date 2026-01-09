class Produto:
    def __init__(self, codigo: int, descriçao: str, preço: float) -> None:
        # atributos privados!
        self.__codigo = codigo
        self.__descriçao = descriçao
        self.__preço = preço
        self.__quantidade_estoque = 0
    
    def entrada_estoque(self, valor: int) -> None:
        self.__quantidade_estoque += valor
    
    def saida_estoque(self, valor: int) -> None:
        self.__quantidade_estoque -= valor

    def visualizar_quantidade_estoque(self) -> None:
        print(f"Quantidade em estoque: {self.__quantidade_estoque}")
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def descriçao(self) -> str:
        return self.__descriçao
    
    @descriçao.setter
    def descriçao(self, valor: str) -> None:
        self.__descriçao = valor
    
    @property
    def preço(self) -> float:
        return self.__preço
    
    @preço.setter
    def preço(self, valor: float) -> None:
        if valor <= 0:
            print("Erro: Somente Numeros Positivos!")
        else:
            self.__preço = valor
            
    @property
    def quantidade_estoque(self) -> float:
        return self.__quantidade_estoque
                                            