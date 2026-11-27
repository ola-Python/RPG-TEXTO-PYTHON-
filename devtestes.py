from equipamento import Equipamento
from equipamento.armadura import Armadura
from jogador import Jogador
from partida import Partida
from eventos import EventoAleatorio
from interface import funcoes,menu
from rich import print


def menudev(jog:Jogador,turno,evento) :
    opc = True
    while opc :
        funcoes.limpar_tela()
        print(menu.statusJogador(jog,turno))
        print("""Escolha :
        [-1] Sair               [0] + 1000 moedas       [1] + 10 agilidade          [2] evento de hp
        [3] gerar/equipar arma  [4] gerar/equipar anel  [5]gerar/equipar armadura   [6] + 0.5 sorte 
        [7] + 10 turno          [8]+100xp               [9] critico máximo          [10] + 3 chance critico
        """)
        opc = Partida.validar_opc([0,1,2,3,4,5,6,7,8,9,10],saida=True)

        match opc :
            case -1 :
                return turno
            case 0 :
                jog.moedas += 1000
                opc = True
            case 1 :
                jog.agilidadebonus += 10
            case 2 :
                evento.escolher_jogador(),evento.hp()
            case 3 :
                arma = Equipamento.gerarArma(turno)
                jog.adicionar_item_inventario(arma)
                jog.equipar(arma)
            case 4 :
                anel = Equipamento.gerarAnel(turno)
                jog.adicionar_item_inventario(anel)
                jog.equipar(anel)
            case 5 :
                armadura = Armadura.gerarArmadura(turno)
                jog.adicionar_item_inventario(armadura)
                jog.equipar(armadura)
            case 6 :
                jog.aumentar_sorte(0.5)
            case 7 :
                turno += 10
            case 8 :
                jog.ganharXp(100)
            case 9 :
                jog.criticobonus = 3.0
            case 10 :
                jog.chancecritico = 3
    return turno
