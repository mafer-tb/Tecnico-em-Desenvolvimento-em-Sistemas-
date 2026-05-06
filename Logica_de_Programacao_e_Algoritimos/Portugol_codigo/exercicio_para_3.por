programa {
  funcao inicio() {
    inteiro numero, fatoral=1
    
    escreva("Digite um número: ")
    leia(numero)

    para(inteiro i=numero;i>=1;i--){
      fatoral= fatoral * i 
    }
    escreva("O fatoral de ",numero," é ", fatoral)

  }
}
