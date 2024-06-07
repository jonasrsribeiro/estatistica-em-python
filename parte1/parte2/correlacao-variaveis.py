from parte1.medidas_dispersao import calculo_dispersao
from parte1.medidas_estatisticas import calcula_estatisticas

metragem = [65,78,120,72,98]
aluguel = [772,998,1200,800,895]

a, b, desvioPadraoMetragem, c, d = calculo_dispersao(metragem)
a, b, desvioPadraoAluguel, c, d = calculo_dispersao(aluguel)
mediaMetragem, a, b = calcula_estatisticas(metragem)
mediaAluguel,a, b = calcula_estatisticas(aluguel)

metragemSoma = sum(metragem)
aluguelSoma = sum(aluguel)

covarianciaAmostral = sum((metragem[i] - mediaMetragem) * (aluguel[i] - mediaAluguel) for i in range(len(metragem))) / (len(metragem) - 1)

print('Covariância amostral:', round(covarianciaAmostral,2))

if covarianciaAmostral > 0:
    print('Covariância positiva')
elif covarianciaAmostral < 0:
    print('Covariância negativa')
else:
    print('Covariância neutra')

correlacaoDePearsonAmostral = covarianciaAmostral / (desvioPadraoMetragem * desvioPadraoAluguel)

print('Correlação de Pearson Amostral:', round(correlacaoDePearsonAmostral,2))

if correlacaoDePearsonAmostral > 0:
    print('Correlação positiva')
    if correlacaoDePearsonAmostral > 0.8:
        print('Correlação forte')
    elif correlacaoDePearsonAmostral < 0.8 and correlacaoDePearsonAmostral > 0.5:
        print('Correlação moderada')
    else:
        print('Correlação fraca')
elif correlacaoDePearsonAmostral < 0:
    print('Correlação negativa')
    if correlacaoDePearsonAmostral < -0.8:
        print('Correlação forte')
    elif correlacaoDePearsonAmostral > -0.8 and correlacaoDePearsonAmostral < -0.5:
        print('Correlação moderada')
    else:
        print('Correlação fraca')
else:
    print('Correlação neutra')

correlacaoDePearsonPopulacional = (len(metragem) * sum(metragem[i] * aluguel[i] for i in range(len(metragem)))) - (metragemSoma * aluguelSoma) / (((len(metragem) * sum((metragem[i] ** 2) for i in range(len(metragem))) - metragemSoma ** 2) * (len(metragem) * sum((aluguel[i] ** 2) for i in range(len(aluguel))) - aluguelSoma ** 2)) ** 0.5)

print('Correlação de Pearson Populacional:', round(correlacaoDePearsonPopulacional,2))

if correlacaoDePearsonPopulacional > 0:
    print('Correlação positiva')
    if correlacaoDePearsonPopulacional > 0.3 and correlacaoDePearsonPopulacional <= 0.5:
        print('Correlação fraca')
    elif correlacaoDePearsonPopulacional > 0.5 and correlacaoDePearsonPopulacional < 1:
        print('Correlação moderada')
    else:
        print('Correlação forte')
else:
    print('Correlação negativa')
    if correlacaoDePearsonPopulacional < -0.3 and correlacaoDePearsonPopulacional >= -0.5:
        print('Correlação fraca')
    elif correlacaoDePearsonPopulacional < -0.5 and correlacaoDePearsonPopulacional > -1:
        print('Correlação moderada')
    else:
        print('Correlação forte')


coeficienteDeDeterminacao = correlacaoDePearsonAmostral ** 2 #utilizado pelo excel

print('Coeficiente de Determinação:', round(coeficienteDeDeterminacao,2))