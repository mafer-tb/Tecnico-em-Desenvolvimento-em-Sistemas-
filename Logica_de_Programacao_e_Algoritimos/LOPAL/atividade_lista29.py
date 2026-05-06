matriz = []
identidade = True

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Elemento [i][j]: ")))
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if i == j and matriz[i][j] != 1:
            identidade = False
        if i != j and matriz[i][j] != 0:
            identidade = False

if identidade:
    print("É matriz identidade")
else:
    print("Não é matriz identidade")