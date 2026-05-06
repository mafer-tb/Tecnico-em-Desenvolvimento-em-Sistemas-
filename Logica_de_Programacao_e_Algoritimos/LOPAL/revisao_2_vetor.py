#solicita um texto para o usuario 
texto = input("Digite um texto qualquer:")

# exibir letra por letra do texto 
# para cada letra no texto 
for letra in texto:
    print(letra)

# contar quantidade de caracteres != ''
qtd_caracteres = 0 

for letra in texto:
    if (letra != " "):
        qtd_caracteres+=1
print("A quantidade de caracteres é:", qtd_caracteres)

# contar as quantidades de vogais 
vogais = "aeiouAEIOUáàãâÁÀÃÂéèêÉÈÊíìîÍÌÎóòôõÓÕÔÒûùúÚÙÛ"
qtd_caracteres=0 

for vogal in vogais:
    for letra in texto:
        if(letra == vogal):
            qtd_caracteres+=1
print("A quantidade de vogais é: ", qtd_caracteres)

#palindromo 
texto_invertido = "" 

for i in range (len(texto)-1,-1,-1):
    texto_invertido = texto_invertido + texto[i]

if(texto == texto_invertido):
    print("É palindromo!")
else:
    print("Não é palindromo")
