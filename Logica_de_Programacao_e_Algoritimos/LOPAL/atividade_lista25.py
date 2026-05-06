matriz = []

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Elemento [i][j]: ")))
    matriz.append(linha)

for j in range(3):
    soma = 0
    for i in range(2):
        soma += matriz[i][j]
    print(f"Soma da coluna {j}: {soma}")