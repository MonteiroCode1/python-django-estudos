# Classe que demonstra o uso variaveis estáticas
# Classe que implementa o algaritmo de ordenaçao QuickSort 
class Jogador:
    # Variável de CLASSE
    # Ela pertence à classe Jogador, não aos objetos
    # Todos os jogadores compartilham esse mesmo valor
    numero_jogadores = 0

    def __init__(self, nome: str) -> None:
        # Atributo de OBJETO
        # Cada jogador terá seu próprio nome
        self.nome = nome

        # Acessando a CLASSE para alterar a variável de classe
        # Sempre que um jogador é criado, aumenta o contador
        Jogador.numero_jogadores += 1

    def sair(self) -> None:
        # Quando o jogador sai, diminuímos o contador global
        Jogador.numero_jogadores -= 1

        # self.nome -> pertence ao objeto
        # Jogador.numero_jogadores -> pertence à classe
        print(
            f"O jogador {self.nome} se desconectou. "
            f"restam {Jogador.numero_jogadores} jogadores."
        )
    
    def imprimir_quantidade_jogadores(self) -> None:
        # Esse método mostra quantos jogadores existem no total
        # Ele usa apenas a variável de classe
        print(
            f"Neste momento, há {Jogador.numero_jogadores} jogadores conectados."
        )

