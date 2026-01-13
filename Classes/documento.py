import datetime
class Documento:
    def __init__(self, numeros: int, data_criaçao: datetime, resumo: str) -> None:
        self.__numeros = numeros
        self.__data_criaçao = data_criaçao
        self.__resumo = resumo
    
    def __str__(self) -> str:
        resultado = '\nDocumento n.:' + self.__numeros + '\n'
        resultado += 'Data de Criação: ' + datetime.datetime.strftime(self.__data_criaçao, '%d/%m/%y') + '\n'
        resultado += 'resumo: ' + self.__resumo + '\n' 
        return resultado
    @property
    def numero(self) -> str:
        return self.__numeros

    @property
    def data_criaçao(self) -> datetime:
        return self.__data_criaçao
    
    @property
    def resumo(self) -> str:
        return self.__resumo
    
    @resumo.setter
    def resumo(self, resumo: str) -> None:
        if resumo == '' or resumo == None:
            print("Error: o resumo precisa ter algum conteudo!")
        else:
            self.__resumo = resumo
    
         