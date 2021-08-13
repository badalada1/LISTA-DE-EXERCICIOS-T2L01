carga = int(input("quantas teias você tem homiranha?"))
prediso = int(input("quantos prédios vc quer escalar homiranha?"))

total = carga / 3

if(carga >= total):
    print("você poderá pular na ponta de todos os prédios")
elif(carga < total):
    print("recarregue suas teias imediato")
