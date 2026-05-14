from jogador import Jogador
class Partida :
    def __init__(self,jogadores:Jogador):
        self.jogadores = jogadores
        self.mortos:list[Jogador] = []

    @classmethod
    def registrar_jogadores(cls,qj,hp):
        jogadores = []
        for i in range(qj):
            # nome = str (input (f"Nome do jogador{i+1}"))
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
        print("Vivos :")
        for jog in self.jogadores :
            print(jog.nome)
        if self.mortos :
            print("Lista de mortos :")
            for morto in self.mortos :
                print(morto.nome)

    def fim_partida (self):
        if len(self.jogadores) <=1 :
            if self.jogadores[0].hp >= 1 :
                campeao:Jogador = self.jogadores[0]
                print(f"{campeao.nome} Venceu a partida!")
            else :
                print("Todo mundo morreu ")
            return True

        return False



