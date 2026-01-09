from produto5 import Produto

um_produto = Produto(1, "mause", 200.00)
outro_produto = Produto(2, "Manitor", 150.25)

print(um_produto.preço)
print(outro_produto.preço)
um_produto.preço = 10.00
print(um_produto.preço)