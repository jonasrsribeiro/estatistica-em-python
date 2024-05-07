import pandas as pd
import matplotlib.pyplot as plt

""" Atividade 2 """

dados = [
    'F', 'F', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'F',
    'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'M',
    'M', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'F',
    'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M', 'M',
    'F', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'M',
    'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F',
    'M', 'F', 'M', 'F', 'F', 'F', 'F', 'M', 'F', 'M',
    'M', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'F',
    'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'F',
    'F', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'F', 'F',
    'F', 'F', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'F',
    'F', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F',
    'M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'M', 'F',
    'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'F',
    'F', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'M', 'M',
    'M', 'M', 'M', 'M', 'F', 'F', 'F', 'M', 'F', 'M',
    'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M',
    'M', 'M', 'M', 'F', 'F', 'M', 'F'
]

# Criar listas para cada gênero
feminino = [x for x in dados if x == 'F']
masculino = [x for x in dados if x == 'M']
nao_aplicavel = [x for x in dados if x == 'N/A']

intervalo = 6

valorMinimoFeminino = min(feminino)
valorMaximoFeminino = max(feminino)

valorMinimoMasculino = min(masculino)
valorMaximoMasculino = max(masculino)

valorMinimoNA = min(nao_aplicavel)
valorMaximoNA = max(nao_aplicavel)

frequenciaIntervaloFeminino = round((valorMaximoFeminino - valorMinimoFeminino) / intervalo)
frequenciaIntervaloMasculino = round((valorMaximoMasculino - valorMinimoMasculino) / intervalo)
frequenciaIntervaloNA = round((valorMaximoNA - valorMinimoNA) / intervalo)

intervaloRangeFeminino = []
intervaloRangeMasculino = []
intervaloRangeNA = []

intervaloSomaFeminino = valorMinimoFeminino
intervaloSomaMasculino = valorMinimoMasculino
intervaloSomaNA = valorMinimoNA

intervaloTabelaFeminino = []
intervaloTabelaMasculino = []
intervaloTabelaNA = []

intervaloMinFeminino = []
intervaloMinMasculino = []
intervaloMinNA = []

listaFrequenciaAbsolutaFeminino = []
listaFrequenciaAbsolutaMasculino = []
listaFrequenciaAbsolutaNA = []

listaFrequenciaRelativaFeminino = []
listaFrequenciaRelativaMasculino = []
listaFrequenciaRelativaNA = []

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