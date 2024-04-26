from math import sqrt

def calculo_dispersao(lista):
    dados = lista
    quantidadeDeValores = len(dados)
    somaDosDados = sum(dados)

    mediaDosValores = somaDosDados / quantidadeDeValores

    somaDosQuadradosDosValores = sum([x**2 for x in dados])

    calculoPrincipal = somaDosQuadradosDosValores - ((1 / quantidadeDeValores) * (somaDosDados ** 2))

    varianciaPopulacionalAoQuadrado = calculoPrincipal / quantidadeDeValores

    varianciaAmostralAoQuadrado = calculoPrincipal / (quantidadeDeValores - 1)

    desvioPadrao = sqrt(varianciaAmostralAoQuadrado)

    dispersaoDaMedia = str(round(mediaDosValores + desvioPadrao, 2)) + " reais | " + str(round(mediaDosValores - desvioPadrao, 2)) + " reais"

    coeficienciaDeVariancia = (desvioPadrao / mediaDosValores) * 100

    return varianciaPopulacionalAoQuadrado, varianciaAmostralAoQuadrado, desvioPadrao, dispersaoDaMedia, coeficienciaDeVariancia



