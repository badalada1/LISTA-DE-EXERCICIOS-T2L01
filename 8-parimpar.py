'''
08 – Escreva um programa em Python que faça o seguinte:
- Usando o operador que calcula o resto de divisão, verifique se um número informado pela pessoa é par ou ímpar.
- Solicite que a pessoa informe um número
- Calcule a divisão desse número por 2 usando o operador de resto da divisão (%)
- Se o resultado for 0, informe que o número digitado é par
- Senão, informe que é ímpar.
'''

numero = int(input("Digite um numero: "))

if (numero%2) == 0:
    print("Par")
else:
    print("Ímpar")