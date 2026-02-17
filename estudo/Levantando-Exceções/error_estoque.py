#Criando uma exceção
class EstoqueInsuficienteException(Exception):
    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem

    def __str__(self) -> str:
        return self.mensagem
