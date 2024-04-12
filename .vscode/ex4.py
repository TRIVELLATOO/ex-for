idades = []
sm = 0
md = 0
for i in range (0,5):
    idade = int(input(f"insira a {i+1} idade"))
    idades.append(idade)
    sm += idade
    md = sm/len (idades)
print(f"a média das idades é {md}")