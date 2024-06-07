from parte1.medidas_estatisticas import calcula_estatisticas
from parte1.calculo_de_quartis import calcula_quartis
from parte1.medidas_dispersao import calculo_dispersao
import matplotlib.pyplot as plt
import numpy as np

listaA = [9.5, 10.0, 11.0, 9.5, 10.5, 10.0, 10.0, 9.0, 10.0, 10.5, 10.0, 8.5, 10.5, 9.5, 9.0, 9.5, 10.0, 8.5, 10.0, 9.5, 10.0, 9.5, 9.5, 10.5, 9.0, 9.5, 11.5, 11.0, 9.0, 8.5, 10.0, 8.5, 10.0, 9.0, 10.0, 8.5, 9.0, 8.5, 11.0, 11.0, 10.5, 8.5, 7.5, 9.5, 10.0, 10.0, 9.5, 9.5, 10.0, 10.0, 9.5, 8.5, 9.0, 10.0, 10.5, 10.5, 10.5, 9.5, 10.0, 9.5, 10.0, 9.5, 9.5, 9.5, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 9.5, 9.5, 10.5, 8.5, 10.0, 9.0, 9.5, 8.5, 9.0, 10.0, 9.0, 10.5, 9.5, 10.5, 10.0, 9.5, 9.5, 10.0, 9.0, 9.5, 10.0, 11.0, 10.5, 9.0, 10.0, 9.0, 11.0, 9.0, 10.5, 9.5]

listaB = [8.5, 9.5, 10.5, 10.5, 10.0, 10.5, 12.0, 9.5, 9.0, 10.5, 8.5, 11.0, 10.0, 10.5, 11.0, 10.5, 9.5, 10.5, 10.0, 10.0, 10.0, 9.5, 10.0, 9.5, 10.0, 10.5, 10.0, 10.0, 11.0, 9.0, 10.0, 9.5, 10.0, 9.0, 8.5, 10.5, 11.0, 9.0, 10.5, 9.5, 10.0, 10.0, 10.5, 9.0, 8.5, 10.5, 10.5, 8.0, 10.0, 9.0, 9.0, 10.0, 9.5, 9.5, 9.5, 11.0, 10.0, 9.0, 9.5, 10.5, 12.5, 10.0, 9.5, 10.0, 10.5, 9.5, 9.5, 9.0, 10.0, 10.5, 10.0, 10.0, 10.5, 9.0, 9.5, 11.5, 8.5, 9.5, 9.5, 9.5, 9.5, 10.0, 10.0, 8.0, 9.5, 10.0, 9.5, 10.0, 10.0, 10.5, 11.0, 9.5, 10.0, 10.0, 10.0, 9.0, 11.5, 10.5, 9.0, 10.0]

listaC = [9.5, 8.5, 10.5, 10.0, 10.5, 10.5, 10.0, 10.0, 10.5, 10.5, 9.0, 9.5, 10.0, 9.0, 10.5, 9.5, 9.0, 9.0, 9.0, 11.0, 7.5, 8.5, 10.0, 9.0, 10.0, 8.5, 8.5, 10.0, 8.0, 10.0, 9.5, 9.0, 8.5, 10.5, 10.0, 10.5, 9.5, 10.5, 10.0, 10.5, 9.5, 10.0, 8.0, 8.5, 10.5, 9.0, 9.0, 9.5, 10.0, 10.0, 10.0, 9.5, 11.0, 10.0, 9.5, 10.5, 9.5, 8.0, 10.0, 8.5, 8.5, 10.0, 10.0, 9.5, 9.5, 8.0, 8.0, 9.0, 9.5, 10.0, 8.5, 10.0, 10.5, 8.0, 10.0, 9.0, 9.5, 10.5, 10.0, 9.5, 10.0, 10.0, 10.5, 10.0, 9.0, 9.5, 10.0, 9.5, 9.0, 11.5, 11.5, 11.5, 11.0, 11.0, 9.5, 11.5, 11.5, 9.5, 12.0, 11.5]

mediaA, medianaA, modaA = calcula_estatisticas(listaA)
mediaB, medianaB, modaB = calcula_estatisticas(listaB)
mediaC, medianaC, modaC = calcula_estatisticas(listaC)

if mediaA != medianaA != modaA: 
    print('NÃO PODE USAR DISTRIBUICAO NORMAL')
if mediaB != medianaB != modaB: 
    print('NÃO PODE USAR DISTRIBUICAO NORMAL')
if mediaB != medianaB != modaB: 
    print('NÃO PODE USAR DISTRIBUICAO NORMAL') 

varianciaPopulacionalAoQuadradoA, varianciaAmostralAoQuadradoA, desvioPadraoA, dispersaoDaMediaA, coeficienciaDeVarianciaA = calculo_dispersao(listaA)

varianciaPopulacionalAoQuadradoA, varianciaAmostralAoQuadradoA, desvioPadraoB, dispersaoDaMediaA, coeficienciaDeVarianciaA = calculo_dispersao(listaB)

varianciaPopulacionalAoQuadradoA, varianciaAmostralAoQuadradoA, desvioPadraoC, dispersaoDaMediaA, coeficienciaDeVarianciaA = calculo_dispersao(listaC)

# Criar um array de valores x para plotar
valores_x = np.linspace(min(min(listaA), min(listaB), min(listaC)), max(max(listaA), max(listaB), max(listaC)), 100)

# Função para calcular a densidade de probabilidade normal
def calc_densidade_probabilidade_normal(x, media, desvio_padrao):
    return (1.0 / (desvio_padrao * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desvio_padrao) ** 2)

# Criar a distribuição normal para cada lista
distribuicaoNormalA = calc_densidade_probabilidade_normal(valores_x, mediaA, desvioPadraoA)
distribuicaoNormalB = calc_densidade_probabilidade_normal(valores_x, mediaB, desvioPadraoB)
distribuicaoNormalC = calc_densidade_probabilidade_normal(valores_x, mediaC, desvioPadraoC)

# Plotar as distribuições
plt.plot(valores_x, distribuicaoNormalA, label='Lista A')
plt.plot(valores_x, distribuicaoNormalB, label='Lista B')
plt.plot(valores_x, distribuicaoNormalC, label='Lista C')

plt.legend()
plt.show()