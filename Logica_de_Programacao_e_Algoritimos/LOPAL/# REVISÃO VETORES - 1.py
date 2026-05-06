# REVISÃO VETORES - 1
# SOLICITAR AO USUARIO A QUANTIDADE DE NUMEROS
# PREENCHER O VETOR
# PREENCHER O VETOR E CALCULAR A SOMA DOS NUMEROS 
# EXIBIR A SOMA 
#-----------------------------------------------------------------

# PASSO 1) CRIAR AS VARIAVEIS
qtd = int(input("Digite a quantidade de números:"))
vetor = []
soma = 0 

# PASSO 2) PREENCHER O VETOR
for i in range(qtd):
    vetor.append(int(input("Digite um número")))

# PASSO 3) PERCORRER O VETOR 
for num in vetor:
    soma = soma + num

print("A soma é:", soma)