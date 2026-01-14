from datetime import datetime, date

from documento import Documento

class OficioCircular(Documento):

    def __init__(
        self,
        numero: int,
        data_criacao: datetime,
        resumo: str,
        texto: str,
        data_limite: datetime,
        destinatarios: list
    ) -> None:

        # chama o construtor da classe pai
        super().__init__(numero, data_criacao, resumo)

        self._texto = texto
        self._data_limite = data_limite
        self._destinatarios = destinatarios

    def __str__(self) -> str:
        resultado = super().__str__()
        resultado += f"Texto: {self._texto}\n"
        resultado += f"Data Limite Para Envio: {self._data_limite.strftime('%d/%m/%Y')}\n"
        resultado += "Destinatários:\n"
        resultado += ", ".join(self._destinatarios) + "\n"
        return resultado

    @property
    def texto(self) -> str:
        return self._texto

    @texto.setter
    def texto(self, texto: str) -> None:
        if texto is None or texto == "":
            print("Erro: um texto deve ser fornecido!")
        else:
            self._texto = texto

    @property
    def data_limite(self) -> datetime:
        return self._data_limite

    @data_limite.setter
    def data_limite(self, data_limite: datetime) -> None:
        if data_limite is None:
            print("Erro: uma data limite deve ser fornecida!")
        else:
            self._data_limite = data_limite

    @property
    def destinatarios(self) -> list:
        return self._destinatarios

    @destinatarios.setter
    def destinatarios(self, destinatarios: list) -> None:
        self._destinatarios = destinatarios

    def is_vencido(self) -> bool:
        hoje = date.today()
        return self._data_limite.date() < hoje
