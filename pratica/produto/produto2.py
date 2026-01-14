# aqui vai a implementação da classe Produto, o nome da classe começa com letra maiúscula por convenção!
class Produto:
    def __init__(self, codigo: int, descriçao: str, preço:float, quantidade_estoque: int) -> None:
        self.__codigo = codigo
        self.__descriçao = descriçao # o __ no inicio do atributo torna ele Privado
        self.__preço = preço
        self.__quantidade_estoque = quantidade_estoque
    def entrada_estoque(self, quantidade: int) -> None:
        self.__quantidade_estoque += quantidade
    def saida_estoque(self, quantidade: int) -> None:
        self.__quantidade_estoque -= quantidade
    def visualizar_quantidade_estoque(self) -> None:
        print(f"Quantidade em estoque: {self.__quantidade_estoque}")