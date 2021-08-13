'''
12 – Escreva um programa em Python que faça o seguinte:
- Calcule a pontuação de um jogo estilo Guitar Hero.
- Pergunte a quantidade total de notas musicais da fase.
- Pergunte a quantidade de notas musicais acertadas. Esse número será o total de pontos.
- Pergunte a quantidade máxima de notas musicais acertadas em sequência sem errar.
- Agora calcule a porcentagem de acerto (100 * acertos / total)
- Também calcule a porcentagem de notas acertadas em sequência (100 * sequencia / total)
- Depois calcule o bônus:
- Se a sequência de acerto for maior que 80%, acrescente 100 pontos no total.
- Senão, teste se a sequência de acerto foi maior de 50%. Nesse caso acrescente 50 pontos no total.
- Senão, teste se a sequência de acerto foi maior de 20%. Nesse caso acrescente 20 pontos no total.
- Finalmente, mostre para quem está jogando:
- Porcentagem de acerto, porcentagem de notas acertadas em sequência, pontos iniciais, bônus, pontos finais.
'''

print("Qual a quantidade total de nostas tocou na fase?")
total_notas = int(input(""))

print("Qual a quantidade de notas acertadas na fase?")
max_notas_acertadas = int(input(""))

print("Quantas notas acertos em sequência na fase?")
notas_sequencia_acertadas = int(input(""))

procentagem_de_acerto = 100 * max_notas_acertadas / total_notas

porcentagem_notas_sequencia = 100 * notas_sequencia_acertadas / total_notas

total_pontos = 0
if notas_sequencia_acertadas > procentagem_de_acerto:
    total_pontos = 100
elif notas_sequencia_acertadas > procentagem_de_acerto:
    total_pontos = 50
elif notas_sequencia_acertadas > procentagem_de_acerto:
    total_pontos = 20
    