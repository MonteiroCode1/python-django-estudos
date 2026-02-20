from exeçoes import CupomExpiradoExeption, ValorMinimoExeption

class Carrinho:
    def __init__(self, total_compra: float, cupom_ativo: str = 'PYTHON20', valor_minimo_cupom: float = 100.0):
        self.total_compra = total_compra
        self.cupom_ativo = cupom_ativo
        self.valor_minimo_cupom = valor_minimo_cupom
    
    def aplicar_cupom(self, nome_cupom: str) -> None:
        if (nome_cupom != self.cupom_ativo):
            raise CupomExpiradoExeption()
        if (self.total_compra < self.valor_minimo_cupom):
            raise ValorMinimoExeption()
        self.total_compra -= 20
        print('cumpom Aplicado')

compras = Carrinho(200.00)

try:
    compras.aplicar_cupom('PYTHON20')

except CupomExpiradoExeption as e:
    print(e)

except ValorMinimoExeption as e:
    print(e)

else:
    print('Tudo Certo... Carregando Dados!')
    print(f'Cumpom Aplicado: ficou por {compras.total_compra:.2f}')


finally:
    print('obg por nos visita!')
        
