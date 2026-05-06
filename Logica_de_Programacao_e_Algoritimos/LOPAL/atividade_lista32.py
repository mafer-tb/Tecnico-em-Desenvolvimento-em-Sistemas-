vetor = []

for i in range(6):
    vetor.append(int(input(f"Número i: ")))

ordenado = True

for i in range(5):
    if vetor[i] > vetor[i + 1]:
        ordenado = False

if ordenado:
    print("Vetor ordenado")
else:
    print("Vetor não ordenado")