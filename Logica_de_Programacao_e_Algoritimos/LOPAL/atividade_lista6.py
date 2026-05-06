numeros = []
maior = -999999999999999

for i in range(5):
    numeros.append(int(input("Digite o número: ")))

for numero in numeros:
    if(numero > maior):
        maior = numero

print("O maior valor é:", maior)

