numero = int(input("Digite o número:"))
fatorial = 1

for i in range(numero,0,-1):
    fatorial = fatorial * i
print(numero,"! =", fatorial)