from parte1.medidas_estatisticas import calcula_estatisticas
from parte1.medidas_dispersao import calculo_dispersao

listaA = [9.5, 10.0, 11.0, 9.5, 10.5, 10.0, 10.0, 9.0, 10.0, 10.5, 10.0, 8.5, 10.5, 9.5, 9.0, 9.5, 10.0, 8.5, 10.0, 9.5, 10.0, 9.5, 9.5, 10.5, 9.0, 9.5, 11.5, 11.0, 9.0, 8.5, 10.0, 8.5, 10.0, 9.0, 10.0, 8.5, 9.0, 8.5, 11.0, 11.0, 10.5, 8.5, 7.5, 9.5, 10.0, 10.0, 9.5, 9.5, 10.0, 10.0, 9.5, 8.5, 9.0, 10.0, 10.5, 10.5, 10.5, 9.5, 10.0, 9.5, 10.0, 9.5, 9.5, 9.5, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 9.5, 9.5, 10.5, 8.5, 10.0, 9.0, 9.5, 8.5, 9.0, 10.0, 9.0, 10.5, 9.5, 10.5, 10.0, 9.5, 9.5, 10.0, 9.0, 9.5, 10.0, 11.0, 10.5, 9.0, 10.0, 9.0, 11.0, 9.0, 10.5, 9.5]

mediaA, medianaA, modaA = calcula_estatisticas(listaA)
varianciaPopulacionalAoQuadradoA, varianciaAmostralAoQuadradoA, desvioPadraoA, dispersaoDaMediaA, coeficienciaDeVarianciaA = calculo_dispersao(listaA)

listaAOrdenada = listaA.sort()

enumeracao = []

for i in range(len(listaAOrdenada)): 
    enumeracao.append(i+1)

probabilidadeValorSerMenor = []

for i in range(len(listaAOrdenada)):
    probabilidadeValorSerMenor.append(enumeracao[i]/(len(listaAOrdenada)+1))

valorZEstimado = []

for i in range(len(listaAOrdenada)):
    valorZEstimado.append((listaAOrdenada[i] - mediaA) / desvioPadraoA)

"""  """