import sys

class IO:
    def __init__(self, entrada = sys.stdin, saida = sys.stdout):
        # Construtor
        self.entrada = entrada
        self.saida = saida

    def output(self, msg):
        print(msg, file=self.saida, end='')