# aqui vai a implementação da classe Produto, o nome da classe começa com letra maiúscula por convenção!
class Produto:
    def __init__(self, codigo: int, descrisao: str, preço:float, quantidade_estoque: int) -> None:
        self.codigo = codigo
        self.descrisao = descrisao
        self.preço = preço
        self.quantidade_estoque = quantidade_estoque
    def entrada_estoque(self, quantidade: int) -> None:
        self.quantidade_estoque += quantidade
    def saida_estoque(self, quantidade: int) -> None:
        self.quantidade_estoque -= quantidade
    def visualizar_quantidade_estoque(self) -> None:
        print(f"Quantidade em estoque: {self.quantidade_estoque}")