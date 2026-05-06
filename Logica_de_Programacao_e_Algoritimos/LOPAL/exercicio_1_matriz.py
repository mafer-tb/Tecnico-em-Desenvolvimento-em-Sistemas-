
matriz_soma = []
matriz2 = []
matriz1 = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz1[{i}][{j}] =")))
    matriz1.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz2[{i}][{j}] =")))
    matriz2.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz_soma.append(linha)

#exibir matriz (repetir sempre que exibir matriz)
print("Matriz soma:")
for linha in matriz_soma:
    print(linha)
