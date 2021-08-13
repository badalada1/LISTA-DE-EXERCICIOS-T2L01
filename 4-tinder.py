'''
04 – Escreva um programa em Python que faça o seguinte:
- Mostre para quem está jogando o nome de uma pessoa (simulando que seja alguém conhecido, pode usar o nome que você quiser)
- Depois, peça para quem está jogando escrever “esquerda” para simular que arrastou para a esquerda (não curte a pessoa informada) ou “direita” se arrasta para a direita (curte a pessoa informada)
- Se arrastou para a esquerda, mostre uma mensagem de “não deu match”
- Se arrastou para a direita, mostre uma mensagem de “deu match”
'''
import random
limite = 1
while limite <=10:
    limite += 1
    #criei uma lista com nomes de pessoas
    pessoas = ["Pedro","Ana","Maria","Paulo","Matheus","Mariana","Davi"]
    #escolhi uma aleatoria da lista array "pessoas"
    nome_pessoa = random.choice(pessoas)
    #mostro ela na tela
    print(f"{nome_pessoa}")
    #perguntar se pula ou não.
    print("match ou não?")
    esquerda_direita = input("")

    if esquerda_direita == "match": #só para variar o tipo de não
        print(f"você deu match! em {nome_pessoa}") #printa o nome da pessoa que deu match
    elif esquerda_direita == "não": #só para variar os tipos de dar match
        print(f"você pulou {nome_pessoa}") #printa o nome da pessoa que pulou
