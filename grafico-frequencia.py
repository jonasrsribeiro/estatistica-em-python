import pandas as pd
import matplotlib.pyplot as plt

dados = [8, 30, 30, 50, 86, 94, 102, 110, 169, 170, 176, 236, 240, 241, 242, 255, 262, 276, 279, 282]

intervalo = 6

valorMinimo = min(dados)

valorMaximo = max(dados)

frequenciaIntervalo = round((valorMaximo - valorMinimo) / intervalo)

intervaloRange = []

intervaloSoma = valorMinimo

intervaloTabela = []

intervaloMin = []

listaFrequenciaAbsoluta = []

listaFrequenciaRelativa = []

for i in range(intervalo):
    intervaloTabela.append(i)
    intervaloSoma = intervaloSoma + frequenciaIntervalo
    valorMinimoTabela = intervaloSoma - frequenciaIntervalo
    intervaloMin.append(valorMinimoTabela)
    intervaloRange.append(intervaloSoma)

    contadorDeFrequenciaAbsoluta = 0
    for valor in dados:
        if valor >= valorMinimoTabela and valor < intervaloSoma:
            contadorDeFrequenciaAbsoluta = contadorDeFrequenciaAbsoluta + 1

    listaFrequenciaAbsoluta.append(contadorDeFrequenciaAbsoluta)

for frequencia in listaFrequenciaAbsoluta:
    frequenciaRelativa = (frequencia / sum(listaFrequenciaAbsoluta)) * 100
    listaFrequenciaRelativa.append(frequenciaRelativa)

tabela = pd.DataFrame({'Intervalo': intervaloTabela, 'Inicio': intervaloMin, 'Fim': intervaloRange, 'Freq. Absoluta': listaFrequenciaAbsoluta, 'Freq. Relativa': listaFrequenciaRelativa})

print(tabela.to_string(index=False))

# Criando o histograma
plt.bar(intervaloTabela, listaFrequenciaAbsoluta, width=1.0, edgecolor='black')
plt.xlabel('Intervalo')
plt.ylabel('Frequência Absoluta')
plt.title('Histograma dos Dados')
plt.xticks(range(len(intervaloMin)), [f'{min_value}-{max_value}' for min_value, max_value in zip(intervaloMin, intervaloRange)], rotation=45)
plt.show()