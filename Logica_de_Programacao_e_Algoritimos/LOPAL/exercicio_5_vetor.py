vetor = []
numero = 0

for i in range(8):
    num = int (input("Digite o número:"))
    vetor.append(num)

numero = int(input("Digite um número para procurar no vetor:"))

for i in range(8):
    if(vetor[i]== numero):
        print("Encontrou!")
