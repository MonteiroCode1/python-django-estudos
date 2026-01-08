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
    # criando metodos de leitura e mundanças
    # __codigo!
    def get_codigo(self) -> int:
        return self.__codigo
    def set_codigo(self, codigo: int) -> None:
        self.__codigo = codigo
    
    # __descrição
    def get__descrisao(self) -> str: # para leitura de dados privados!
        return self.__descriçao
    def set_descrisao(self, descrisao: str) -> None: # para Modificação de dados privados !
        self.__descriçao = descrisao
    
    #__preço
    def get__preço(self) -> float:
        return self.__preço
    def set__preço(self, preço: float) -> None:
        self.__preço = preço
    
    #__quantidade_estoque
    def get__quantidade_estoque(self) -> int:
        return self.__quantidade_estoque
    def set__quantidade_estoque(self, quantidade_estoque: int) -> None:
        self.__quantidade_estoque = quantidade_estoque
    
