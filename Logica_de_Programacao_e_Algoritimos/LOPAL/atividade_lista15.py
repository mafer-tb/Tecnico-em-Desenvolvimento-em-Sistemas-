numeros = []
soma = 0
media = 0

for i in range(8):
    num = float(input("Digite o número: "))
    numeros.append(num)
    soma = soma + num 

media = soma /8
for numero in numeros:
    if numero > media:
        print(numero,">", media)