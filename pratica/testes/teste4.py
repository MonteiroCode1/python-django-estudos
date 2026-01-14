from produto3 import Produto
um_produto = Produto(1, "mause", 100.00)
outro_produto = Produto(2, "manitor", 500.00)

# entrada de dados
um_produto.entrada_estoque(30)
outro_produto.entrada_estoque(50)

print("Mause estoque: ",um_produto.get__quantidade_estoque())
print("manitor estoque: ",outro_produto.get__quantidade_estoque())

um_produto.set__preço(0)