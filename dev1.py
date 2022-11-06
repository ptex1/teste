dicio_atl = {}
nome_do_atl = "zero"
while nome_do_atl != "sair":
    nome_do_atl = input("nome do atleta")
    aceleracao_do_atl = input("aceleracao do atleta")
    dicio_atl[nome_do_atl] = aceleracao_do_atl

import math
t_dicio = {}
def menor_tempo(dicio_atl):
    for atl in dicio_atl:
        t = math.sqrt(200/dicio_atl[atl])
        t_dicio[atl] = t
    print(t_dicio)
    return min(t_dicio)

for atl in dicio_atl:
    if menor_tempo(dicio_atl) == math.sqrt(200/dicio_atl[atl]):
        vencedor = atl
        break

menor_tempo = menor_tempo(dicio_atl)
print(f'O vencedor é {vencedor} com tempo de conclusão de {menor_tempo} s')
