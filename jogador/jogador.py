from random import randint
from time import sleep

from rich.panel import Panel
from rich.table import Table

from equipamento import Equipamento
from interface.funcoes import mostrar_mensagem
from rich import print
class Jogador :
    def __init__(self,nome,hp):
        # ========= ATRIBUTOS ========
        self.nome = nome
        self.hp = hp
        self.danobase = 0
        self.agilidadebase = 0
        self.moedas = 0
        self.sorte = 1.0
        self.inventario = []

        # ========= SLOTS ========
        self.arma:Equipamento = None
        self.anel:Equipamento = None


    # ============ CALCULANDO AGILIDADE DADO D20===========
    def d20 (self) :
        return randint(1,20) #original (1,20)

    def agilidadetot(self,d20):
        texto = ""
        agitot = d20
        texto = "Rolando dado de agilidade🎲..."
        texto += f"\n[bold] {d20}[/]"
        if self.agilidadebase > 0 :
            texto += f"\n+[bold]{self.agilidadebase}[/] Agilidade bonus"
            agitot += self.agilidadebase
        if self.anel and self.anel.agilidade > 0 :
            texto += f"\n+[bold]{self.anel.agilidade}[/] Agilidade do [bold]{self.anel.nome}[/]"
            agitot += self.anel.agilidade
        if d20 != agitot :
            texto += f"\n[bold]TOTAL = {agitot}[/]"
        mostrar_mensagem(mensagem=texto,titulo="DADO DE AGILIDADE🎲",
                         largura=35,estilo="blue",pausa=0.7)
        sleep(1)
        return agitot

    # ============calculando dano dado D10===========
    def d10 (self) :
        return randint(1,10) #original (1,10)

    def danotot (self,d10,d20) :
        texto = ""
        texto += "Rolando dado de ataque🎲..."
        texto += f"\n [bold]{d10}[/]"
        danotot = d10
        if self.danobase >0 :
            texto += f"\n+{self.danobase} de bônus de ataque"
            danotot += self.danobase
        if self.arma and self.arma.dano > 0 :
            danotot += self.arma.dano
            texto += f"\n+{self.arma.dano} {self.arma.nome}⚔️"
        if self.anel and self.anel.dano > 0 :
            danotot += self.anel.dano
            texto += f"\n+{self.anel.dano} de ataque do {self.anel.nome}"
        if d20 >= 20 :
            texto += "\n[bold red on black]ESPECIAL ATIVADO!!![/]"
            danotot *= 2
        if d10 != danotot :
            texto += f"\n[bold]DANO TOTAL = {danotot}[/]"
        mostrar_mensagem(mensagem=texto,
                         titulo="DADO DE ATAQUE🎲",estilo="red",
                         pausa=0.7, largura=35)
        sleep(0.9)
        return danotot


    def roletar_sorte(self,probabilidade=45):
        chance = int(probabilidade * self.sorte)
        return randint(1,100) <= chance #retorna true ou false

    def aumentar_sorte(self,valor=0.1) :
        self.sorte = min(self.sorte + valor,2.0)


    #============ INVENTÁRIO===========
    def adicionar_item_inventario(self,item) :
        mostrar_mensagem(mensagem=f"[bold]{item.nome}[/] foi adicionado no inventário ▤ ",
                         titulo="▤ INVENTÁRIO",pausa=1.5,largura=35)
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario :
            mostrar_mensagem(mensagem="Inventário vazio",titulo="▤ Inventário",
                             estilo="red",pausa=1.5)
            return
        opc = 0
        fim = len(self.inventario)
        while opc != fim :
            tabela = Table(title="▤ Inventário ▤ ")
            tabela.add_column("#")  # index
            tabela.add_column("Nome")
            tabela.add_column("Dano",style="red")
            tabela.add_column("Agilidade",style="blue")
            tabela.add_column("Categoria")
            from partida import Partida
            for i, item in  enumerate(self.inventario) :
                tabela.add_row(
                    str(i),
                    str(item.nome),
                    str(item.dano),
                    str(item.agilidade),
                    str(item.tipo)
                )
            tabela.add_row("[red]-1[/]", "[red]↩️ Voltar[/]", "", "", "")
            print(tabela)
            arma = self.arma.nome if self.arma else "Vazio"
            anel = self.anel.nome if self.anel else "Vazio"
            texto = f"Arma : {arma}"
            texto += f"\nAnel : {anel}"
            painel = Panel(title="EQUIPADOS⚔️",
                           renderable=texto,width=60)
            print(painel)

            opc = Partida.validar_opc(lista=self.inventario)
            if opc == None :
                return

            if self.inventario[opc].tipo == "arma" or self.inventario[opc].tipo == "anel" :
                self.equipar(self.inventario[opc])


    def equipar(self,item):
        texto = ""
        if item not in self.inventario :
            mostrar_mensagem(f"{item.nome} Não está no inventário",titulo=":/",estilo="red")
            sleep(1)
            return
        if item.tipo == 'arma' :
            if self.arma :
                texto = f"↓ Desequipando {self.arma.nome}\n"
            self.arma = item
        elif item.tipo == "anel" :
            if self.anel :
                texto = f"↓ Desequipando {self.anel.nome}\n"
                sleep(0.5)
            self.anel = item
        texto += f"[bold]{self.nome}[/]↑ Equipou [bold]{item.nome}[/]"
        mostrar_mensagem(texto,titulo="▤ Inventário",pausa=1.3)