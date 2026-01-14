from Classes.produto1 import Produto

umProduto = Produto(1, "son automativo", 574.20, 8)
umProduto.entrada_estoque(2.0)
umProduto.visualizar_quantidade_estoque()
umProduto.saida_estoque(4)
umProduto.visualizar_quantidade_estoque()