matriz = []
n = int(input("Digite um número:"))

#preencher matriz (repetir sempre que preencher matriz)
for i in range(n):
    linha = []
    for j in range(n):
        if(i==j):
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

#exibir matriz (repetir sempre que exibir matriz)
print("Matriz Identidade:")
for linha in matriz:
    print(linha)
