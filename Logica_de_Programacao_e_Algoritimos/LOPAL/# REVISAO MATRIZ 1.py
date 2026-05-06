# REVISAO MATRIZ 1 
# SOLICITAR A QUANTIDADE DE LINHAS 
# SOLICITAR A QUANTIDADE DE COLUNAS 
# PREENCHER A MATRIZ 
# CALCULAR A SOMA DE TODOS OS NUMEROS 
#--------------------------------------------------------------

# PASSO 1) VARIAVEIS 
linhas = int(input("Digite a quantidade de linhas:"))
colunas = int(input("Digite a quantidade de colunas:"))
matriz = []
soma = 0 

# PASSO 2) PREENCHER MATRIZ 
#SEMPRE REPETIR QUANDO PREENCHER MATRIZ
for i in range(linhas):
    linha = []
    for j in range (colunas):
        linha.append (int (input("Digite um número:")))
    matriz.append(linha)

# PASSO 3) PERCORRER A MATRIZ E CALCULAR A SOMA 
for i in range(linhas):
    for j in range(colunas):
        soma = soma + matriz[i][j]
print("Soma é:", soma )

