class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def falar(self) -> str:
        return "O animal Falou"