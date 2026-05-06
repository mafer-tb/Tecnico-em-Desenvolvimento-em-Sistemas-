programa {
  funcao inicio() {
    inteiro lado1, lado2,lado3

    escreva("Digite o lado1: ")
    leia(lado1)

    escreva("Digite o lado2: ")
    leia(lado2)

    escreva("Digite o lado3: ")
    leia(lado3)
    
    se(lado1==lado2 e lado1==lado3 e lado2==lado3){
      escreva("Equilátero")
    }

    senao se(lado1==lado2 ou lado1==lado3 ou lado3==lado2){
      escreva("Isósceles")
    }

    senao se(lado1!=lado2 e lado2!=lado3){
      escreva("Escaleno")
    }
  }
}
