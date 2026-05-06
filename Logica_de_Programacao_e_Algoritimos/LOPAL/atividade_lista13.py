soma = 0
quantidade = 0
numero = 0

while (numero != -1):
    numero = float(input("Digite um número (-1 para encerrar): "))

    if(numero != -1):
        soma += numero
        quantidade += 1

media = soma / quantidade
print("Média:", media)