numeroInicio = int(input("digite o número inicial:"))
numeroFinal = int(input("Digite o número final:"))
soma = 0
for i in range(numeroInicio,numeroFinal+1):
    if(i%2==0):
      soma = soma + i
print("A soma dos números é:",soma)