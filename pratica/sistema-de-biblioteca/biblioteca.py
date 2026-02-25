from exeçoes import LivroIndisponivelError, LivroNaoExisteError

class Livro:
    def  __init__(self, titulo: str, autor: str, qtd: int) -> None:
        self._titulo = titulo
        self._autor = autor
        self._qtd = qtd
    
    def emprestar(self, titulo: str) -> None:
        if titulo != self._titulo:
            raise LivroNaoExisteError("Livro Não existe...")
        if self._qtd == 0:
            raise LivroIndisponivelError("Livro esta indisponivel...")
        else:
            self._qtd -= 1
    
    def devolver(self, titulo: str) -> None:
        if self._titulo != titulo:
            raise LivroNaoExisteError()
        self._qtd += 1
    
    def __str__(self) -> str:
        return self._titulo
    

class Biblioteca:
    def __init__(self) -> None:
        self._lista = []
    
    def adicionar_livro(self, livro: str) -> None:
        self._lista.append(livro)

    def emprestar_livro(self, livro: str) -> None:
        if livro in self._lista:
            e = Livro()
            e.emprestar(livro)
    
    def devolver_livro(self, livro: str) -> None:
        if livro in self._lista:
            e = Livro()
            e.devolver(livro)
        

bib = Biblioteca()

livro1 = Livro("Python POO", "Gui Dev", 2)
livro2 = Livro("JavaScript Ninja", "JS Master", 1)

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

bib.emprestar_livro("Python POO")
bib.emprestar_livro("Python POO")
bib.emprestar_livro("Python POO")  # deve lançar exceção

#bib.devolver_livro("Python POO")
            
    