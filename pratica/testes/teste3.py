from produto3 import Produto
um_produto = Produto(1, "mause", 24.50, 100)
# esta é a forma correta de acessar os atributos privados
print(f"codigo: {um_produto.get_codigo()}")
print(f"descrisão: {um_produto.get__descrisao()}")
print(f"Preço: {um_produto.get__preço()}")
print(f"quantidade em estoque: {um_produto.get__quantidade_estoque()}")
