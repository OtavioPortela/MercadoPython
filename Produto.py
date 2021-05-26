from utils.helper import Formata_float_str_moeda

class Produto:
    Contador: int = 1

    def __init__(self: object, nome: str, preco:float) -> None:
        self.__codigo: int = Produto.Contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.Contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f'Codigo: {self.codigo} \nNome: {self.nome} \nPreço: {Formata_float_str_moeda(self.preco)}'


