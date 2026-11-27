from time import sleep

import som
from interface.funcoes import mostrar_mensagem
from jogador import Jogador
from random import randint,choice,choices,random
from rich import print
from rich.panel import Panel
from random import uniform


class EventoAleatorio :
    def __init__(self,jogadores:list[Jogador],turno):
        self.alvo = []
        self.jogadores = jogadores
        self.turno = turno


    def escolher_jogador(self):
        if random() < 0.80:  #escolhe apenas um jogador 80% de chance 0.80
            self.alvo = [choice(self.jogadores)]
        else : #20% de chance
            self.alvo = self.jogadores #todos os jogadores foram escolhidos
            mostrar_mensagem("TODOS OS JOGADORES FORAM ESCOLHIDOS!",
                             titulo="EVENTO ALEATÓRIO",pausa=1.5,largura=70)

    def escolher_evento(self): #método usado apenas na classe
        eventos = { #métodos da classe + chance de aparecer
            self.moeda:35,
            self.hp:50,
            self.cassino:15

        }

        evento = choices(list(eventos.keys()),
                         weights=list(eventos.values()),
                         k=1)[0]

        evento()

    def executar(self): #método chamado no código principal
        #ele pode receber o turno no futuro ao inves de ser um self

        if random() < 0.30 : #30% de chance de executar um evento
            som.evento.play()
            mostrar_mensagem(titulo="EVENTO ALEATÓRIO",
                             mensagem="ESCOLHENDO EVENTO ALEATÓRIO. . .",
                             pausa=2.2,largura=70)

            #escolhe um ou todos os jogadores e executa o evento
            self.escolher_jogador()
            self.escolher_evento()

    def moeda(self):
        for jogador in self.alvo :
            sommoeda = None #somente para o som
            maxmoeda = int(self.turno*0.4)
            if maxmoeda <=0 :
                maxmoeda = 1
            moedas = randint(1,maxmoeda)
            texto = f"{jogador.nome} foi escolhido!"
            if jogador.roletar_sorte(45) : #se tiver sorte
                sommoeda = som.moedas
                texto += f"\n{jogador.nome} [#0EEE7E bold]ganhou[/] [#FFF300]{moedas} moedas[/]"
                texto += f"\n[#FFF300]moedas : {jogador.moedas} -> "
                jogador.moedas += moedas
                texto += f"{jogador.moedas}[/] "
            else : #azar perder moeda
                maxmoeda = int(self.turno * 0.2)
                sommoeda = som.roubado
                if maxmoeda <= 0:
                    maxmoeda = 1
                moedas = randint(1, maxmoeda)
                texto += f"\n{jogador.nome} [red]perdeu {moedas} moedas[/]"
                texto += f"\nmoedas : [#FFF300]{jogador.moedas}[/] -> "
                jogador.moedas -= moedas
                if jogador.moedas < 0 :
                    jogador.moedas = 0
                texto += f"[red]{jogador.moedas}[/] "
            mostrar_mensagem(texto,titulo="EVENTO ALEATÓRIO",som=sommoeda,linha_som=2,
                             largura=70)
            sleep(1.5)

    def cassino(self):
        for jogador in self.alvo :
            texto =f"{jogador.nome} foi escolhido!"
            multi = round(uniform(1.0,2.0),1)
            chance = int(35 * jogador.sorte)
            texto += f"\n[#FFF300]Multiplicador de moedas : [bold #0EEE7E]{multi}[/][/]"
            texto+=f"\n[#0EEE7E]chance de [bold]ganhar {chance}%[/][/]"
            texto+= f"\n[#FFF300]suas moedas : [bold]{jogador.moedas}[/][/]"
            som.cassino.play()
            while True :

                mostrar_mensagem(texto, titulo="[#0EEE7E]$$$[/] [#FFF300 bold]CASSINO [#0EEE7E]$$$[/][/]", largura=60, pausa=0.8)
                try :
                    aposta = int (input ("quanto deseja apostar?"))
                except ValueError :
                    mostrar_mensagem("Digite um valor válido",titulo=":/",
                                     estilo="red",pausa=1)
                    continue
                if aposta > jogador.moedas :
                    mostrar_mensagem("Você não tem essa quantidade de moedas!",
                                     titulo=":/",estilo="red",pausa=1.3)
                    continue
                elif aposta <0 :
                    mostrar_mensagem("Você não pode apostar menos que 0 moedas!"
                                     ,titulo=":/",estilo="red",pausa=1.3)
                    continue
                break

            if aposta == 0 :
                mostrar_mensagem(f"{jogador.nome} Escolheu não apostar",
                                 titulo="[#0EEE7E]$$$[/] [#FFF300 bold]CASSINO [#0EEE7E]$$$[/][/]",pausa=1.3,largura=60)
                continue
            texto = ""
            som.roletando.play()
            mostrar_mensagem("[#FFF300 bold]ROLETANDO. . .[/]",titulo="[#0EEE7E]$$$[/] [#FFF300 bold]CASSINO [#0EEE7E]$$$[/][/]",pausa=2.5,largura=60)
            roubo = None
            if jogador.roletar_sorte(35) : #=====  GANHOU  =====
                recompensa = int(aposta * multi)
                texto = f"✨ Você [#FFF300 bold]ganhou {recompensa} moedas!✨"
                texto += f"\nMoedas : {jogador.moedas} -> {jogador.moedas + recompensa}[/]"
                jogador.moedas += recompensa

            else : # ===== PERDEU =====
                som.roletando.stop()
                variacao = randint(0,2)
                if variacao == 0 :
                    roubo = som.roubado
                elif variacao == 1 :
                    roubo = som.fail
                elif variacao == 2 :
                    som.fail2.play()
                texto += f"☠️Você [red bold]perdeu {aposta} moedas!☠️"
                texto += f"\nMoedas : {jogador.moedas} -> {jogador.moedas - aposta}[/]"
                jogador.moedas -= aposta
            mostrar_mensagem(texto,titulo="[#0EEE7E]$$$[/] [#FFF300 bold]CASSINO [#0EEE7E]$$$[/][/]",pausa=1.5,largura=60,som=roubo,linha_som=1)



    def hp(self):
        for jogador in self.alvo : #jogador = jogador atual da lista
            dano = False #pra verificar se o jogador ganhou ou perdeu hp
            texto = ""
            if jogador.roletar_sorte(45) : #se ele tiver sorte
                acoes = [("pocaomine",f"{jogador.nome} encontrou e bebeu uma poção de cura"),
                         ("comer",f"{jogador.nome} comeu um pastel com caldo de cana"),
                         ("minexp",f"{jogador.nome} encontrou um mago que usou uma magia de cura")]

                tipo,acao = choice(acoes)
                hp = randint(1,self.turno)
                if tipo == "pocaomine" :
                    som.pocaomine.play()
                elif tipo == "comer" :
                    som.comer.play()
                elif tipo == "minexp" :
                    som.xpmine.play()
                texto += f"{acao} [green]aumentando [bold]{hp}[/] de hp[/]"
                texto += f"\n[green]{jogador.hp}[/] -> [green]{jogador.hp+ hp}[/]"
                jogador.hp += hp
                xp = hp
            else :
                acoes = [("raio",f"{jogador.nome} foi atingido por um raio"),
                         ("bonk",f"{jogador.nome} escorregou e caiu de cabeça"),
                         ("bonk",f"{jogador.nome} foi atingido por um tijolo"),
                         ("cjfogo", f"{jogador.nome} começou a pegar fogo♨️")
                         ]
                tipo,acao = choice(acoes)
                dano = True
                maxhp = int(self.turno * 0.6)
                if maxhp <= 0 :
                    maxhp = 1
                hp = randint(1,maxhp)
                texto += f"{acao}   dano = {hp}"
                if tipo == "raio" :
                    som.raio.play()
                elif tipo == "bonk" :
                    som.bonk.play()
                elif tipo == "cjfogo" :
                    som.fogocj.play()
            mostrar_mensagem(texto,titulo="EVENTO ALEATÓRIO",pausa=2.4,largura=70)
            if dano :
                jogador.receber_dano(hp)
                xp = int( hp * 1.5)
            sleep(0.5)
            jogador.ganharXp(xp)

