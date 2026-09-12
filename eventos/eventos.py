from time import sleep

from interface.funcoes import mostrar_mensagem
from jogador import Jogador
from random import randint,choice,choices,random
from rich import print
from rich.panel import Panel


class EventoAleatorio :
    def __init__(self,jogadores:list[Jogador],turno):
        self.alvo = []
        self.jogadores = jogadores
        self.turno = turno


    def escolher_jogador(self):
        if random() < 0.80:  #escolhe apenas um jogador 80% de chance
            self.alvo = [choice(self.jogadores)]
        else : #20% de chance
            self.alvo = self.jogadores #todos os jogadores foram escolhidos
            mostrar_mensagem("TODOS OS JOGADORES FORAM ESCOLHIDOS!",
                             titulo="EVENTO ALEATÓRIO",pausa=1.5,largura=70)

    def escolher_evento(self):
        eventos = {
            self.moeda:40,
            self.hp:50

        }

        evento = choices(list(eventos.keys()),
                         weights=list(eventos.values()),
                         k=1)[0]

        evento()

    def executar(self):
        if random() < 0.40 :
            mostrar_mensagem(titulo="EVENTO ALEATÓRIO",mensagem="ESCOLHENDO EVENTO ALEATÓRIO. . .",
                             pausa=2,largura=70)
            self.escolher_jogador()
            self.escolher_evento()

    def moeda(self):
        for jogador in self.alvo :
            maxmoeda = int(self.turno*0.4)
            if maxmoeda <=0 :
                maxmoeda = 1
            moedas = randint(1,maxmoeda)
            texto = f"{jogador.nome} foi escolhido!"
            if jogador.roletar_sorte(45) :
                texto += f"\n{jogador.nome} [green]ganhou[/] [#FFF300]{moedas} moedas[/]"
                texto += f"\nmoedas : {jogador.moedas} -> "
                jogador.moedas += moedas
                texto += f"{jogador.moedas} "
            else :
                texto += f"\n{jogador.nome} [red]perdeu {moedas} moedas[/]"
                texto += f"\nmoedas : [#FFF300]{jogador.moedas}[/] -> "
                jogador.moedas -= moedas
                if jogador.moedas < 0 :
                    jogador.moedas = 0
                texto += f"[red]{jogador.moedas}[/] "
            mostrar_mensagem(texto,titulo="EVENTO DE MOEDAS")
            sleep(1.5)

    def hp(self):
        for jogador in self.alvo : #jogador = jogador atual da lista
            texto = f"{jogador.nome} foi escolhido!"
            if jogador.roletar_sorte(45) : #se ele tiver sorte
                acoes = [f"{jogador.nome} encontrou e bebeu uma poção de cura",
                         f"{jogador.nome} comeu um pastel com caldo de cana",
                         f"{jogador.nome} encontrou um mago que usou uma magia de cura"]

                acao = choice(acoes)
                hp = randint(1,self.turno)
                texto += f"\n{acao} [green]aumentando [bold]{hp}[/] de hp[/]"
                texto += f"\n[green]{jogador.hp}[/] -> [green]{jogador.hp+ hp}[/]"
                jogador.hp += hp
            else :
                acoes = [f"{jogador.nome} foi atingido por um raio",
                         f"{jogador.nome} escorregou e caiu de cabeça",
                         f"{jogador.nome} foi atingido por um tijolo",]
                acao = choice(acoes)
                maxhp = int(self.turno * 0.6)
                if maxhp <= 0 :
                    maxhp = 1
                hp = randint(1,maxhp)

                texto += f"\n{acao} [red]perdendo [bold]{hp}[/] de hp[/]"
                texto += f"\n[green]{jogador.hp}[/] -> [red]{jogador.hp - hp}[/]"
                jogador.hp -= hp
            mostrar_mensagem(texto,titulo="EVENTO ALEATÓRIO",pausa=2,largura=70)
            sleep(1.5)

