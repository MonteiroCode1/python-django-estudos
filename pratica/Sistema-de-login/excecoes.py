class UsuarioJaLogadoExeption(Exception):
    def __init__(self, mensagem: str = "Error... Usuário Já Existente!...") -> None:
        self.mensagem = mensagem
    
    def __str__(self) -> str:
        return self.mensagem

class SenhaIncorretaExeption(UsuarioJaLogadoExeption):
    def __init__(self, mensagem = "Error... Senha Incorreta..."):
        super().__init__(mensagem)
    

