idades = []

for i in range(6):
    idade = int(input("digite sua idade:"))
    idades.append(idade)

    for idade in idades:
        if(idade>=18):
            print("Maior de idade!")
        else:
            print("Menor de idade!")