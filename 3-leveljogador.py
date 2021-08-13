'''
03 – Escreva um programa em Python que faça o seguinte:
- Pergunte ao jogador/jogadora seu level (ou nível de experiência)
- Teste para qual fase esse level permite que o jogador/jogadora inicie e lhe informe:
- Se o level for menor de 10, é obrigatório acessar a fase 1.
- Se o level for maior ou igual a 10, pode iniciar a fase 2.
'''

nivel_jogador = input (int("qual seu nível:"))

if nivel_jogador >= 10:
    print("inicie na fase 2!")
elif nivel_jogador <= 10:
    print("inicie na fase 1!")
