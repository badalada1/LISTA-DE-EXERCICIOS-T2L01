'''
6 – Escreva um programa em Python que faça o seguinte:
- Crie uma variável para armazenar o valor do recorde de pontos de uma fase, e atribua um valor qualquer a sua escolha.
- Pergunte a quem está jogando quantas moedas pegou em uma fase.
- Pergunte também quantos diamantes pegou.
- Cada diamante vale 10 moedas.
- Calcule a pontuação total (moedas + diamantes * 10)
- Teste se a pontuação total bateu o recorde.
- Caso verdadeiro, informe que o recorde foi batido com a pontuação total.
- Caso falso, só informe a pontuação.
'''

valor_recorde = 4500
print("Quantas moedas você pegou em uma fase?")
moedas_jogador = int(input(""))

print("Quantos diamantes você pegou em uma fase?")
diamantes_jogador = int(input(""))

pontuacao_total = moedas_jogador + diamantes_jogador * 10

if pontuacao_total >= pontuacao_total:
    print(f"Parabéns você passou o recorde! \nsua pontuação total foi de: {pontuacao_total}")
else:
    print(f"sua pontuação foi de: {pontuacao_total}")
