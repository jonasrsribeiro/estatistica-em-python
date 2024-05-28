import pandas as pd
import matplotlib.pyplot as plt

# Dados
investidores = ['A', 'B', 'C']
numeroDeAcoes = [96, 181, 88]
numeroDePrevidencias = [181, 3, 29]
numeroDeAlugueis = [88, 152, 142]

# Criando o DataFrame
df = pd.DataFrame({
    'Investidores': investidores,
    'Ações': numeroDeAcoes,
    'Previdências': numeroDePrevidencias,
    'Aluguéis': numeroDeAlugueis
})

# Plotando o gráfico de barras
df.plot(x='Investidores', kind='bar', stacked=False, figsize=(10, 6))
plt.grid(axis='y')
plt.title('Distribuição de Investimentos por Investidor')
plt.xlabel('Investidores')
plt.ylabel('Quantidade')
plt.legend(title='Tipo de Investimento')
plt.show()

""" EXER 2 """

gruposEtarios = ['18-25', '25-35', '35-45', '45-55', '55-65', '65+']

empregados = [60, 85, 95, 97, 97, 100]

desempregados = [40, 15, 5, 3, 3, 0]

# Criando o DataFrame
df = pd.DataFrame({
    'Grupos Etários': gruposEtarios,
    'Empregados': empregados,
    'Desempregados': desempregados
})

# Plotando o gráfico de barras
df.plot(x='Grupos Etários', kind='bar', stacked=False, figsize=(10, 6))
plt.grid(axis='y')
plt.title('Distribuição de Investimentos por Investidor')
plt.xlabel('Grupos Etários')
plt.ylabel('Porcentagem')
plt.legend(title='Empregabilidade')
plt.show()