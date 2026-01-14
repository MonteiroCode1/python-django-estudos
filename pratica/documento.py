from datetime import datetime


class Documento:

    def __init__(self, numero: int, data_criacao: datetime, resumo: str) -> None:
        self._numero = numero
        self._data_criacao = data_criacao
        self._resumo = resumo

    def __str__(self) -> str:
        resultado = f"Documento n.: {self._numero}\n"
        resultado += f"Data de Criação: {self._data_criacao.strftime('%d/%m/%Y')}\n"
        resultado += f"Resumo: {self._resumo}\n"
        return resultado

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def data_criacao(self) -> datetime:
        return self._data_criacao

    @property
    def resumo(self) -> str:
        return self._resumo

    @resumo.setter
    def resumo(self, resumo: str) -> None:
        if resumo is None or resumo == "":
            print("Erro: o resumo precisa ter algum conteúdo!")
        else:
            self._resumo = resumo
