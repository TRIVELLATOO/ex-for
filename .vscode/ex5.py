import random
ni = []
np = []

for i in range (0, 10):
    numero = random.randint(0, 100)
    if numero % 2 == 0:
        np.append(numero)
    else:
        ni.append(numero)

print(f"Quantidade de nrs pares:{len(np)} ({np})")
print(f"Quantidade de nrs ímpares: {len(ni)} ({ni})")
