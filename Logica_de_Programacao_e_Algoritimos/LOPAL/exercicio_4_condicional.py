ladoA = int(input("Digite o lado A:"))
ladoB = int(input("Digite o lado B:"))
ladoC = int(input("Digite o lado C:"))

if((ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA):
    if(ladoA==ladoB and ladoB ==ladoC and ladoA== ladoC):
        print("Equilátero")
    elif(ladoA!=ladoB and ladoB!=ladoC and ladoA!=ladoC):
      print("Escaleno")
    else:
      print("Isósceles")
else:
   print("O triângulo não existe!!")