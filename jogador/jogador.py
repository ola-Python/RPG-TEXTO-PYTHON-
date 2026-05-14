from random import randint
from time import sleep
from equipamento import Equipamento
class Jogador :
    def __init__(self,nome,hp):
        self.nome = nome
        self.hp = hp
        self.danobase = 10
        self.agilidadebase = 0
        self.inventario = []

        #slots
        self.arma:Equipamento = None
        self.anel = None


    def d20 (self) :
        print("Rolando dado de agilidade🎲 . . .")
        sleep(0.5)
        d10 = randint(10,20)
        print(d10)
        return d10
    def d10 (self) :
        print("Rolando dado de ataque🎲 . . .")
        sleep(0.5)
        d10 = randint(1,10)
        print(d10)
        return d10

    def danotot (self,d10,d20) :
        danotot = d10
        if self.danobase >0 :
            print(f"+ {self.danobase} de bônus")
            danotot += self.danobase
        if self.arma and self.arma.dano > 0 :
            danotot += self.arma.dano
            print(f"+ {self.arma.dano} ⚔️")
        if d20 >= 20 :
            print("ESPECIAL ATIVADO!!!")
            sleep(0.3)
            danotot *= 2
        return danotot
    def adicionar_item_inventario(self,item) :
        print (f"{item.nome} foi adicionado no inventário")
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario :
            print("Inventário vazio")
            return
        opc = 0
        fim = len(self.inventario)
        while opc != fim :
            for i, item in  enumerate(self.inventario) :
                print(f"-[{i}] {item.nome}  dano:{item.dano}  agilidade:{item.agilidade}  tipo:{item.tipo}")
            print(f"-[{fim}] Saída")
            if self.arma :
                print(f"Arma equipada : {self.arma.nome}")
            if self.anel :
                print(f"Anel equipado : {self.anel.nome}")
            opc = int (input ("> "))
            if opc == fim :
                return
            if self.inventario[opc].tipo == "arma" or self.inventario[opc].tipo == "anel" :
                self.equipar(self.inventario[opc])


    def equipar(self,item):
        if item not in self.inventario :
            print(f"{item.nome} Não está no inventário")
            return
        if item.tipo == 'arma' :
            if self.arma :
                print(f"Desequipando {self.arma.nome}")
            self.arma = item
        elif item.tipo == "anel" :
            if self.anel :
                print(f"Desequipando {self.anel.nome}")
            self.anel = item
        print(f"{self.nome} Equipou {item.nome}")