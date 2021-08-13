'''
11 – Escreva um programa em Python que faça o seguinte:
- Pergunte a pontuação obtida por três pessoas em um jogo: 
- Faça uma pergunta por pessoa, guardando a pontuação de cada nas variáveis correspondentes.
- Depois, faça os testes pra mostrar na tela a pessoa que ficou em primeiro lugar:
- Teste se pessoa 1 > pessoa 2. Se for, teste se pessoa 1 > pessoa 3. Aí você sabe que a pessoa 1 é a vencedora.  
- Pode usar a mesma lógica para testar cada pessoa e saber se a pontuação dela é maior que as outras duas, para identificar quem venceu.
'''

print("informe a pontuacao dos jogadores de 1 a 10")

um = int(input("informe a pontuação do jogador um"))
dois = int(input("informe a pontuação do jogador dois"))
tres = int(input("informe a pontuação do jogador três"))


if(um > dois):
    if(um > tres):
        print("o jogador um atingiu a maior pontuação!")
elif(dois > um):
    if(dois > tres):
        print("o jogador um atingiu a maior pontuação!")
else:
    print("o jogador três venceu!")

print("obrigado por participar!")
