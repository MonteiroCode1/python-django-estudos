class QuickSort:
    def __init__(self, numeros: list) -> None:
        self.__numeros = numeros
        self.ordena()

    def ordena(self) -> None:
        self.__particiona(0, len(self.__numeros) - 1)

    def __particiona(self, inicio: int, fim: int) -> None:
        if fim - inicio > 0:
            pivo = self.__numeros[inicio]
            esquerda = inicio
            direita = fim

            while esquerda <= direita:
                while self.__numeros[esquerda] < pivo:
                    esquerda += 1

                while self.__numeros[direita] > pivo:
                    direita -= 1

                if esquerda <= direita:
                    self.__numeros[esquerda], self.__numeros[direita] = (
                        self.__numeros[direita],
                        self.__numeros[esquerda],
                    )
                    esquerda += 1
                    direita -= 1

            self.__particiona(inicio, direita)
            self.__particiona(esquerda, fim)

    @property
    def resultado(self) -> list:
        return self.__numeros
