from produto2 import Produto
umProduto = Produto(1, "BYD", 11.50, 50)
# a forma correta de alterar ou leitura de atributos privados é criando metodos.
print(f"codigo: {umProduto._Produto__quantidade_estoque}") # mesmo sendo privado vc pode acessar seus valores! Mas. Não é muito recomendado fazer isso!
print(f"descrisão: {umProduto._Produto__descriçao}")
print(f"preço: {umProduto._Produto__preço:.2f}")
print(f"codigo: {umProduto._Produto__codigo}")

