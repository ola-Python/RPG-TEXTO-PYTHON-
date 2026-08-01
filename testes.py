from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida
from loja import Loja
from rich import inspect #apagar?
from rich import print
while True :
    try :
        qj = int (input ("Quantos jogadores teremos na partida?"))
        if qj <= 1 :
            print("Só é possível iniciar uma partida com 2 ou mais jogadores")
        else :
            break
    except ValueError :
        print("Digite um valor válido")
#hp = int (input ("Hp dos jogadores :"))
jogadores : list[Jogador] = Partida.registrar_jogadores(qj=qj,hp=10)
partida = Partida(jogadores)

jogatual = 0


turno = 5
loja = Loja()
while True :
    partida.verificar_mortos()
    if partida.fim_partida() :
        break
    if jogatual >= len(jogadores):
        jogatual = 0 #TESTE
    jog = jogadores[jogatual] #Jogador atual
    loja.turno = turno
    print(f"""
    TURNO : {turno}
    vez do jogador {jogadores[jogatual].nome}       hp: {jogadores[jogatual].hp}
    [1] Atacar
    [2] Loja
    [3] Ver inventário
    [4] + 30 moedas (teste)
    """)
    opc = Partida.validar_opc([1,2,3,4  ,5],"Sua opção:")

    if opc == 1 :
        combate = Combate(jog=jogadores[jogatual],jogadores=jogadores,indice=jogatual)
        combate.atacar()
        jogatual = (jogatual + 1) % len(jogadores)
        turno += 1


    if opc == 2 :
        loja.entrar_loja(jog=jog)

    if opc == 3 :
        jogadores[jogatual].mostrar_inventario()

    if opc == 4:
        jog.moedas += 30