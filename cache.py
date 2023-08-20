from memoria import Memoria

class Cache(Memoria):
    def __init__(self, tamanho, ram):
        Memoria.__init__(self, tamanho)
        self.ram = ram
        self.memoria = [0] * self.tamanho()
    
    def read(self, ender):
        # Tem o endereço no cache? Se não copiar os endereços da memoria ram para a cache
        for val in self.memoria:
            if( val == ender):
                # Encontrei, HIT o cache
                print(f'Cache HIT: {ender}')
                return self.ram.read(ender)
        
        print(f'Cache MISS: {ender}')
        j = ender
        for i in range(len(self.memoria)):
            self.memoria[i] = j
            j = j + 1
        
        return self.ram.read(ender)

    def write(self, ender, val):
        # Tem o endereço no cache? Se não copiar os endereços da memoria ram para a cache
        for val in self.memoria:
            if( val == ender):
                # Encontrei, HIT o cache 
                print(f'Cache HIT: {ender}')
                return self.ram.write(ender, val)
        
        print(f'Cache MISS: {ender}')
        j = ender
        for i in range(len(self.memoria)):
            self.memoria[i] = j
            j = j + 1
        
        return self.ram.write(ender, val)