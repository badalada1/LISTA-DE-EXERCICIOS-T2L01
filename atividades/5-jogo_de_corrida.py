'''
05 – Escreva um programa em Python que faça o seguinte:
- Simule um jogo de corrida “drag racing” (arrancadão) onde dois carros correm em uma reta até a linha de chegada
- Pergunte quantos segundos o carro 1 levou para cruzar a linha de chegada
- Pergunte quantos segundos o carro 2 levou para cruzar a linha de chegada
- Teste se o carro 1 demorou menos que o carro2, e informe o vencedor, mas além disso calcule a diferença de segundos para montar a mensagem
- Faça o mesmo para o carro 2
'''
print("Quantos segundos o carro 1 levou?")
carro1_tempo = float(input(""))
print("Quantos segundos o carro 2 levou?")
carro2_tempo = float(input(""))

diferenca = carro1_tempo - carro2_tempo

if carro1_tempo < 1000:
    print("Vencedor carro 1")
    print(f"com {diferenca} segundos de diferença")
elif carro2_tempo < 1000:
    print("Vencedor carro 2")
    print(f"com {diferenca} segundos de diferença!")
