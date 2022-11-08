class Ambiente:
    def __init__(self, dens_att, temperatura):
        self.dens_att = dens_att
        self.temperatura = temperatura
        def calc_coeficiente(self):
# calculando dens att para coeficiente, quanto maior o valor, menor o arrasto, base 0
            coeff_dens_att = -self.dens_att/1000
# calculando temperatura para coeficiente, quanto maior o valor, menos arrasto, base 25       
            coeff_temperatura = (25-self.temperatura)/1000

            ca = 1 + coeff_dens_att + coeff_temperatura

            return ca

        self.coeffiente_ambiente = calc_coeficiente(self)

# # calcular coeficiente de ambiente, quanto maior o valor maior o arrasto, float com 3 casas decimais aproximado de 1.000
#     def calc_coeficiente(self):
# # calculando dens att para coeficiente, quanto maior o valor, menor o arrasto, base 0
#         coeff_dens_att = -self.dens_att/1000
# # calculando temperatura para coeficiente, quanto maior o valor, menos arrasto, base 25       
#         coeff_temperatura = (25-self.temperatura)/1000

#         ca = 1 + coeff_dens_att + coeff_temperatura
        
#         print(f"calculando coeficiente de ambiente:  {ca}")

#         return ca

    



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

print(pt100 )

sertao = Ambiente(200, 40)

print(sertao.coeffiente_ambiente)