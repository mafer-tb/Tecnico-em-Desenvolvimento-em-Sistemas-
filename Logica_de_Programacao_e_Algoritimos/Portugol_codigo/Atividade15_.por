programa {
  funcao inicio() {
    inteiro idade = 0
		inteiro somaIdades = 0
		inteiro contador = 0
		real media

    enquanto (verdadeiro)
		{
			escreva("Digite uma idade (ou um número negativo para sair): ")
			leia(idade)

			se (idade < 0)
			{
				pare 
			}
      senao
			{
				somaIdades = somaIdades + idade
				contador = contador + 1
			}
		}

		se (contador > 0)
		{
			media = somaIdades / contador
			escreva("\nTotal de idades válidas: ", contador)
			escreva("\nMédia das idades: ", media, "\n")
		}
		senao
		{
			escreva("\nNenhuma idade válida foi digitada.\n")
		}
	}
}
  
  
