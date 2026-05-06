programa {
  funcao inicio() {
    real basemaior, basemenor, altura, area

    escreva("Base Maior:")
    leia(basemaior)

    escreva("Base Menor:")
    leia(basemenor)
    
    escreva("Altura:")
    leia(altura)

    area=((basemaior+basemenor)*altura)/2
    escreva("Área do Trapézio:",area)
  }
}
