from medidas_estatisticas import calcula_estatisticas
from calculo_de_quartis import calcula_quartis
from medidas_dispersao import calculo_dispersao

listaDeValores = [60,65,66,67,68,69,69,70,71,72,77]

media, mediana, moda = calcula_estatisticas(listaDeValores)

menorValor, listaDeQuartis, maiorValor = calcula_quartis(listaDeValores)

varianciaPopulacionalAoQuadrado, varianciaAmostralAoQuadrado, desvioPadrao, dispersaoDaMedia, coeficienciaDeVariancia = calculo_dispersao(listaDeValores)

print(media, mediana, moda)

print(menorValor, listaDeQuartis, maiorValor)

for quartil in listaDeQuartis:
    primeiroQuartil = listaDeQuartis[0]
    mediana = listaDeQuartis[1]
    terceiroQuartil = listaDeQuartis[2]

coeficienteQuartilicoDeAssimetria = ((terceiroQuartil + primeiroQuartil) - (2 * mediana)) / (terceiroQuartil - primeiroQuartil)

print(round(coeficienteQuartilicoDeAssimetria, 2))

if coeficienteQuartilicoDeAssimetria > 0:
    print("Assimetria Positiva")
    if coeficienteQuartilicoDeAssimetria > 1:
        print("Assimetria Forte")
    elif coeficienteQuartilicoDeAssimetria < 1 and coeficienteQuartilicoDeAssimetria > 0.15:
        print("Assimetria Moderada")
    else:
        print("Assimetria Fraca")
elif coeficienteQuartilicoDeAssimetria < 0:
    print("Assimetria Negativa")
else:
    print("Assimetria Simétrica")


if moda == 1:
    coeficienteDePearson = media - moda / desvioPadrao
else:
    coeficienteDePearson =  3 * (media - mediana) / desvioPadrao
    
print(round(coeficienteDePearson,2))