nomes = []

for i in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome) 


print("\nNomes na ordem inversa:")
for nome in nomes[::-1]:
    print(nome)
