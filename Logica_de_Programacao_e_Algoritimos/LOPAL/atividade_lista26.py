maior = None

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    if maior is None or n > maior:
        maior = n

print("Maior número:", maior)