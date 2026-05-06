programa {
  funcao inicio() {
    inteiro numero

    escreva("DIGITE UM NÚMERO: ")
    leia(numero)

    se (numero % 3 == 0 e numero % 5 == 0)
		{
			escreva("O número ", numero, " é múltiplo de ambos (3 e 5).")
		}
		senao se (numero % 3 == 0)
		{
			escreva("O número ", numero, " é múltiplo de 3.")
		}
		senao se (numero % 5 == 0)
		{
			escreva("O número ", numero, " é múltiplo de 5.")
		}
		senao
		{
			escreva("O número ", numero, " não é múltiplo de 3 nem de 5.")
		}
  }
}
