from collections import Counter

def calcula_estatisticas(lista):

    listaDeValores = lista

    # Calculando a média
    media = sum(listaDeValores) / len(listaDeValores)

    # Calculando a mediana
    listaEmOrdem = sorted(listaDeValores)
    casaDaMediana = len(listaDeValores) / 2
    if len(listaDeValores) % 2 != 0:
        mediana = listaEmOrdem[int(casaDaMediana)]
    else:
        mediana = (listaEmOrdem[int(casaDaMediana) - 1] + listaEmOrdem[int(casaDaMediana)]) / 2

    # Calculando a moda
    contagem = Counter(listaDeValores)
    moda = contagem.most_common(1)[0][0]
    if contagem[moda] == 1:
        moda = 'Não há moda'

    return media, mediana, moda