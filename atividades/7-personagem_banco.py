'''
7 – Escreva um programa em Python que faça o seguinte:
- Simule um jogo no qual o personagem chega em um banco.
- Crie uma variável para armazenar o saldo do personagem, e atribua um valor qualquer para esse saldo.
- Mostre uma mensagem perguntando quanto o personagem deseja retirar.
- Teste se o personagem tem o valor solicitado em sem saldo
- Se tiver, diminua o valor da retirada e mostre o saldo atualizado.
- Se não tiver, informe que o saldo é insuficiente e mostre o saldo que ele tem.
'''

saldo_personagem = 500
print(f"Seu saldo é de: {saldo_personagem}")

print("Quanto você deseja retirar?")
retirar = int(input(""))

if retirar > saldo_personagem:
    print("você não tem saldo suficiente para retirar esse valor!")
else:
    retirar_saldo = saldo_personagem - retirar
    print(f"Seu saldo agora é de: {retirar_saldo}")

