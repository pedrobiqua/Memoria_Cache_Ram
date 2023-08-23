from memoria import Memoria

class RAM(Memoria):
    def __init__(self, k):
        Memoria.__init__(self, 2**k)
        self.memoria = [0] * self.tamanho()

    def read(self, ender):
        """
        Le os valores contidos na RAM.

        :param ender: int

        :return int Valor contido no endereço passado
        """
        super().verifica_endereco(ender)
        return self.memoria[ender]

    def write(self, ender, val):
        """
        Escreve um valor em um endereço na RAM.

        :param ender: int
        :param val: int
        """
        super().verifica_endereco(ender)
        self.memoria[ender] = val