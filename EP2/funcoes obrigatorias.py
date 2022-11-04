import random

def transforma_base(lista_questoes):
    nova_base = {}
    for questao in lista_questoes:
        if questao["nivel"] not in nova_base:
            nova_base[questao["nivel"]] = [questao]
        else:
            nova_base[questao["nivel"]].append(questao)
    return nova_base


def valida_questao(questao):
    saida = {}
    saida_letras = {}
    chaves = questao.keys()
    if len(chaves) != 4:
        saida["outro"] = "numero_chaves_invalido"
    if "titulo" not in chaves:
        saida["titulo"]= 'nao_encontrado'
    else:
        titulo = questao["titulo"]
        if not titulo or not titulo.strip():
            saida["titulo"] = "vazio"
    if "nivel" not in chaves:
        saida["nivel"]= 'nao_encontrado'
    else:
        nivel = questao["nivel"]
        if nivel not in ["facil", "medio", "dificil"]:
            saida['nivel'] = "valor_errado"
    if "opcoes" not in chaves:
        saida["opcoes"]= 'nao_encontrado'
    else:
        opcoes = questao["opcoes"]
        if len(opcoes) != 4:
            saida['opcoes'] = 'tamanho_invalido'
        else:
            alternativas = opcoes.keys()
            if list(alternativas) != ['A', 'B', 'C', 'D']:
                saida["opcoes"]= 'chave_invalida_ou_nao_encontrada'
            for alternativa, letra in opcoes.items():
                if not letra or not letra.strip():
                    saida_letras[alternativa] = "vazia"
                    saida["opcoes"] = saida_letras 
    if "correta" not in chaves:
        saida["correta"]= 'nao_encontrado'
    else:
        correta = questao["correta"]
        if correta not in ['A', 'B', 'C', 'D']:
            saida['correta'] = 'valor_errado'
      
    return saida


def valida_questoes(lista_questao):
    retorno = []
    for questao in lista_questao:
        if valida_questao(questao):
            retorno.append(valida_questao(questao))
        else:
            retorno.append({})
    return retorno


def sorteia_questao(dic_questoes,nivel):
    questoes_nivel = dic_questoes[nivel]
    questao = random.choice(questoes_nivel)
    return questao


def sorteia_questao_inedida(dic_questoes,nivel,lista_sorteadas):
    questao_sorteada = ""
    while questao_sorteada not in lista_sorteadas:
        questao_sorteada = sorteia_questao(dic_questoes,nivel)
        if questao_sorteada not in lista_sorteadas:
            lista_sorteadas.append(questao_sorteada)
    return questao_sorteada


def questao_para_texto(dic_questao,num_questao):
    traco = "-" * 40
    string = f"{traco}\nQUESTAO {num_questao}\n\n{dic_questao['titulo']}\n\nRESPOSTAS:\n"
    alternativas = ""
    for alternativa, resposta in dic_questao["opcoes"].items():
        alternativas += f"{alternativa}: "
        alternativas += f"{resposta}\n"
    return string + alternativas