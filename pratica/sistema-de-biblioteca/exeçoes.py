class LivroIndisponivelError(Exception):
    def __init__(self, mensagen: str) -> None:
        self.mensagen = mensagen

    def __str__(self) -> str:
        return self.mensagen

class LivroNaoExisteError(LivroIndisponivelError):
    def __init__(self, mensagen: str) -> None:
        self.mensagen = mensagen
    
    def __str__(self) -> None:
        return self.mensagen