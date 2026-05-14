from jogador import Jogador
class Combate :
    def __init__(self,jog,jogadores,indice):
        self.jog:Jogador = jog
        self.jogadores = jogadores
        self.indice = indice  #-> indice do jogador atual que vai atacar
        self.qj = len(self.jogadores)
        self.alvo:Jogador = None  #-> jogador que será atacado

    def escolher_alvo(self):
        if self.qj > 2 :
            for i in range (self.qj) :
                if i != self.indice :
                    print(f"- [{i}] {self.jogadores[i].nome}")
            ialvo = int (input ("Escolha quem você vai atacar"))
        else  :
            for i in range (self.qj) :
                if i != self.indice :
                    ialvo = i
        self.alvo = self.jogadores[ialvo]

    def atacar (self) :
        self.escolher_alvo()
        d20 = self.jog.d20()
        if d20 > 10 :
            d10 = self.jog.d10()
            danotot = self.jog.danotot(d10,d20)
            self.alvo.hp -= danotot
            print(f"{self.alvo.nome} perdeu {danotot} de HP!")
        else :
            print("Errou o dano!")



