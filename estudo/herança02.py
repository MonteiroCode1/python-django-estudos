from herança01 import Animal

class Cachorro(Animal):

    def falar(self) -> str: # sobrescrita de metodo
        # super() ele acessa metodos e construtor do pai!
        metodo_pai = super().falar() # agr entendi pra que serve o super(), ele serve para chamar metodos do pai para filho!
        return  metodo_pai + " O cachorro Latiu"

cachorro = Cachorro("Bolinha")

print(cachorro.falar())
print(cachorro.nome)

# polimorfismo: é o mesmo metodo, mesmo nome com comportamentos diferentes!