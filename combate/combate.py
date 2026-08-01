from time import sleep

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
                for i in range(self.qj):
                    if i != self.indice:
                        print(f"{f"[ {i} ]":<5} {self.jogadores[i].nome}")
                print(f"{"[-1 ]":<5} Voltar")
                try:
                    ialvo =  int (input ("Escolha quem você vai atacar"))
                    if ialvo == -1 :
                        return False
                    if ialvo == self.indice :
                        print("Você não pode se atacar!")
                        continue
                    if ialvo > self.qj-1 or ialvo < 0 :
                        continue
                    else :
                        self.alvo = self.jogadores[ialvo]
                        return True
                except ValueError :
                    print("Digite um valor válido")
        else  :
            for i in range (self.qj) :
                if i != self.indice :
                    ialvo = i
        self.alvo = self.jogadores[ialvo]
        return True

    def atacar (self) :
        if not self.escolher_alvo() :
            return
        d20 = self.jog.d20()
        if d20 > 10 :
            d10 = self.jog.d10()
            danotot = self.jog.danotot(d10,d20)
            self.alvo.hp -= danotot
            print(f"{self.alvo.nome} perdeu {danotot} de HP!")
        else :
            print("Errou o dano!")
        sleep(1.5)

        return True



