programa {
  funcao inicio() {
    inteiro N, soma = 0, i
escreva("Digite o valor de N: ")
leia(N)
para (i = 1; i <= N; i++) {
se (i % 2 != 0) {
soma = soma + i
}
}
escreva("A soma dos ímpares é: ", soma)
}
  }

