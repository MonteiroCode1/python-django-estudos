import  datetime

class OficioCircular:

    def __init__(self, numeros: int, data_criaçao: datetime, resumo: str, texto: str, data_limite: datetime, destinatario: list) -> None:
        self.__numeros = numeros
        self.__data_criaçao = data_criaçao
        self.__resumo = resumo
        self.__texto = texto
        self.__data_limite = data_limite
        self.__destinatario = destinatario
    
    def __str__(self) -> str:
        resultado = 'documento n.:' + self.__numeros + '\n'
        resultado += 'Data de Criação: ' + datetime.datetime.strftime(self.__data_criaçao, "%d/%m/%y") + '\n'
        resultado += 'resumo: ' + self.__resumo + '\n'
        resultado += 'texto: ' + self.__texto + '\n'
        resultado += 'Data Limite Para Envio: ' + self.__data_limite.strftime('%d/%m/%y') + '\n'
        resultado += 'Destinarios: \n'
        resultado += ', '.join(self.__destinatario) + '\n'
        return resultado