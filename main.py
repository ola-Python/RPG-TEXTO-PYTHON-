from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida
from rich import inspect #apagar?
from rich import print

qj = int (input ("Quantos jogadores teremos na partida?"))
#hp = int (input ("Hp dos jogadores :"))
jogadores : list[Jogador] = Partida.registrar_jogadores(qj=qj,hp=10)
partida = Partida(jogadores)

jogatual = 0
espada = Equipamento("Espada comum",5,8,0,"arma")
espada2 = Equipamento("Faca ",3,8,0,"arma")
anel = Equipamento("Anel mágico",1,5,4,"anel")
anel2 = Equipamento("Anel comum",1,5,45,"anel")

jogadores[0].adicionar_item_inventario(anel2)
jogadores[0].adicionar_item_inventario(espada)
jogadores[0].equipar(espada)
jogadores[0].adicionar_item_inventario(espada2)
jogadores[0].equipar(espada2)
jogadores[0].adicionar_item_inventario(anel)
jogadores[0].equipar(anel)
while True :
    partida.verificar_mortos()
    if partida.fim_partida() :
        break
    if jogatual >= len(jogadores):
        jogatual = 0
    print(f"""
    vez do jogador {jogadores[jogatual].nome}       hp: {jogadores[jogatual].hp}
    [1] Atacar
    [2] Loja
    [3] Ver inventário
    """)
    opc = int (input ("Sua opção : "))

    if opc == 1 :
        combate = Combate(jog=jogadores[jogatual],jogadores=jogadores,indice=jogatual)
        combate.atacar()

        jogatual = (jogatual + 1) % len(jogadores)


    if opc == 2 :
        #Loja
        pass

    if opc == 3 :
        jogadores[jogatual].mostrar_inventario()