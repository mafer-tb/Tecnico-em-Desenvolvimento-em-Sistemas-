numeros = []

for i in range(6):
    n = int(input("Digite o número: "))
    numeros.append(n)

print("Números pares:")
for n in numeros:
    if n % 2 == 0:
        print(n)