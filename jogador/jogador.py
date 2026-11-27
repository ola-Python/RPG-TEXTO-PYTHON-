from os import remove
from random import randint
from time import sleep

from rich.panel import Panel
from rich.table import Table

import som
from equipamento import Equipamento
from equipamento.armadura import Armadura
from interface.funcoes import mostrar_mensagem
from rich import print
class Jogador :
    def __init__(self,nome,hp):
        # ========= ATRIBUTOS ========
        self.nome = nome
        self.hp = hp
        self.danobonus = 0 #original = 0
        self.D10MAX = 7 #original = 7
        self.criticobonus = 0.0 #original = 0.0
        self.chancecritico = 0 #original = 0
        self.agilidadebonus = 0 #original = 0
        self.moedas = 0 #original = 0
        self.bonusMoedas = 0 #original = 0
        self.sorte = 1.0 #original = 1.0
        self.xp = 0 #original = 0
        self.XPMAX = 100 #original = 100
        self.level = 1 #original = 1
        self.inventario = []

        # ========= SLOTS ========
        self.arma:Equipamento = None
        self.anel:Equipamento = None
        self.armadura:Armadura = None


    def ganharXp(self,valor):
        from jogador.upgrade import upgrade

        if valor > 0 :
            self.xp += valor
            if valor > 5 :
                som.xpmine.play()
                mostrar_mensagem(f"[bold]{self.nome}[/] Ganhou + {valor}XP", estilo="blue", titulo="XP",pausa=0.9)
        while self.xp >= self.XPMAX :
            self.xp -= self.XPMAX
            self.level += 1
            som.levelup.play()
            mostrar_mensagem(f"{self.nome} Subiu para o Level {self.level}!",
                             estilo="blue", titulo="LEVEL UP", pausa=1.5,largura=40)

            upgrade(self)
    @property
    def agilidade(self):
        """Calcula todo o bonus de agilidade do jogador"""
        agi = self.agilidadebonus
        if self.anel :
            agi += self.anel.agilidade
        if  self.arma:
            agi += self.arma.agilidade
        return agi

    @property
    def d20max(self):
        """A cada 10 de bonus de agilidade aumenta 1 no valor máximo do d20"""
        return min(20+ self.agilidade // 7, 30) #a cada 7 de bonus de agilidade aumenta 1 no dado d20
    #começa com 20, o máximo é 30. aumenta as chances de crítico

    @property
    def d10max(self):
        dmax = self.D10MAX #começa com 7 sendo o maior valor do dado no inicio
        if self.arma :
            dmax += self.arma.dano
        return dmax


    @property
    def dano(self):
        """Pega os bonus de ataque, sem contar da arma, pois o bonus da arma
        vai influenciar o dado, ele não vai somar, apenas o dano do anel e o
        bonus que vai somar"""
        dano = self.danobonus
        if self.anel :
            dano += self.anel.dano
        return dano

    @property
    def critico(self):
        critico = min(1.5+self.criticobonus,3.0) #MAX = 3.0
        return critico

    def receber_dano(self,dano,combate=False):
        #o parametro combate é somente para o som, o programa vai verificar se essa função foi
        #chamada em um combate ou emm qualquer outra coisa que envolva dano
        if self.armadura :
            dano = self.armadura.absorverDano(dano,self)

            if self.armadura.esta_quebrada() :
                self.inventario.remove(self.armadura)
                self.armadura = None
        texto = f"{self.nome} perdeu [bold]{dano} de HP![/]"
        texto += f"\n{self.nome} HP: {self.hp} -> "
        self.hp = max(0, self.hp - dano)
        texto += f"{self.hp}"
        if combate :
            #Se for no combate pvp o som que vai tocar vai depender do dano que ele recebeu
            mostrar_mensagem(mensagem=texto,
                             titulo="DANO", estilo="red",
                             largura=35, pausa=0.8,som=som.dano_som(dano))
        else :
            #se o dano não for do combate, o som que vai tocar vai depender da situação
            mostrar_mensagem(mensagem=texto,
                             titulo="DANO", estilo="red",
                             largura=35, pausa=0.8)
        sleep(2)
        return dano



    # ============ CALCULANDO AGILIDADE DADO D20===========
    def d20 (self) :
        return randint(1,self.d20max) #original (1,d20max [começa com 20])

    def agilidadetot(self,d20):
        texto = ""
        agitot = d20
        texto = "Rolando dado de agilidade🎲..."
        texto += f"\n[bold] {d20}[/]"
        if self.agilidadebonus > 0 :
            texto += f"\n+[bold]{self.agilidadebonus}[/] Agilidade bonus"
            agitot += self.agilidadebonus
        if self.anel and self.anel.agilidade > 0 :
            texto += f"\n+[bold]{self.anel.agilidade}[/] Agilidade do [bold]{self.anel.nome}[/]"
            agitot += self.anel.agilidade
        if d20 != agitot :
            texto += f"\n[bold]TOTAL = {agitot}[/]"
        mostrar_mensagem(mensagem=texto,titulo="DADO DE AGILIDADE🎲",
                         largura=35,estilo="blue",pausa=0.7,som=som.dado,linha_som=2)
        sleep(0.8)
        return agitot

    # ============calculando dano dado D10===========
    def d10 (self) :
        return randint(1,self.d10max) #original (1,d10max)


    def danotot (self,d10,d20) :
        texto = ""
        texto += "Rolando dado de ataque🎲..."
        texto += f"\n [bold]{d10}[/]"
        danotot = d10
        if self.danobonus >0 :
            texto += f"\n+{self.danobonus} de bônus de ataque"
            danotot += self.danobonus
        if self.anel and self.anel.dano > 0 :
            danotot += self.anel.dano
            texto += f"\n+{self.anel.dano} de ataque do {self.anel.nome}"
        if d20 >= 20 :
            mostrar_mensagem(mensagem=f"[bold red on black]ESPECIAL ATIVADO!!!({self.critico}X)[/]",
                             titulo="DADO DE ATAQUE🎲", estilo="red",
                             pausa=1.3, largura=35, som=som.especial)
            danotot = int(danotot * self.critico)
        if d10 != danotot :
            texto += f"\n[bold]DANO TOTAL = {danotot}[/]"

        mostrar_mensagem(mensagem=texto,
                         titulo="DADO DE ATAQUE🎲",estilo="red",
                         pausa=0.8, largura=35,som=som.dado,linha_som=2)
        sleep(0.8)
        return danotot


    def roletar_sorte(self,probabilidade=45):
        chance = int(probabilidade * self.sorte)
        return randint(1,100) <= chance #retorna true ou false

    def aumentar_sorte(self,valor=0.1) :
        self.sorte = round(min(self.sorte + valor,1.6),1)


    #============ INVENTÁRIO===========
    def adicionar_item_inventario(self,item) :
        mostrar_mensagem(mensagem=f"[bold]{item}[/] foi adicionado no inventário ▤ ",
                         titulo="▤ INVENTÁRIO",pausa=1.5,largura=35)
        self.inventario.append(item)

    def inventariomenu(self):
        while True:
            self.mostrar_inventario()
            continuar = self.escolherequip()

            if not continuar:
                break

    def mostrar_inventario(self):
        som.inventario.play()
        if not self.inventario:
            mostrar_mensagem(mensagem="Inventário vazio", titulo="▤ Inventário",
                             estilo="red", pausa=1.5)
            return

        tabela = Table(title="▤ Inventário ▤ ")
        tabela.add_column("#")  # index
        tabela.add_column("Nome")
        tabela.add_column("Dano", style="red")
        tabela.add_column("Agilidade", style="blue")
        tabela.add_column("defesa", style="steel_blue")
        tabela.add_column("valor")

        for i, item in enumerate(self.inventario):
            tabela.add_row(
                str(i),
                str(item),
                str(item.dano if item.dano > 0 else " _ "),
                str(item.agilidade if item.agilidade > 0 else " _ "),
                str(item.defesa if item.defesa > 0 else " _ "),
                str(item.valor)
            )
        tabela.add_row("[red]-1[/]", "[red]↩️ Voltar[/]", "", "", "")
        print(tabela)
        arma = self.arma if self.arma else "Vazio"
        anel = self.anel if self.anel else "Vazio"
        armadura = self.armadura if self.armadura else "Vazio"
        texto = f"Arma : {arma}"
        texto += f"\nAnel : {anel}"
        texto += f"\nArmadura: {armadura}"
        painel = Panel(title="EQUIPADOS⚔️",
                       renderable=texto, width=60)
        print(painel)

    def escolherequip(self):
        if not self.inventario:
            return
        from partida import Partida
        opc = Partida.validar_opc(lista=self.inventario)
        if opc is None:
            return False
        if isinstance(self.inventario[opc], Equipamento):
            self.equipar(self.inventario[opc])
            return True
        return True

    def equipar(self,item):
        texto = ""
        if item not in self.inventario :
            mostrar_mensagem(f"{item} Não está no inventário",titulo=":/",estilo="red")
            sleep(1)
            return
        if item.tipo == 'arma' :
            if self.arma :
                texto = f"↓ Desequipando {self.arma}\n"
            self.arma = item
        elif item.tipo == "anel" :
            if self.anel :
                texto = f"↓ Desequipando {self.anel}\n"
                sleep(0.5)
            self.anel = item

        elif item.tipo == "armadura":
            if self.armadura:
                texto = f"↓ Desequipando {self.armadura.nome}\n"
            self.armadura = item
        texto += f"[bold]{self.nome}[/]↑ Equipou [bold]{item}[/]"
        som.equipar.play()
        mostrar_mensagem(texto,titulo="▤ Inventário",pausa=1.3,largura=50)
