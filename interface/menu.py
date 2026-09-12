from jogador import Jogador
from rich.table import Table
from rich.panel import Panel
from rich import print
from rich.text import Text
from rich.columns import Columns
from rich.box import HEAVY



def Tabelajogadores(jogadores:list[Jogador],jogatual:Jogador):

    tabela = Table(title=f"Jogadores ")
    tabela.add_column("", width=1)
    tabela.add_column("Nome",justify="left",style="bold")
    tabela.add_column("[#0BC900]HP ❤️[/]",justify="center")
    tabela.add_column("[#FFF300]Moedas ✪ [/]",justify="left",width=9,style="#FFF300")

    for jog in jogadores :
        alerta = ""
        corhp = "[#0BC900]"
        nomecor = "[bold]"
        if 20 <= jog.hp <= 30:
            corhp = "[#FFA500]"  # laranja em rgb
            nomecor = "[#FFA500]"
        elif jog.hp < 20:
            corhp = "[bold red]"
            nomecor = "[bold red]"
            alerta = "[bold red]⚠️[/]"
        marcador = "[red]▻[/]" if jog == jogatual else ""
        tabela.add_row(f"{marcador}",f"{nomecor}{jog.nome}[/]{alerta}",f"{corhp}{jog.hp}[/]",f"{jog.moedas}")
    print(tabela)


def mostrar_acoes(jogatual:Jogador,turno):
    espada = jogatual.arma.nome if jogatual.arma else "Sem arma"
    anel = jogatual.anel.nome if jogatual.anel else "Sem anel"
    texto = Text()
    texto.append("[1] ⚔️ Atacar\n",style="bold red")
    texto.append("[2] ▣ Loja\n",style="bold #FFF300")
    texto.append("[3] ▤ Inventário\n",style="bold blue")
    opcoesPanel = Panel(texto,height=5,width=25,title="⚔ AÇÕES")
    status = f"[#0BC900]HP : [bold]{jogatual.hp}[/][/]"
    status +=f"    [#FFF300]Moedas ✪ : [bold]{jogatual.moedas}[/][/]"
    status += f"\n[#0EEE7E]Sorte: [bold]{jogatual.sorte}[/]x[/]"
    status+= f"\nEspada : {espada}"
    status+=f"\nAnel   : {anel}"
    statusPainel = Panel(status,
                         title=f"[bold red on black]{jogatual.nome}[/]",
                         width=30,height=6,box=HEAVY,subtitle=f"⏰ [bold red on black]Turno :{turno}[/]")
    print(Columns([opcoesPanel,statusPainel]))



