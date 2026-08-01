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
            "comum": 0.5,
            "raro": 0.6,
            "épico": 1.1,
            "lendário": 1.7,
            "mítico":2
        }
        pesos = [70, 32, 9, 2, 0.5]
        nomes = ["espada","foice","faca","Machado","Adaga","Katana"]
        nome = choice(nomes)
        raridade = choices (list(qualidade.keys()),
                            weights= pesos,
                            k=1
                            )[0]
        danomin = 1
        danomax = int(qualidade[raridade] * turno)
        match raridade:
            case "épico":
                danomin = int(danomax * 0.25)
            case "lendário":
                danomin = int(danomax * 0.50)
            case "mítico":
                danomin = int(danomax * 0.80)
        if danomin <= 0 or danomax <= 0 :
            danomin = 1
            danomax = 2
        dano = random.randint(danomin,danomax)
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



