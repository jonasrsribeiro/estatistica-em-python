import pandas as pd
import matplotlib.pyplot as plt

numeroDosPedidos = [1002369, 1002145, 1002036,1002248,1002965,1004789,1005514,1003025,1002456,1002188,1002365,1002244,1002121,1002033]
diasParaEntrega = [4,24,13,6,19,5,14,9,5,17,14,2,13,5]

# Calcular o número de bins usando a regra de Sturges
def regraDeSturges(listaDeDados):
    n = len(listaDeDados)
    k = int(1 + 3.3 * (n ** (1/3)))  # Fórmula de Sturges
    return k

k = regraDeSturges(diasParaEntrega)

# Plotar histograma
plt.hist(diasParaEntrega, bins=k, edgecolor='black')
plt.title('Histograma de Dias para Entrega')
plt.xlabel('Dias para Entrega')
plt.ylabel('Frequência')
plt.grid(False)
plt.show()

""" EXER 2 """

numeroDoTeste = ['#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13','#14','#15']

horasParaFalha = [20,35,40,55,80,60,61,85,80,64,80,75,23,70,45]

k2 = regraDeSturges(horasParaFalha)

# Plotar histograma
plt.hist(horasParaFalha, bins=k2, edgecolor='black')
plt.title('Histograma de Dias para Entrega')
plt.xlabel('Dias para Entrega')
plt.ylabel('Frequência')
plt.grid(False)
plt.show()

""" EXER 3 """

