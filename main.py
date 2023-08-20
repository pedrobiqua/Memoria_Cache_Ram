import sys
from es import IO
from ram import RAM
from cache import Cache
from cpu import CPU
from erros import EnderecoInvalido

def main():
    try:
        io = IO()
        ram = RAM(7)
        cache = Cache(8, ram)
        cpu = CPU(cache, io)

        inicio = 10
        ram.write(inicio, 118)
        ram.write(inicio + 1, 130)
        cpu.run(inicio)
    except EnderecoInvalido as e:
        print("Endereço inválido:", e.ender, file=sys.stderr)


if __name__ == '__main__':
    main()
