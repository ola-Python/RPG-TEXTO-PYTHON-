import random
from random import choices,randint,uniform

import som
from interface.funcoes import mostrar_mensagem
from jogador import Jogador
from partida import Partida


def upgrade(jog:Jogador) :

    upgrades = { #nome do upgrade e a chance de vim
        "dano no dado" : 30,
        "dano bonus" : 15,
        "moeda bonus":15,
        "agilidade bonus":30,
    }

    if jog.sorte < 1.6 :
        upgrades["sorte"] = 10

    if jog.critico < 3.0 :
        upgrades["critico"] = 15
    if jog.chancecritico < 3 :
        upgrades["chance critico"] = 10

    melhorias = { #nome do upgrade + bonus
        "dano no dado" : [2,6],
        "dano bonus" : [1,4],
        "moeda bonus":[2,7],
        "agilidade bonus":[2,6],
        "sorte" : [0.1,0.3],
        "chance critico" : [1,2],
        "critico" : [0.2,0.5]
    }

    opcs = {}

    for i in range(3) : #vai escolher 3 upgrades aleatorios

        nomes = list(upgrades.keys())
        pesos = list(upgrades.values())

        escolha = choices(nomes,pesos,k=1)[0]

        if escolha not in ["sorte","critico"] :
            opcs[escolha] = randint(melhorias[escolha][0],melhorias[escolha][1])
        else :
            opcs[escolha] = round(uniform(melhorias[escolha][0], melhorias[escolha][1]), 1)

        del upgrades[escolha]

    opcsValores = list(opcs.values())
    texto = ""
    for i,opc in enumerate (opcs) : #mostrar os upgrades
        if opc  != "chance critico" :
            texto += f"[{i}] {opc} + {opcsValores[i]}\n"
        else :
            texto += f"[{i}] {opc} + {opcsValores[i]*5}%\n"
    mostrar_mensagem(texto,titulo="UPGRADES",estilo="blue",pausa=0.4)
    escolher = Partida.validar_opc(lista=list(opcs.keys()),
                                   mensagem="Escolha seu upgrade: ",saida=False)

    match list(opcs)[escolher]:

        case "dano no dado" :
            jog.D10MAX += opcs["dano no dado"]

        case "dano bonus" :
            jog.danobonus += opcs["dano bonus"]

        case "moeda bonus":
            jog.bonusMoedas += opcs["moeda bonus"]

        case "agilidade bonus" :
            jog.agilidadebonus += opcs["agilidade bonus"]
        case "sorte" :
            jog.aumentar_sorte(opcs["sorte"])

        case "chance critico" :
            jog.chancecritico += opcs["chance critico"]

        case "critico" :
            jog.criticobonus += opcs["critico"]

    som.upgradesom.play()
