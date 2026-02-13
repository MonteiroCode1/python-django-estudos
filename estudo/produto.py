# alguns cenarios de erros
# como lidar com erros 
class Produto:
    def __init__(self, codigo: int, descriçao: str, preço: float) -> None:
        self.__codigo = codigo
        self.__descriçao = descriçao
        self.__preço = preço
        self.__quantidade_estoque = 0

    def entrada_estoque(self, quantidade: int) -> None:
        self.__quantidade_estoque += quantidade
    
    def saida_estoque(self, quantidade: int) -> None:
        self.__quantidade_estoque -= quantidade
    
    def visualizar_estoque(self) -> None:
        print(f"Quantidade em estoque: {self.__quantidade_estoque}")

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def descriçao(self) -> str:
        return self.__descriçao
    
    @descriçao.setter
    def descriçao(self, descriçao: str) -> None:
        self.__descriçao = descriçao

    @property
    def preço(self) -> float:
        return self.__preço
    
    @preço.setter
    def preço(self, preço: float) -> None:
        if preço <= 0:
            print("Error... Preço não pode ser menor ou igual a Zero!")
        else:
            self.__preço = preço
    
    @property
    def quantidade_estoque(self) -> int:
        return self.__quantidade_estoque
    

tecnologia = Produto(1, "Notebook Lenovo ideapad3i", 2500.00)

tecnologia.entrada_estoque(20)
tecnologia.visualizar_estoque()
tecnologia.descriçao
tecnologia.saida_estoque(15)
tecnologia.visualizar_estoque()
