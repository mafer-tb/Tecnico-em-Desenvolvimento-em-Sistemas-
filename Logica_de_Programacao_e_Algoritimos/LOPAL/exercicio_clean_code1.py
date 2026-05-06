numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite a {i+1}ª nota:")))

soma = sum(numeros)

print("A soma total é:",soma )

