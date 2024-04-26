def calcula_quartis(lista):

    listaDeValores = lista

    # Colocar em ordem crescente
    listaEmOrdem = sorted(listaDeValores)

    # Número de elementos na lista ordenada
    numeroDeCasas = len(listaEmOrdem)

    # Calcular a posição da mediana
    casaDoQuartil = (numeroDeCasas + 1) / 4

    #Lista de Quartis
    listaDeQuartis = []

    #Menor valor e maior valor
    menorValor = listaEmOrdem[0]
    maiorValor = listaEmOrdem[-1]

    for quartil in range(1,4):
        numeroReal = quartil * casaDoQuartil
        arredondamento = int(numeroReal)
        valorMaior = (numeroReal - arredondamento)
        valorMenor = (1 - valorMaior)
        valorDoQuartil = ((listaEmOrdem[arredondamento-1] * valorMenor) + (listaEmOrdem[arredondamento] * valorMaior))
        listaDeQuartis.append(valorDoQuartil)

    return menorValor, listaDeQuartis, maiorValor