'''
10 – Escreva um programa em Python que faça o seguinte:
- Simule um labirinto onde o personagem deve escolher entre esquerda e direita.
- Pergunte para qual lado o personagem quer ir.
- Um dos dois é o caminho certo, e o outro é uma trollagem (você define qual é qual).
- Invente formas engraçadas de ser trollado.
- Você escreverá cinco ciclos dessa forma:
- Primeiro pergunte se o personagem vai para a direita ou para a esquerda
- Teste a resposta e diga se avançou sem problemas ou se caiu na trollagem informando o que aconteceu.
- Depois repita o ciclo, pergunte se o personagem vai para a direita ou esquerda.
- Teste a resposta e diga se avançou sem problemas ou se caiu na trollagem informando o que aconteceu.
- Use uma variável criada no começo do programa para somar as trollagens que o personagem caiu.
- Para cada trollagem, some mais um na variável (trollagem = trollagem + 1)
Ao final, teste se o personagem chegou intacto e mostre uma mensagem dando parabéns, ou senão mostre uma mensagem dizendo em quantas trollagens ele caiu.
'''

lado = print("Para qual lado você quer ir? esquerda//direita")
trolagem_pontuacao = 0

lado1 = input("Qual lado: ")
if lado1 == "esquerda":
    print("você avançou!")
else:
    trolagem_pontuacao += 1
    print("errou babaca!")
lado2 = input("Qual lado: ")
if lado2 == "esquerda":
    print("você avançou!")
else:
    trolagem_pontuacao += 1
    print("eroru otário!")
lado3 = input("Qual lado: ")
if lado3 == "esquerda":
    print("você avançou!")
else:
    trolagem_pontuacao += 1
    print("c era o bichão, agora perdeu!")
lado4 = input("Qual lado: ")
if lado4 == "direita":
    print("você avançou!")
else:
    trolagem_pontuacao += 1
    print("você caiu em uma furada!")
lado5 = input("Qual lado: ")
if lado5 == "direita":
    print("você avançou!")
else:
    print("você caiu em mais uma trolagem hahaha!")
    trolagem_pontuacao += 1

if trolagem_pontuacao == 0:
    print("Parabéns você chegou e nem viu o perigo")
elif trolagem_pontuacao >= 1:
    print(f"você caiu em {trolagem_pontuacao}!")
