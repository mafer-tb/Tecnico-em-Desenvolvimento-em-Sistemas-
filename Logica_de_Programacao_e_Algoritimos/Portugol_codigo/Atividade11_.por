programa {
  funcao inicio() {
    inteiro contador, numero
		inteiro soma = 0

    para (contador = 1; contador <= 10; contador++)
		{
			escreva("Digite o ", contador, "º número: ")
			leia(numero)
			
			soma = soma + numero 
      escreva("\nA soma total dos 10 números é: ", soma, "\n")
		}
  }
}
