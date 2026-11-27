from time import sleep

import interface
import som
from equipamento.armadura import Armadura
from interface.funcoes import limpar_tela
from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida
from loja import Loja
from rich import print
from interface.menu import mostrar_acoes,Tabelajogadores
from interface.funcoes import mostrar_mensagem
from eventos import EventoAleatorio
import devtestes
#emojis que funcionam no terminal : ☠️⚔️✨⚙️⛏️⏲️⏰⏳⌛
# ✏️⛲⛺♨️⛈️❄️⚠️❇️✅❌✪↩️↓↑♾️☯️✝️
versao = "0.1.0"
#================================ criar exe : ================================
#python -m PyInstaller --clean --onefile --name TerminalPvP v0.1.0 --add-data "sound;sound" main.py
#=============================================================================


texto =f"[red]TERMINAL RPG[/]  [green]v{versao}[/]"
mostrar_mensagem(texto,titulo="TERMINAL RPG⚔️",pausa=2,largura=50)
while True :
    try :
        qj = int (input ("Quantos jogadores teremos na partida?"))
        if qj <= 1 :
            mostrar_mensagem("Só é possível iniciar uma partida com 2 ou mais jogadores  ",
                             titulo=":/",estilo="red")
        else :
            break
    except ValueError :
        print("[red]Digite um valor válido[/]")
while True :
    try:
        hp = int(input("quanto de hp os jogadores terão? (padrão = 100)"))
        if hp <= 0 :
            continue
    except ValueError :
        print("[red]Digite um valor válido![/]")
    else :
        break

limpar_tela()
jogadores : list[Jogador] = Partida.registrar_jogadores(qj=qj,hp=hp)
partida = Partida(jogadores)



jogatual = 0
turno = 1
rodada = 1
loja = Loja()
mostrar_mensagem("Boa Partida!",som=som.menusom(),titulo=":)",pausa=1.5)
som.comeco.play()
while True :
    limpar_tela()

    partida.verificar_mortos()
    if partida.fim_partida() :
        break
    if jogatual >= len(jogadores): #TESTE
        jogatual = 0
    jog = jogadores[jogatual] #Jogador atual
    evento = EventoAleatorio(turno=turno,jogadores=jogadores)
    Tabelajogadores(jogadores=jogadores,jogatual=jog)
    mostrar_acoes(jog,turno=turno)
    loja.turno = turno
    jog.ganharXp(0) #verifica se ele precisa evoluir

    #==================  IMPORTANTE ===========================
    #opc = Partida.validar_opc([0, 1, 2, 3, 4, 5], "Sua opção:")  #pra teste
    opc = Partida.validar_opc([1, 2, 3, 4], "Sua opção:") # pra jogar e distribuir o jogo sem as funções de dev
    #===========================================================

    if opc == 0 : #passa para o próximo jogador === ferramenta de teste ===
        jogatual = (jogatual + 1) % len(jogadores)
        turno += 1
    if opc == 1 :
        som.atacar.play()
        combate = Combate(jog=jogadores[jogatual],jogadores=jogadores,indice=jogatual)
        if combate.atacar() :
            partida.verificar_mortos()
            if partida.fim_partida():
                break

            #após o ataque, chance de ganhar moeda e executar evento
            Partida.ganhar_moeda(rodada=rodada, jog=jog)
            evento.executar()
            jogatual = (jogatual + 1) % len(jogadores) #passou para o proximo jogador

            if jogatual == 0 : #verifica se passou de rodada
                loja.chance_att_loja()
                rodada +=1
            turno += 1


    if opc == 2 : #abre a loja
        som.menusom()
        loja.entrar_loja(jog=jog)

    if opc == 3 : #abre o inventário
        jogadores[jogatual].inventariomenu()

    if opc == 4 : #testando eventos === ferramenta de teste ===
        turno = devtestes.menudev(jog,turno,evento)


mostrar_mensagem("Jogo criado por Erick\n"
                 "Canal do youtube : https://www.youtube.com/@OlaPython\n"
                 "Repositório no github : https://github.com/ola-Python/RPG-TEXTO-PYTHON-\n"
                 "Obrigado por Jogar! =D",
                 titulo="Créditos",som=som.menusom(),pausa=2,largura=75)

