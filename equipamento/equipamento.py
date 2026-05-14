class Equipamento :
    def __init__(self,nome,dano=0,valor=0,agilidade=0,tipo=None):
        self.nome = nome
        self.dano = dano
        self.valor = valor
        self.agilidade = agilidade
        self.tipo = tipo  #arma  anel  armadura