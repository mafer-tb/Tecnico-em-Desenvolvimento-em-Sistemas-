vetor = []

for i in range(8):
    vetor.append(int(input("Número i: ")))

for i in range(8):
    for j in range(7):
        if vetor[j] < vetor[j + 1]:
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

print("Ordem decrescente:", vetor)