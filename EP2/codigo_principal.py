from base_de_perguntas import *
from funcoes_obrigatorias import *

#checagem da base de perguntas

validacao =  valida_questoes(quest)
base_transformada = transforma_base(quest)
print(validacao)


#introducao

print("\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n")
nome = input("Qual seu nome? ")
print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n")
print("As opcões de resposta são 'A','B','C','D','ajuda','pula' e 'parar'!\n\n")
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n\n")
print("Vamos começar com questões de nível FACIL!")
input("Aperte ENTER para continuar...")




