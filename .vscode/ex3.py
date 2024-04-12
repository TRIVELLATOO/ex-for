while True:
    nm = int(input("insira um valor de 1 a 10 e obtenha sua tabuada: "))

    if nm > 10:
        print("valor invalido")
    elif nm < 1:
        print("valor invalido")
    else:
        for i in range (1,11):
            print (f"{nm} x {i} = {nm * i}")