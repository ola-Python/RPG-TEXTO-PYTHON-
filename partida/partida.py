import random
from time import sleep
from rich import print

from interface.funcoes import mostrar_mensagem
from jogador import Jogador
class Partida :
    def __init__(self,jogadores:Jogador):
        self.jogadores = jogadores
        self.mortos:list[Jogador] = []

    @classmethod
    def registrar_jogadores(cls,qj,hp):
        jogadores = []
        for i in range(qj):
            #nome = str (input (f"Nome do jogador{i+1}")).strip().title()
            nome = f"Jogador {i + 1}"
            jogadores.append(Jogador(nome, hp))
        return jogadores

    def verificar_mortos (self) :
        for jogador in self.jogadores[:] :
            if jogador.hp <=0 :
                print(f"{jogador.nome} morreu")
                self.mortos.append(jogador)
                self.jogadores.remove(jogador)

    def lista_mortos(self): #testando
        if self.mortos :
            print("Lista de mortos :")
            for morto in self.mortos :
                print(morto.nome)
    @classmethod
    def ganhar_moeda(cls,jog:Jogador,rodada):
        moedamax = int(4 + rodada / 4)
        fim = 3
        moeda = random.randint(1,moedamax)
        chance = random.randint(1,fim)
        if chance == 1 :
            mostrar_mensagem(f"{jog.nome} ganhou {moeda} moedas!",estilo="#FFF300",
                             pausa=1,titulo="RECOMPENSA")
            jog.moedas += moeda
            sleep(1.5)
    def fim_partida (self):
        if len(self.jogadores) <=1 :
            if self.jogadores[0].hp >= 1 :
                campeao:Jogador = self.jogadores[0]
                print(f"{campeao.nome} Venceu a partida!")
            else :
                print("Todo mundo morreu ")
            return True

        return False

    @classmethod
    def validar_opc(cls,lista=None,mensagem=">",mnsgvazio="lista vazia"):
        if not lista:
            print(mnsgvazio)
            return None
        fim = len(lista)
        opc = None
        while opc != -1:
            try :
                opc = int (input(mensagem))
                if opc == -1 :
                    return None
                if opc >=0 and opc < fim :
                    return  opc
            except ValueError :
                print("[red]Digite um valor válido[/]")





