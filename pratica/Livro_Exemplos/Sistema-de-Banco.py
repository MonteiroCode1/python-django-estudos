from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome: str, cpf: int) -> None:
        self.nome = nome
        self.cpf = cpf
    
    def __str__(self) -> str:
        resumo = f"Nome: {self.nome}\nCPF: {self.cpf}"
        return resumo

class Conta(ABC):
    def __init__(self, cliente: str, saldo: float) -> None:
        self._saldo = saldo # deve ser protegido e nao privado
        self.cliente = cliente
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass
    
    @property
    def saldo(self) -> float:
        return self._saldo

class ContaCorrente(Conta):
    def sacar(self, valor: float) -> bool:
        if (valor < 0 or valor > self._saldo):
            return False
        else:
            taxa_de_saque = ((0.26/100) * self._saldo)
            total = taxa_de_saque + valor
            self._saldo -= total
            return True

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        if (valor < 0 or valor > self._saldo):
            return False
        else:
            redimento = (0.5/100) * self._saldo
            self._saldo += redimento
            self._saldo -= valor
            return True            
            
pessoa = Cliente("Guilherme", 11176189352)
cc = ContaCorrente(pessoa, 300.00)
cc.sacar(30.00)

cp = ContaPoupanca(pessoa, 300)

cp.sacar(10)
print(cp.saldo)
print(pessoa)
    

