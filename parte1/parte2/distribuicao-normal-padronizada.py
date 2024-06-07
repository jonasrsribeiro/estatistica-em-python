import math

media = 3
desvioPadrao = 0.3

valorZMin = -4
valorZMax = 4

frequenciaNormal = []

frequencialNormalAcumulada = []

for i in range(81):
    if i == 0:
        valorAtual = valorZMin
    else:
        valorAtual = valorAtual + 0.1
    frequenciaNormal.append(round(valorAtual,2))

print(frequenciaNormal)

for i in range(81):
    calculo = 1/math.sqrt(2*math.pi) * math.exp(-0.5 * (frequenciaNormal[i] - media) / desvioPadrao)
    
    frequencialNormalAcumulada.append(round(calculo,2))

print(frequencialNormalAcumulada)



z = 3.75 - 3 / 0.3

