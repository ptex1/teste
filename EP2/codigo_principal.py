from base_de_perguntas import *
from funcoes_obrigatorias import *


def pergunta_ao_usuario():
    resposta = input("Qual sua resposta?! ")
    if resposta in ["A", "B", "C", "D", "ajuda", "pular"]:
        return resposta
    else:
        print("Resposta inválida")
        pergunta_ao_usuario()

#checagem da base de perguntas

jogo_defeito = False
validacao =  valida_questoes(quest)
for i in range(len(validacao)):
    if validacao[i] != {}:
        print(f"A pergunta {i} contém o erro a seguir: {validacao[i]}")
        jogo_defeito = True

if jogo_defeito:
    print("Base de perguntas com erro, o jogo será encerrado")
    exit()

#introducao

print("\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n")
nome = input("Qual seu nome? ")
print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n")
print("As opcões de resposta são 'A','B','C','D','ajuda','pula' e 'parar'!\n\n")
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n\n")
print("Vamos começar com questões de nível FACIL!")
input("Aperte ENTER para continuar...")

#inicio do jogo

base_transformada = transforma_base(quest)
premio = 0
premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
continuar = True
num_questao = 1
lista_questoes_sorteadas = []
num_ajudas = 2
num_pulos = 3

while premio < 1000000 and continuar:
    pode_ajuda = True
    if num_questao < 4:
        nivel = "facil"
    elif num_questao < 7:
        nivel = "medio"
    else:
        nivel = "dificil"
    questao = sorteia_questao_inedida(base_transformada,nivel,lista_questoes_sorteadas)
    print(questao_para_texto(questao,num_questao))
    resposta = pergunta_ao_usuario()
    
    if resposta == "ajuda":
        if pode_ajuda:
            if num_ajudas > 0:
                num_ajudas -= 1
                pode_ajuda = False
                print(f"Ok, lá vem ajuda! Você ainda tem {num_ajudas} ajudas!")
                input("Aperte ENTER para continuar...")
                gera_ajuda(questao)
                print(questao_para_texto(questao,num_questao))
            else:
                print("Você não possui mais ajudas")
                resposta = pergunta_ao_usuario()
        else:
            print("Você já pediu ajuda nesta pergunta, escolha outra opção")
    if resposta == "pular":
        print()
    num_questao += 1






