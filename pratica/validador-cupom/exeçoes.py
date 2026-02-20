class CupomExpiradoExeption(Exception):
    def __init__(self, mensagem: str = 'Este Cupom não é mais valido!...') -> None:
        self.mensagem = mensagem
    
    def __str__(self) -> str:
        return self.mensagem

class ValorMinimoExeption(CupomExpiradoExeption):
    def __init__(self, mensagem = 'Valor da Compra insuficiente para este cupom...'):
        super().__init__(mensagem)

