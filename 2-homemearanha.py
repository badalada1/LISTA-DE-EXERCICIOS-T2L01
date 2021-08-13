'''
02 – Escreva um programa em Python que faça o seguinte:
- Pergunte ao homem-aranha quantas cargas de teia ele possui.
- Depois, pergunte quantos prédios ele pretende escalar.
- Cada carga de teia é suficiente para escalar 3 prédios. Por isso, você precisa calcular se o homem-aranha tem cargas de teia suficientes:
- Faça um cálculo de dividir a quantidade de cargas de teia por 3. Isso vai dizer quantos prédios são possíveis de se escalar.
- Teste se a quantidade de prédios pretendidos é menor que a quantidade de prédios possíveis. Se for, avise o homem-aranha que ele precisa recarregar suas teias.
'''

carga = int(input("quantas teias você tem homiranha?"))
prediso = int(input("quantos prédios vc quer escalar homiranha?"))

total = carga / 3

if(carga >= total):
    print("você poderá pular na ponta de todos os prédios")
elif(carga < total):
    print("recarregue suas teias imediato")
