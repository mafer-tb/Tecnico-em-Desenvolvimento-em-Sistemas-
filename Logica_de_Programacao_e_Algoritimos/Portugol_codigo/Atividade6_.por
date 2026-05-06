programa {
  funcao inicio() {
    inteiro hora

    escreva("Digite um horário (0 a 23): ")
    leia(hora)

    se (hora >= 0 e hora <= 5) {
      escreva("Madrugada")
    }
    senao se (hora >= 6 e hora <= 11) {
      escreva("Manhã")
    }
    senao se (hora >= 12 e hora <= 17) {
      escreva("Tarde")
    }
    senao se (hora >= 18 e hora <= 23) {
      escreva("Noite")
    }
    senao {
      escreva("Horário inválido! Digite um valor entre 0 e 23.")
    }
  }
}
