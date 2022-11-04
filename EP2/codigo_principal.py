from base_de_perguntas import *
from funcoes_obrigatorias import *

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
num_pergunta = 1
lista_questoes_sorteadas = []
while premio < 1000000:
    sorteia_questao_inedida(base_transformada,"FACIL",lista_questoes_sorteadas)



