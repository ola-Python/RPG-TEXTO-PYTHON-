from rich.panel import Panel

from equipamento import Equipamento
from interface.funcoes import mostrar_mensagem, limpar_tela
from jogador import Jogador
from random import randint
from time import sleep
from rich import print
from rich.table import Table
class Loja:
    def __init__(self):
        self.estoque: list[Equipamento] = []
        self.slot = 3
        self.preco_slot = 3
        self.turno = 1

    def entrar_loja(self,jog:Jogador):
        while True :
            limpar_tela()
            self.mostrar_loja(jog)
            if not self.compra(jog) :
                break


    def tem_moeda (self,jog:Jogador,valor):
        if jog.moedas < valor :
            print("[red bold]Moedas insuficiente![/]")
            sleep(0.6)
            return False

        jog.moedas -= valor
        return True

    def novo_equip(self):
        if randint(0,1) == 0 :
            equip = Equipamento.gerarArma(self.turno)
        else :
            equip = Equipamento.gerarAnel(self.turno)
        self.estoque.append(equip)

    def att_loja(self):
        mostrar_mensagem("❇️LOJA ATUALIZADA!❇️",
                         estilo="#FFF300",titulo="LOJA")
        self.estoque = []
        for c in range (0,self.slot) :
            self.novo_equip()

    def chance_att_loja(self) :
        fim = 3
        if self.turno == 20 :
            print("50% de chance da loja atualizar!")
            sleep(1)
        if self.turno >= 20 :
            fim = 2 #mais chance de att loja
        chance = randint(1,fim)
        if chance == 1 :
            self.att_loja()
        return

    def mostrar_loja(self,jog:Jogador):
        tabela = Table(title="[#FFF300] ▣ LOJA ▣ [/] ")
        tabela.add_column("#") #indice
        tabela.add_column("Nome")
        tabela.add_column("Dano",style="red")
        tabela.add_column("Agilidade",style="blue")
        tabela.add_column("Preço",style="#FFF300")

        if self.estoque :
            for i, e in enumerate (self.estoque) : # e-> equipamento
                tabela.add_row(str(i),
                               str(e.nome),
                               str(e.dano),
                               str(e.agilidade),
                               str(e.valor),)
            print(tabela)
        else :
            mostrar_mensagem(mensagem="[red]Nenhum equipamento disponível na loja![/]",
                             titulo="[#FFF300] ▣ LOJA ▣ [/]",pausa=0)
        print("-="*30)
        texto = f"[#2ECC71][-3] ✚ Comprar +1 slot[/] [#FFF300]({self.preco_slot} moedas)[/]"
        texto += f"\n[#3498DB][-2] ✨ Atualizar loja[/] [#FFF300](5 moedas)[/]"
        texto += f"\n[red][-1] ↩️ Voltar[/]"
        texto +=f"\n[#FFF300]Suas [bold]moedas ✪ : {jog.moedas}[/][/]"
        painel = Panel(texto,title="suas ações :",width=60)
        print(painel)

    def compra(self, jog: Jogador):
        while True :
            try :
                indice = int(input("sua opção : "))
                if indice in (-3,-2,-1) : #comprar slot,att loja ou sair, é válido
                    break #valor válido, pode continuar

                if 0 <= indice < len(self.estoque) :
                    break #valor válido, pode continuar

            except ValueError :
                print("[red]Digite um valor válido[/]")

        if indice == -1 :
            return #sair da loja

        elif indice == -2 :
            if self.tem_moeda(valor=5,jog=jog) : #verifica se o jogador tem dinheiro pra att loja
                self.att_loja()

        elif indice == -3 : #comprar slot na loja
            if self.tem_moeda(jog=jog,valor=self.preco_slot) :
                self.slot += 1
                self.preco_slot += 2
                self.novo_equip()
        else :
            if self.tem_moeda(jog=jog,valor=self.estoque[indice].valor) :
                jog.adicionar_item_inventario(self.estoque[indice])
                self.estoque.remove(self.estoque[indice])
        return True


