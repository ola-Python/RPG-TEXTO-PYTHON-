import os
from random import choices, uniform
from time import sleep
from interface.funcoes import  limpar_tela
qualidade = {
            "comum": 0.2,
            "raro": 0.3,
            "épico": 0.5,
            "lendário": 0.8,
            "mítico": 1.4
        }



builds = {
    "normal":80,
    "sorte":20
}

build = choices(list(builds.keys()),
                weights= list(builds.values()),
                k=1)[0]
print(build)
agi = 20
print(f"agi : {agi}")
if build == "sorte" :
    agi = int(agi / 2)
print(f"agi : {agi}")
# formula para calcular sortemax do anel
sorte = max(0.1,min(round(qualidade["épico"] / 1.6 * 0.1 * 26 ,  1),1.3))

print("sortemax = ",sorte)
print(f"sorte = {round(uniform(0.1,sorte),1)}")
