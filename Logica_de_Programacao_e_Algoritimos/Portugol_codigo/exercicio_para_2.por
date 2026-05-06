programa {
  funcao inicio() {
    inteiro inicio, fim, soma=0
    escreva("Digite o numero de início: ")
    leia(inicio)

    escreva("Digite o numero final: ")
    leia(fim)

    para(inteiro i=inicio;i<=fim;i++){
      se(i%2 == 0){
        soma = soma + i
      }
    }
    escreva("A soma é: ",soma)
  }
}
