programa {
  funcao inicio() {
    cadeia nome
		real nota1, nota2, media

   escreva("Digite o nome do aluno: ")
		leia(nome)

		escreva("Digite a primeira nota: ")
		leia(nota1)

		escreva("Digite a segunda nota: ")
		leia(nota2)

    media = (nota1 + nota2) / 2
    escreva("\nAluno: ", nome, "\nMédia: ", media, "\n")

    se (media >= 7.0) {
			escreva("Situação: APROVADO")
		}
		senao se (media >= 5.0 e media < 7.0) {
			escreva("Situação: RECUPERAÇÃO")
		}
		senao {
			escreva("Situação: REPROVADO")
		}

  }  
}
