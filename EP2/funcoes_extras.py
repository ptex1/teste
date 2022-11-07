from base_de_perguntas import *
from funcoes_obrigatorias import *




def acao_a_tomar(resposta):
    questao = sorteia_questao_inedida(base_transformada,nivel,lista_questoes_sorteadas)

    if resposta == "parar":
        return exit

    if resposta == "pular":
        return sorteia_questao_inedida(base_transformada,nivel,lista_questoes_sorteadas)

    if resposta == "ajuda":
        gera_ajuda(questao)
        if pode_ajuda:
            if num_ajudas > 0:
                num_ajudas -= 1
                pode_ajuda = False
                print(f"Ok, lá vem ajuda! Você ainda tem {num_ajudas} ajudas!")
                input("Aperte ENTER para continuar...")
                print(gera_ajuda(questao))
                print(questao_para_texto(questao,num_questao))
                return pergunta_ao_usuario()
            else:
                print("Você não possui mais ajudas")
                resposta = pergunta_ao_usuario()
        else:
            print("Você já pediu ajuda nesta pergunta, escolha outra opção")
            return pergunta_ao_usuario()

    if resposta == questao["correta"]:
        print("Você acertou! Seu prêmio atual é de R$ {premios[num_acertos]}")
        return sorteia_questao_inedida

    elif resposta != questao["correta"] and resposta == 'A' or 'B' or 'C' or 'D':
        print("Que pena! Você errou e vai sair sem nada :(")
        return sorteia_questao_inedida
