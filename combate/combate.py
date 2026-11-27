from time import sleep
from rich.table import Table
from rich import print

import som
from interface.funcoes import mostrar_mensagem
from jogador import Jogador
class Combate :
    def __init__(self,jog,jogadores,indice):
        self.jog:Jogador = jog
        self.jogadores = jogadores
        self.indice = indice  #-> indice do jogador atual que vai atacar
        self.qj = len(self.jogadores)
        self.alvo:Jogador = None  #-> jogador que será atacado

    def escolher_alvo(self):
        from partida import Partida
        if self.qj > 2 :

            while  True :
                jogtabela = Table(title="JOGADORES⚔️")
                jogtabela.add_column("#") #indice
                jogtabela.add_column("Nome")
                jogtabela.add_column("HP",style= "#0BC900")
                for i in range(self.qj):
                    if i != self.indice:
                        jogtabela.add_row(str(i),
                                          str(self.jogadores[i].nome),
                                          str(self.jogadores[i].hp))
                jogtabela.add_row("[red]-1[/]","[red]↩️ Voltar[/]","")
                print(jogtabela)
                try:
                    ialvo =  int (input ("Escolha quem você vai atacar⚔️ : "))
                    if ialvo == -1 :
                        return False
                    if ialvo == self.indice :
                        mostrar_mensagem(mensagem="Você não pode se atacar!",titulo=":/",estilo="red")
                        continue
                    if ialvo > self.qj-1 or ialvo < 0 :
                        continue
                    else :
                        self.alvo = self.jogadores[ialvo]
                        return True
                except ValueError :
                    mostrar_mensagem(mensagem="Digite um valor válido",titulo=":/",estilo="red")
        else  :
            for i in range (self.qj) :
                if i != self.indice :
                    ialvo = i
        self.alvo = self.jogadores[ialvo]
        return True

    def atacar (self) :
        texto = ""
        if not self.escolher_alvo() :
            return
        d20 = self.jog.d20()
        agitot = self.jog.agilidadetot(d20)
        if agitot > 10 :
            d10 = self.jog.d10()
            danotot = self.jog.danotot(d10,d20)
            self.alvo.receber_dano(danotot,combate=True)

        else :
            som.errou_ataque()
            mostrar_mensagem(mensagem="[bold]ERROU O DANO[/]",titulo=":(",estilo="red")


        # Ganhar xp após o ataque
        self.jog.ganharXp(d20)

        return True



