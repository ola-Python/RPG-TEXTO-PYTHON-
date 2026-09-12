from rich import print
from rich.panel import Panel
from time import sleep
import os

def limpar_tela() :
    os.system("cls")

def mostrar_mensagem(mensagem,titulo,pausa=0.8,largura=30,estilo="") :
    linhas = mensagem.split("\n")
    texto = ""
    for linha in linhas :
        texto += linha + "\n"
        limpar_tela()

        print(Panel(
            renderable=texto,title=titulo,width=largura,style=estilo
        ))
        sleep(pausa)
