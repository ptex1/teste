import colorama
from base_de_perguntas import *
from funcoes_obrigatorias import *
from colorama import *




base_transformada = transforma_base(quest)
pos_premio = 0
premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
continuar = True
num_questao = 1
lista_questoes_sorteadas = []
num_ajudas = 2
num_pulos = 3
pode_ajuda = True

def pergunta_ao_usuario():
    resposta = input("Qual sua resposta?! ")
    if resposta in ["A", "B", "C", "D", "ajuda", "pula","parar"]:
        return resposta
    else:
        print(Fore.RED + Style.BRIGHT + "Resposta inválida" + Style.RESET_ALL)
        pergunta_ao_usuario()

#checagem da base de perguntas

jogo_defeito = False
validacao =  valida_questoes(quest)
for i in range(len(validacao)):
    if validacao[i] != {}:
        print(f"A pergunta {i} contém o erro a seguir: {validacao[i]}")
        jogo_defeito = True

if jogo_defeito:
    print(Fore.RED + Style.BRIGHT + "Base de perguntas com erro, o jogo será encerrado" + Style.RESET_ALL)
    exit()

#introducao

print(Fore.MAGENTA + Style.BRIGHT + "\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n" + Style.RESET_ALL)
nome = input("Qual seu nome? ")
print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!\n")
print(Fore.CYAN + Style.BRIGHT + "As opcões de resposta são 'A','B','C','D','ajuda','pula' e 'parar'!\n\n" + Style.RESET_ALL)
input("Aperte ENTER para continuar...")
print("\nO jogo já vai começar! Lá vem a primeira questão!\n\n")
print("Vamos começar com questões de nível FACIL!")
input("Aperte ENTER para continuar...")

#inicio do jogo


def acao(resposta,questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios):
    if resposta == "ajuda":
        if pode_ajuda:
            if num_ajudas > 0:
                num_ajudas -= 1
                print(f"Ok, lá vem ajuda! Você ainda tem {num_ajudas} ajudas!")
                input("Aperte ENTER para continuar...")
                print(gera_ajuda(questao))
                print(questao_para_texto(questao,num_questao))
                resposta = pergunta_ao_usuario()
                pode_ajuda = False
                acao(resposta,questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)
            else:
                print(Fore.RED + Style.BRIGHT + "Você não possui mais ajudas, escolha outra alternativa" + Style.RESET_ALL)
                resposta = pergunta_ao_usuario()
                acao(resposta, questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)
        else:
            print(Fore.RED + Style.BRIGHT + "Você já utilizou 'ajuda' nesta pergunta, escolha outra alternativa" + Style.RESET_ALL)
            resposta = pergunta_ao_usuario()
            acao(resposta, questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)
    elif resposta == "pula":
        if num_pulos > 0:
            num_pulos -= 1
            num_questao += 1
            print(f"Ok, pulando! Você ainda tem {num_pulos}")
            input("Aperte ENTER para continuar...")

            questao = sorteia_questao_inedita(base_transformada,nivel,lista_questoes_sorteadas)
            print(questao_para_texto(questao,num_questao))
            resposta = pergunta_ao_usuario()
            return acao(resposta, questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)
        else:
            print("Você já utilizou todos os 'pular, selecione outra opção")
            print(questao_para_texto(questao,num_questao))
            resposta = pergunta_ao_usuario()
            acao(resposta, questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)
    elif resposta == questao["correta"]:
        if pos_premio == 8:
            print(Fore.GREEN + Style.BRIGHT + "PARABENS, você zerou o jogo e ganhou um milhão de reais" + Style.RESET_ALL)
            exit()
        else:
            print(Fore.GREEN + Style.BRIGHT + f"Você acertou! Seu prêmio atual é de R${premios[pos_premio]}.00" + Style.RESET_ALL)
            pos_premio += 1
    elif resposta == "parar":
        quer_parar = input(f"Deseja mesmo parar [S/N]?? Caso responda 'S', sairá com R${premios[pos_premio]}.00 ")
        if quer_parar == "S":
            print(f"\nOK! Você parou e seu prêmio é de R$ {premios[pos_premio]}.00")
            exit()
    else:
        print(Fore.RED + Style.BRIGHT +f"Que pena! Você errou e vai sair sem nada :("+ Style.RESET_ALL)
        exit()
    return pode_ajuda, num_ajudas, num_pulos, num_questao, pos_premio


while pos_premio < 9:
    pode_ajuda = True
    if num_questao < 4:
        nivel = "facil"
    elif num_questao < 7:
        nivel = "medio"
    else:
        nivel = "dificil"
    if pos_premio == 4:
        print("HEY! Você passou para o nível MEDIO")
    elif pos_premio == 7:
        print("HEY! Você passou para o nível DIFICIL")
    questao = sorteia_questao_inedita(base_transformada,nivel,lista_questoes_sorteadas)
    print(questao_para_texto(questao,num_questao))
    resposta = pergunta_ao_usuario()
    pode_ajuda, num_ajudas, num_pulos,num_questao, pos_premio  = acao(resposta,questao,num_questao,pode_ajuda,num_ajudas,num_pulos,pos_premio,premios)

    num_questao += 1






