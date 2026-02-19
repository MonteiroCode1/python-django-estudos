from excecoes import UsuarioJaLogadoExeption, SenhaIncorretaExeption

class SistemaLogin:
    def __init__(self) -> None:
        self.usuario_logado = False
    
    def fazer_login(self, senha_digitado: int) -> None:
        if self.usuario_logado == True:
            raise UsuarioJaLogadoExeption()
        
        if senha_digitado != 1234:
            raise SenhaIncorretaExeption()
    
    print("Analizando Dados...")

sistema_login = SistemaLogin()

try:
    sistema_login.fazer_login(1234)

except UsuarioJaLogadoExeption as e:
    print(e)

except SenhaIncorretaExeption as e:
    print(e)

else:
    sistema_login.usuario_logado = True
    print("Seja Bem Vindo!")

finally:
    print("Sitema Concluido!")


