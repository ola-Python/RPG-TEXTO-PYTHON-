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
    def gerarArma(cls,turno=5,raridade=None):

        qualidade ={
            "comum": 0.5,
            "raro": 0.6,
            "épico": 1.1,
            "lendário": 1.7,
            "mítico":2
        }

        cores_raridade = {
            "comum": "[bold]",
            "raro": "[blue]",
            "épico": "[purple]",
            "lendário": "[#FFEB00]",
            "mítico": "[#FF1812 bold on black]"
        }
        pesos = [70, 32, 9, 2, 0.5]
        nomes = ["espada","foice","faca","Machado","Adaga","Katana"]
        nome = choice(nomes)
        if raridade == None :
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
        nome = f"{cores_raridade[f"{raridade}"]}{nome}[/]"
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

    @classmethod
    def gerarAnel(cls, turno=5, raridade=None):

        qualidade = {
            "comum": 0.5,
            "raro": 0.6,
            "épico": 1.1,
            "lendário": 1.7,
            "mítico": 2
        }

        cores_raridade = {
            "comum": "[bold]",
            "raro": "[blue]",
            "épico": "[purple]",
            "lendário": "[#FFEB00]",
            "mítico": "[#FF1812 bold on black]"
        }
        pesos = [70, 32, 9, 2, 0.5]
        nomes = ["anel mágico", "colar sagrado", "anel dourado", "anel diabolico", "anel de fogo",
                 "anel de gelo"]
        nome = choice(nomes)
        if raridade == None:
            raridade = choices(list(qualidade.keys()),
                               weights=pesos,
                               k=1
                               )[0]
        agimin = 1
        dano = 0
        agimax = int(qualidade[raridade] * turno)
        match raridade:
            case "épico":
                agimin = int(agimax * 0.25)
            case "lendário":
                danomax = int(0.4 * agimax)
                if danomax < 1 :
                    danomax = 1
                dano = random.randint(1,danomax)

                agimin = int(agimax * 0.50)
            case "mítico":
                agimin = int(agimax * 0.80)
                danomax = int(0.6 * agimax)
                if danomax < 1:
                    danomax = 1
                dano = random.randint(1, danomax)
        if agimin <= 0 or agimax <= 0:
            agimin = 1
            agimax = 2
        agilidade = random.randint(agimin,agimax)
        valor = int(agilidade * 0.7)
        nome = f"{cores_raridade[f"{raridade}"]}{nome}[/]"
        if valor <= 0: valor = 1
        tipo = "anel"
        return cls(
            nome=nome,
            dano=dano,
            valor=valor,
            agilidade=agilidade,
            tipo=tipo,
            raridade=raridade
        )



