from memoria import Memoria

class Cache(Memoria):
    def __init__(self, tamanho, ram):
        Memoria.__init__(self, tamanho)
        self.ram = ram
        self.memoria = [0] * self.tamanho()
        self.ender_inicial = 0
        self.ender_final = 0
    
    def read(self, ender):
        """
        Le os valores contidos na cache.

        :param ender: int

        :return int Valor contido no endereço passado
        """
        # Tem o endereço no cache? Se não copiar os endereços da memoria ram para a cache
        self.ram.verifica_endereco(ender)
        if(self.ender_inicial <= ender and ender < self.ender_final):
            # Encontrei, HIT o cache
            print(f'Cache HIT: {ender}')
            l = self.ender_inicial
            for i in range(len(self.memoria)):
                if(ender == l + i):
                    return self.memoria[i]
                
        # Não encontrou, então retorna CACHE MISS
        print(f'Cache MISS: {ender}')
        j = ender
        self.ender_inicial = j

        # Copia os dados da RAM para a cache
        for i in range(len(self.memoria)):
            self.memoria[i] = self.ram.read(j)
            j = j + 1
        self.ender_final = self.ender_inicial + len(self.memoria)
        return self.ram.read(ender)

    def write(self, ender, val):
        """
        Escreve um valor em um endereço na Cache.

        :param ender: int
        :param val: int
        """

        # Tem o endereço no cache? Se não copiar os endereços da memoria ram para a cache
        self.ram.verifica_endereco(ender)
        if(self.ender_inicial <= ender and ender < self.ender_final):
            # Encontrei, HIT o cache
            print(f'Cache HIT: {ender}')
            l = self.ender_inicial
            for i in range(len(self.memoria)):
                if(ender == l + i):
                    self.memoria[i] = val
                    return 
        
        # Quando der miss, tem que mandar pra RAM os valores da CACHE, e copiar o novo bloco
        print(f'Cache MISS: {ender}')
        j = self.ender_inicial
        y = ender
        
        # Copia os dados da RAM para a cache
        # E repassa o bloco da cache par a RAM
        for i in range(len(self.memoria)):
            # Manda pra RAM
            self.ram.write(j, self.memoria[i])

            # Adicionei o try e except, pois o bloco de memoria da cache acaba passando o tamanho da RAM
            # Isso se dá no cache MISS do 126, endereços [126, 127, 128, 129, 130, 131, 132, 133]
            #                                          RAM ACABA ^| 
            try:
                # Copia da RAM
                self.memoria[i] = self.ram.read(y)
            except:
                self.memoria[i] = 0
            j = j + 1
            y = y + 1
        self.ender_inicial = ender
        self.ender_final = self.ender_inicial + len(self.memoria)
        self.ram.write(ender, val)