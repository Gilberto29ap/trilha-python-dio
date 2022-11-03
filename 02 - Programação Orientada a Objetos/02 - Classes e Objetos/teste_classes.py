import random




class Arma:
    def __init__(self, calibre, bore_speed):
        self.calibre = calibre
        self.bore_speed = bore_speed




class Ammunition:
    def __init__(self, calibre_ammunition, speed_base, peso):
        self.calibre_ammunition = calibre_ammunition
        self.speed_base = speed_base
        self.peso = peso


ar10 = Arma(".308", 780)
cbc_308_sniper = Ammunition(".308", 750, 175)
federal_308_HPBT = Ammunition(".308", 800, 175)

def velocidade_disparo(arma, ammunition):
    return (arma.bore_speed + ammunition.speed_base)/2

velocidade1 = velocidade_disparo(ar10, cbc_308_sniper)
velocidade2 = velocidade_disparo(ar10, federal_308_HPBT)

print(ar10.calibre)

ar15 = Arma(".308", 900)

print(velocidade1)
print(velocidade2)


    

