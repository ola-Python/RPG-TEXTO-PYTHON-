from random import randint
from time import sleep
from equipamento import Equipamento
class Jogador :
    def __init__(self,nome,hp):
        self.nome = nome
        self.hp = hp
        self.danobase = 0
        self.agilidadebase = 0
        self.moedas = 0
        self.inventario = []

        #slots
        self.arma:Equipamento = None
        self.anel = None

# preciso criar um método pra calcular a agilidade total
    def d20 (self) :
        print("Rolando dado de agilidade🎲 . . .")
        sleep(0.6)
        d20 = randint(1,20) #original (1,20)
        print(d20)
        sleep(0.3)
        return d20
    def d10 (self) :
        print("Rolando dado de ataque🎲 . . .")
        sleep(0.6)
        d10 = randint(1,10) #original (1,10)
        print(d10)
        sleep(0.3)
        return d10

    def danotot (self,d10,d20) :
        danotot = d10
        if self.danobase >0 :
            print(f"+ {self.danobase} de bônus")
            sleep(0.5)
            danotot += self.danobase
        if self.arma and self.arma.dano > 0 :
            danotot += self.arma.dano
            print(f"+ {self.arma.dano} ⚔️")
        if d20 >= 20 :
            print("ESPECIAL ATIVADO!!!")
            sleep(0.8)
            danotot *= 2
        return danotot
    def adicionar_item_inventario(self,item) :
        print (f"{item.nome} foi adicionado no inventário")
        sleep(1)
        self.inventario.append(item)

    def mostrar_inventario(self):
        if not self.inventario :
            print("Inventário vazio")
            sleep(1)
            return
        opc = 0
        fim = len(self.inventario)
        while opc != fim :
            from partida import Partida
            for i, item in  enumerate(self.inventario) :
                print(f"{f"[ {i} ]":<5} {item.nome}  dano:{item.dano}  agilidade:{item.agilidade}  tipo:{item.tipo}")
            print(f"{"[-1 ]":<5} Saída")
            if self.arma :
                print(f"Arma equipada : {self.arma.nome}")
            if self.anel :
                print(f"Anel equipado : {self.anel.nome}")
            opc = Partida.validar_opc(lista=self.inventario)
            if opc == None :
                return

            if self.inventario[opc].tipo == "arma" or self.inventario[opc].tipo == "anel" :
                self.equipar(self.inventario[opc])


    def equipar(self,item):
        if item not in self.inventario :
            print(f"{item.nome} Não está no inventário")
            sleep(1)
            return
        if item.tipo == 'arma' :
            if self.arma :
                print(f"Desequipando {self.arma.nome}")
                sleep(0.5)
            self.arma = item
        elif item.tipo == "anel" :
            if self.anel :
                print(f"Desequipando {self.anel.nome}")
                sleep(0.5)
            self.anel = item
        print(f"{self.nome} Equipou {item.nome}")
        sleep(1)