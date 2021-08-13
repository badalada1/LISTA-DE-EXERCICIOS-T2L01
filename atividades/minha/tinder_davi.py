import random
#código: utf-8

#escolhi uma aleatoria da lista array "pessoas"
genero_ = input("por qual gênero você quer buscar? mulheres//homens: ")

if genero_ == "mulheres":
    print("você optou por buscar mulheres!")
    print('\n'*1)


if genero_ == "homens":
    print("você optou por buscar homens!")
    print("\n"*1)

while True:
    escolha = (genero_)
    if escolha == "mulheres":
        meninas = [
            "Ana",
            "Bruna",
            "marina",
            "juliana",
            "malu",
            "clara",        #Desculpa fiquei com preguiça de ajustar os nomes pois copiei do google-_-
            "Eva",
            "Simone",
            "Cecília",
            "Marie",
            "Margaret",
            "Valentina",
            "Rosa"]
        nome_pessoa = random.choice(meninas)
    if escolha == "homens":
        meninos = [
            "Pedro",
            "Matheus",
            "paulo",
            "Miguel",
            "Davi",         #Desculpa fiquei com preguiça de ajustar os nomes pois copiei do google-_-
            "Gabriel",
            "Arthur",
            "Lucas",
            "Matheus",
            "Pedro",
            "Guilherme",]
        nome_pessoa = random.choice(meninos)
    #mostrar nome
    print(f"{nome_pessoa}")

    #perguntar se pula ou não.
    print("match ou não?")
    esquerda_direita = input("")

    if esquerda_direita == "match": #só para variar o tipo de não
        print(f"você deu match! em {nome_pessoa}") #printa o nome da pessoa que deu match
    if esquerda_direita == "não": #só para variar os tipos de dar match
        print(f"você pulou {nome_pessoa}") #printa o nome da pessoa que pulou
