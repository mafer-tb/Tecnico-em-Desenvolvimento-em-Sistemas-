matriz = []

for i in range(3):
    linha = []
    for j in range(2):
        linha.append(int(input("Elemento [i][j]: ")))
    matriz.append(linha)

print("Números maiores que 10:")
for i in range(3):
    for j in range(2):
        if matriz[i][j] > 10:
            print(matriz[i][j])