class arma:
    def __init__(self, peso = 300, comprimento = 23):
        self.peso = peso
        self.comprimento = comprimento
        

    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class equipamento:
    def __init__(self, espaco_ocupado = 4):
        self.espaco_ocupado = espaco_ocupado



class arma_fogo(arma):
    def __init__(self, calibre, nro_canos = 1, **kw):
        self.nro_canos = nro_canos
        self.calibre = calibre
        super().__init__(**kw)


    def atirar(self):
        print("Bam!")

class Pistola(arma_fogo, equipamento):
    def __init__(self, capacidade_carregador, espaco_ocupado, **kw):
        super().__init__(**kw)
        self.espaco_ocupado = espaco_ocupado
        self.capacidade_carregador = capacidade_carregador
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

pistola1 = arma_fogo(1,".40", peso=400, comprimento = 20)

pt100 = Pistola(capacidade_carregador=10, calibre=".40", peso=400, comprimento = 25, espaco_ocupado=5)

print(pt100)
