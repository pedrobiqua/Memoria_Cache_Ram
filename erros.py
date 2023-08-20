# Exceção (erro)
class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender

    def __repr__(self):
        return self.ender