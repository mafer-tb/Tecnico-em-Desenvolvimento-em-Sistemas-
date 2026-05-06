matriz = []
maior = None

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Elemento [i][j]: "))
        linha.append(valor)
        if maior or valor > maior:
            maior = valor
    matriz.append(linha)

print("Maior valor:", maior)