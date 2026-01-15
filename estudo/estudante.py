class Estudante:
    def __init__(self, matricula: int) -> None:
        self._matricula = matricula
    
    def __str__(self) -> str:
        resultado = f"Matricula: {self._matricula}\n"
        return resultado
    
    @property
    def matricula(self) -> str:
        return self._matricula