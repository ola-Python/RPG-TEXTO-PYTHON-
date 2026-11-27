import som
from equipamento import Equipamento
from interface.funcoes import mostrar_mensagem
from random import randint,choice,choices




class Armadura(Equipamento) :
    def __init__(self,nome,defesa,durabilidade,raridade,valor):
        super().__init__(nome=nome,raridade=raridade,tipo="armadura",valor=valor)


        self.durabilidade = durabilidade
        self.durabilidademax = durabilidade
        self.defesa = defesa

    def __str__(self):
        return f"{Armadura.cores_raridade[self.raridade]}{self.nome}({self.durabilidade}/{self.durabilidademax})"

    def absorverDano(self,dano,jog):
        dano_absorvido = min(dano,self.defesa)
        dano_absorvido = min(dano_absorvido,self.durabilidade)

        #==========  SOM  ==========
        variacao = randint(0,1)
        if variacao == 0:
            som.golpe_armadura.play()
        elif variacao == 1:
            som.golpe_armadura2.play()
        #==============================
        mostrar_mensagem(f"{self.__str__()} [blue]Absorveu {dano_absorvido} do dano[/]"
                         f"\nDurabilidade {self.durabilidade} -> {self.durabilidade - dano_absorvido}",
                         titulo="ARMADURA", pausa=2.1, largura=35)

        self.durabilidade -= dano_absorvido

        return max(0,dano - dano_absorvido)

    def esta_quebrada(self):
        if self.durabilidade <= 0:
            som.quebra_armadura.play()
            mostrar_mensagem(
                f"💥 {self.nome} quebrou!",
                titulo="ARMADURA",
                estilo="red",
                pausa=2.4,
                largura=45
            )
            return True

        return False


    @classmethod
    def gerarArmadura(cls,turno,raridade=None):
        qualidade = {
            "comum": 0.4,
            "raro": 0.8,
            "épico": 1.4,
            "lendário": 1.8,
            "mítico": 2.5
        }

        pesos = [70, 32, 9, 2, 0.5]

        if raridade == None:
            raridade = choices(list(qualidade.keys()),
                               weights=pesos,
                               k=1
                               )[0]
        hpmin = 20
        hpmax = int(qualidade[raridade] * turno * 2)
        if hpmax < hpmin:
            hpmax = hpmin
        defesamin = 3
        defesamax = int(qualidade[raridade] * turno)
        if defesamax < defesamin:
            defesamax = defesamin

        match raridade :
            case "comum" :
                nomes = ["armadura de couro","armadura enferrujada","Armadura de Ferro Velho",
                         "Armadura de Aço Simples","armadura de Malha"]
                nome = choice(nomes).title()
            case "raro":
                nomes = ["armadura de ferro","Armadura do Cavaleiro","Armadura reforçada"]
                nome = choice(nomes).title()
                hpmin *= 1.2
                hpmax *= 1.3
            case "épico":
                nomes = ["Armadura das Sombras","Armadura do Dragão","Armadura do Arcano","armadura de cristal",
                         "armadura de gelo❄️"]
                nome = choice(nomes).title()
                hpmin *= 1.4
                hpmax *= 1.5
            case "lendário":
                nomes = ["Armadura dourada", "Armadura do Colosso","armadura do titã",
                         "Armadura da Fênix","Armadura do Rei"]
                nome = choice(nomes).title()
                hpmin *= 1.5
                hpmax *= 1.9
            case "mítico":
                nomes = ["Armadura DIVINA✝️","Armadura do Deus da guerra♎","Armadura do Caos☠️",
                         "Armadura do Abismo","armadura de sangue"]
                nome = choice(nomes).title()
                hpmin *= 1.9
                hpmax *= 2.3
        hpmin = int(hpmin)
        hpmax = int(hpmax)

        durabilidade = randint(hpmin,hpmax)
        defesa = randint(defesamin,defesamax)
        valor = int(0.15 * durabilidade + defesa // 3)

        return cls(
            nome=nome,
            raridade=raridade,
            durabilidade=durabilidade,
            defesa=defesa,
            valor=valor
        )