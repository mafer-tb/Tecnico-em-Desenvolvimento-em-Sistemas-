contador = 0

while True:
    nome = input("Digite um nome (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    contador += 1

print("Total de nomes digitados:", contador)