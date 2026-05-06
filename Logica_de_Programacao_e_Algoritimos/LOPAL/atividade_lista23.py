matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input("Digite o elemento [i][j]: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for i in range(2):
    for j in range(2):
        soma += matriz[i][j]

print("A soma de todos os elementos é:", soma)