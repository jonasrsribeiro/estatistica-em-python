from parte1.medidas_dispersao import calculo_dispersao
from parte1.medidas_estatisticas import calcula_estatisticas

fornecedorA = [103,105,108,106]
fornecedorB = [110,108,107,107]
fornecedorC = [114,114,113,116]
fornecedorD = [115,117,113,115]

somaFornecedorA = sum(fornecedorA)
somaFornecedorB = sum(fornecedorB)
somaFornecedorC = sum(fornecedorC)
somaFornecedorD = sum(fornecedorD)

mediaFornecedorA, a, b = calcula_estatisticas(fornecedorA)
mediaFornecedorB, a, b = calcula_estatisticas(fornecedorB)
mediaFornecedorC, a, b = calcula_estatisticas(fornecedorC)
mediaFornecedorD, a, b = calcula_estatisticas(fornecedorD)

termoA = (((somaFornecedorA ** 2) / 4) + ((somaFornecedorB ** 2) / 4) + 
          ((somaFornecedorC ** 2) / 4) + ((somaFornecedorD ** 2) / 4))
termoB = ((somaFornecedorA + somaFornecedorB + somaFornecedorC + somaFornecedorD) ** 2) / 16

somaDosQuadradosEntreGrupos = termoA - termoB

somaDosQuadradosDentroDosGrupos = sum((fornecedorA[i] - mediaFornecedorA) ** 2 + (fornecedorB[i] - mediaFornecedorB) ** 2 + (fornecedorC[i] - mediaFornecedorC) ** 2 + (fornecedorD[i] - mediaFornecedorD) ** 2 for i in range(len(fornecedorA)))

print('Soma dos quadrados entre grupos:', round(somaDosQuadradosEntreGrupos,2))
print('Soma dos quadrados dentro dos grupos:', round(somaDosQuadradosDentroDosGrupos,2))

grausDeLiberdadeEntreGrupos = 4 - 1
grausDeLiberdadeDentroDosGrupos = 16 - 4

print('Graus de liberdade entre grupos:', grausDeLiberdadeEntreGrupos)
print('Graus de liberdade dentro dos grupos:', grausDeLiberdadeDentroDosGrupos)

quadradosMediosEntreGrupos = somaDosQuadradosEntreGrupos / grausDeLiberdadeEntreGrupos
quadradosMediosDentroDosGrupos = somaDosQuadradosDentroDosGrupos / grausDeLiberdadeDentroDosGrupos

print('Quadrados médios entre grupos:', round(quadradosMediosEntreGrupos,2))
print('Quadrados médios dentro dos grupos:', round(quadradosMediosDentroDosGrupos,2))

estatisticaF = quadradosMediosEntreGrupos / quadradosMediosDentroDosGrupos
print('Estatística F:', round(estatisticaF,2))
""" coluna 3 x linha 12 na tabela Z """
fCritico = 3.49

if estatisticaF > fCritico:
    print('Rejeitar a hipótese nula')
else:
    print('Aceitar a hipótese nula')



