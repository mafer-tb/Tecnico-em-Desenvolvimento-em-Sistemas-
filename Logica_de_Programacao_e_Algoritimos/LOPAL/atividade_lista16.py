numeros = []

for i in range(6):
    num = float(input("Digite o número: "))
    
    if num < 0:
        num = 1 
    
    numeros.append(num)

print("Valores finais:")
for n in numeros:
    print(n)