'''
9 – Escreva um programa em Python que faça o seguinte:
- Identifique em que nível a pessoa é cringe.
- Crie uma variável para ir somando o valor de cringisse.
- Pergunte se a pessoa gosta de emoji.
- Se a resposta for sim, a variável cringe deve aumentar em 1 (cringe = cringe + 1)
- Depois pergunte se a pessoa gosta de séries antigas.
- Se a resposta for sim, a variável cringe deve aumentar em 1 (cringe = cringe + 1)
- Por último, pergunte se a pessoa gosta de apreciar tipos diferentes de café.
- Se a resposta for sim, a variável cringe deve aumentar em 1 (cringe = cringe + 1)
- No final, teste o resultado. Se a variável cringe for 0, informe que a pessoa passou no teste e não é cringe.
- Caso contrário, informe o nível cringe da pessoa.
'''
cringe_soma_valor = 0

print("Você gosta de emoji?")
gosta_de_emoji = str(input(""))
if gosta_de_emoji == "sim":
    cringe_soma_valor += 1

print("Você gosta de séries antigas?")
gosta_de_series = str(input(""))
if gosta_de_series == "sim":
    cringe_soma_valor += 1

print("gosta de apreciar tipos diferentes de café?")
gosta_de_cafe = str(input(""))
if gosta_de_cafe == "sim":
    cringe_soma_valor += 1

if cringe_soma_valor == 0:
    print("Parabéns você não é cringe!")
else:
    print(f"parabéns você é cringe! seu valor de cringisse é {cringe_soma_valor}!")
