vetor = []

for i in range(10):
    vetor.append(int(input("Número i: ")))

menor = vetor[0]
posicao = 0

for i in range(1, 10):
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i

print("Menor valor:", menor)
print("Posição:", posicao)