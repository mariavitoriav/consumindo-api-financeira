class Cotacao:

    def __init__(self, id: int = 1, dolar: float = 0.0, euro: float = 0.0,  timestamp: str = "") -> None:
        super().__init__()
        self.__id = id
        self.__dolar = dolar
        self.__euro = euro
        self.__timestamp = timestamp

    @property
    def id(self):
        return self.__id

    @property
    def dolar(self):
        return self.__dolar

    @property
    def euro(self):
        return self.__euro

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def cotacao(self) -> dict:
        return{
            'dolar': self.__dolar,
            'euro': self.__euro,
            'timestamp': self.__timestamp
        }

    def __str__(self) -> str:
        return f'{self.__timestamp}, $ {self.__dolar}, € {self.__euro}'



