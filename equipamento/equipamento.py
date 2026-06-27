import random
from random import choice,choices
class Equipamento :
    def __init__(self,nome,dano=0,valor=0,agilidade=0,tipo=None,raridade=None):
        self.nome = nome
        self.dano = dano
        self.valor = valor
        self.agilidade = agilidade
        self.tipo = tipo  #arma  anel  armadura
        self.raridade = raridade
    @classmethod
    def gerarEquipamento(cls,turno=5):

        qualidade ={
            "comum": 1,
            "raro": 1.3,
            "épico": 1.9,
            "lendário": 3.4,
            "mítico":5
        }
        pesos = [70, 20, 90, 2, 0.5]
        nomes = ["espada","foice","faca","Machado","Adaga","Katana"]
        nome = choice(nomes)
        raridade = choices (list(qualidade.keys()),
                            weights= pesos,
                            k=1
                            )[0]
        danomax = int(qualidade[raridade] * turno)
        dano = random.randint(1,danomax)
        valor = int(dano * 0.7)
        if valor <= 0: valor = 1
        agilidade = 0
        tipo ="arma"
        return cls(
            nome=nome,
            dano=dano,
            valor=valor,
            agilidade=0,
            tipo="arma",
            raridade=raridade
        )


espada = Equipamento.gerarEquipamento(turno=65)
espada2 = Equipamento.gerarEquipamento(turno=65)
espada3 = Equipamento.gerarEquipamento(turno=65)
espada4 = Equipamento.gerarEquipamento(turno=65)

equipamentos = [espada,espada2,espada3,espada4]
for equip in equipamentos :
    print(f"{equip.nome} {equip.raridade} tem {equip.dano} de dano e custa {equip.valor}")
