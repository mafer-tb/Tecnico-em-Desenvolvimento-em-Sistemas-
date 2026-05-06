programa {
  funcao inicio() {
    inteiro numero

    escreva("Digite um número: ")
    leia(numero)

    se(numero==1){
      escreva("Domingo")
    }

     senao se (numero==2){
      escreva("Segunda-feira")
    }

    senao se (numero==3){
      escreva("Terça-feira")
    }

    senao se (numero==4){
      escreva("Quarta-feira")
    }

    senao se (numero==5){
      escreva("Quinta-feira")
    }

    senao se (numero==6){
      escreva("Sexta-feira")
    }
    senao se (numero==7){
      escreva("Sábado")
    }
    senao se (numero>=8){
      escreva("Dia inválido")
    }
  }
}
