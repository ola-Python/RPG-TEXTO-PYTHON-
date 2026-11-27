from time import sleep
import sys
from pathlib import Path
import pygame
from random import random,randint

PASTA_PROJETO = Path(__file__).resolve().parent


if getattr(sys, "frozen", False):
    PASTA_BASE = Path(sys._MEIPASS)
else:
    PASTA_BASE = Path(__file__).resolve().parent

PASTA_SONS = PASTA_BASE / "sound"
pygame.mixer.init()

bonk = pygame.mixer.Sound(PASTA_SONS/"Bonk.ogg")
dano_soco =pygame.mixer.Sound(PASTA_SONS/"soco.ogg")
dano_soco2=pygame.mixer.Sound(PASTA_SONS/"soco2.ogg")
dano_espada=pygame.mixer.Sound(PASTA_SONS/"golpeespada1.ogg")
moedas =pygame.mixer.Sound(PASTA_SONS/"moedas.ogg")
dano_espada_forte =pygame.mixer.Sound(PASTA_SONS/"golpeespada2.ogg")
novo_slot =pygame.mixer.Sound(PASTA_SONS/"novo slot.ogg")
quebra_armadura =pygame.mixer.Sound(PASTA_SONS/"quebrar_armadura.ogg")
evento =pygame.mixer.Sound(PASTA_SONS/"evento_aleatorio.ogg")
raio =pygame.mixer.Sound(PASTA_SONS/"raio.ogg")
roubado =pygame.mixer.Sound(PASTA_SONS/"roubado.ogg")
esquiva =pygame.mixer.Sound(PASTA_SONS/"esquiva.ogg")
attloja =pygame.mixer.Sound(PASTA_SONS/"att_loja.ogg")
compra =pygame.mixer.Sound(PASTA_SONS/"compra.ogg")
equipar = pygame.mixer.Sound(PASTA_SONS/"equipar.ogg")
inventario =pygame.mixer.Sound(PASTA_SONS/"inventario.ogg")
fail = pygame.mixer.Sound(PASTA_SONS/"fail.ogg")
fail2 =pygame.mixer.Sound(PASTA_SONS/"bobsad.ogg")
mine_dano =pygame.mixer.Sound(PASTA_SONS/"minecraft damage.ogg")
atacar =pygame.mixer.Sound(PASTA_SONS/"atacar.ogg")
grave2=pygame.mixer.Sound(PASTA_SONS/"grave2.ogg")
golpe_armadura=pygame.mixer.Sound(PASTA_SONS/"armadura ataque1.ogg")
golpe_armadura2 =pygame.mixer.Sound(PASTA_SONS/"armadura ataque2.ogg")
dado=pygame.mixer.Sound(PASTA_SONS/"dado.ogg")
comer =pygame.mixer.Sound(PASTA_SONS/"mine comendo.ogg")
pocaomine=pygame.mixer.Sound(PASTA_SONS/"pocaomine.ogg")
xpmine=pygame.mixer.Sound(PASTA_SONS/"xpmine.ogg")
cassino=pygame.mixer.Sound(PASTA_SONS/"cassino.ogg")
roletando=pygame.mixer.Sound(PASTA_SONS/"roletando.ogg")
morte1=pygame.mixer.Sound(PASTA_SONS/"morte1.ogg")
morte2=pygame.mixer.Sound(PASTA_SONS/"morte2.ogg")
morte3=pygame.mixer.Sound(PASTA_SONS/"morte3.ogg")
morte4=pygame.mixer.Sound(PASTA_SONS/"morte4.ogg")
todos_morte=pygame.mixer.Sound(PASTA_SONS/"todo mundo morreu.ogg")
especial=pygame.mixer.Sound(PASTA_SONS/"especial.ogg")
fogocj=pygame.mixer.Sound(PASTA_SONS/"cj pegando fogo.ogg")
vitoria =pygame.mixer.Sound(PASTA_SONS/"vitoria.ogg")
clickmenu = pygame.mixer.Sound(PASTA_SONS/"click.ogg")
gtakmenu = pygame.mixer.Sound(PASTA_SONS/"menu gta.ogg")
minemenu = pygame.mixer.Sound(PASTA_SONS/"mine click.ogg")
levelup =pygame.mixer.Sound(PASTA_SONS/"level up.ogg")
upgradesom =pygame.mixer.Sound(PASTA_SONS/"upgradesom.ogg")
menuvoltarsom=pygame.mixer.Sound(PASTA_SONS/"menu voltar.ogg")
selecionarPersonagem = pygame.mixer.Sound(PASTA_SONS/"selecionar personagem.ogg")
comeco = pygame.mixer.Sound(PASTA_SONS/"comeco.ogg")
def mortesom() :
    variacao = randint(1,4)
    if variacao == 1 :
        morte1.play()
    elif variacao == 2 :
        morte2.play()
    elif variacao == 3:
        morte3.play()
    elif variacao == 4 :
        morte4.play()

def menusom () :
    variacao = randint(1,3)
    if variacao == 1 :
        clickmenu.play()
    elif variacao == 2 :
        gtakmenu.play()
    elif variacao == 3 :
        minemenu.play()


def errou_ataque() :
    chance = random()
    if chance < 0.80 :
        esquiva.play()
    else:
        variacao = randint(0,1)
        if variacao == 0 :
            fail.play()
        elif variacao == 1:
            fail2.play()

def dano_som(dano) :
    if dano <= 2 :
        varicao = randint(0,1)
        if varicao == 0 : bonk.play()
        elif varicao == 1 : fail.play()

    elif dano <= 10 :
        variacao = randint(0,2)
        if variacao == 0 :
            dano_soco.play()
        elif variacao == 1 :
            dano_soco2.play()
        elif variacao ==2 :
            mine_dano.play()
    elif dano <= 15:
        dano_espada.play()

    elif dano <= 35 :
        dano_espada_forte.play()
    else :
        grave2.play()




