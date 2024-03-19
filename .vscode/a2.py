a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

dlt = b**2 - 4 * a * c

if dlt > 0:
    print("possui 2 raizes reais")

elif dlt == 0:
    print ("possui 1 raiz real")

else:
    print ("nao possui raiz real")
