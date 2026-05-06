#Criando uma variável número 
numero = 10

#Criando uma variável textual 
nome = "gabriel"

#usuario inserir um texto 
nome_completo = input("Digite seu nome:")

#usuario inserir um numero inteiro
idade = int(input("Digite sua idade:"))

#usuario inserir um numero decimal
salario = float(input("Digite seu salário:"))

#estruturas condicionais - if 
if (salario >1500 and idade >18):
    print ("Você pode tirar carta!")
elif(salario<1500 or idade <18):
    print("Você não pode tirar carta!")
else:
    print("Inválido")

#estruturas condicionais exemplo 2 
turno = input("Digite seu turno (M/V/N):")

if(turno == "M"):#utilize dois iguais para comparar 
    print("Bom dia!")
elif(turno == "V"):
    print("Boa tarde!")
elif(turno == "N"):
    print("Boa noite!")
else:
    print("Inválido")

#estrutura de repetição
#0 -> 10

for i in range(11): #sempre coloque +1
    print(i)

#1 -> 15 
for i in range (1,16): #vai do 1 até 15
    print(i)

#5- > 65(aumentando de 5 em 5 )
for i in range (5,66,+5):
    print(i)

#122 - > (tirando de 2 em 2)
for  i in range(122,-1,-2):
    print(i)

#usuario escolhe o inicio e fim
#inicio - > fim 

inicio = int(input("INICIO:"))
fim = int(input("FIM"))
  
for i in range(inicio,fim +1):
    print(i)

#vetores
nomes =[]

#sempre utilizar para preencher o vetor 
for i in range(5):
    nomes.append(input("Digite um nome:"))

#sempre utilizar para exibir o vetor 
for nome in nomes:
    print(nome)