import pandas as pd
import matplotlib.pyplot as plt

meses = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

dias_com_chuva = [
    12, 11, 10, 9, 8, 6,
    4, 6, 7, 8, 10, 11
]

faturamento = [
    3574.00, 4708.00, 5332.00, 6693.00, 8843.00, 12347.00,
    15180.00, 11198.00, 9739.00, 9846.00, 6620.00, 5085.00
]

# Criando um DataFrame com os dados
df = pd.DataFrame({
    'Meses': meses,
    'Dias com Chuva': dias_com_chuva,
    'Faturamento': faturamento
})

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotando o gráfico de linhas para o faturamento
plt.plot(df['Meses'], df['Faturamento'], marker='o', color='blue', label='Faturamento')

# Criando um segundo eixo y para os dias com chuva
plt.twinx()
plt.bar(df['Meses'], df['Dias com Chuva'], color='orange', alpha=0.5, label='Dias com Chuva')

# Adicionando legendas e título
plt.xlabel('Meses')
plt.ylabel('Dias com Chuva', color='orange')
plt.ylabel('Faturamento', color='blue')
plt.title('Faturamento vs Dias com Chuva por Mês')
plt.legend(loc='upper left')

# Exibindo o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()

""" exer 2 """

meses2 = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

faturamento2 = [
    23000.00, 38000.00, 25000.00, 19000.00, 40000.00, 53000.00,
    15000.00, 36000.00, 56000.00, 50000.00, 42000.00, 30000.00
]

despesas = [
    3574.00, 4708.00, 5332.00, 6693.00, 8843.00, 12347.00,
    15180.00, 11198.00, 9739.00, 9846.00, 6620.00, 5085.00
]

qtd_funcionarios = [
    109, 108, 120, 130, 115, 280,
    110, 135, 190, 195, 180, 210
]

df2 = pd.DataFrame({
    'Meses': meses2,
    'Dias com Chuva': dias_com_chuva,
    'Faturamento': faturamento2,
    'Despesas': despesas,
    'Quantidade de Funcionários': qtd_funcionarios
})

# Configurando o tamanho do gráfico
plt.figure(figsize=(10, 6))

# Plotando o gráfico de linhas para o faturamento
plt.plot(df2['Meses'], df2['Quantidade de Funcionários'], marker='o', color='gray', label='Qtd de Funcionários')

# Criando um segundo eixo y para os dias com chuva
plt.twinx()
plt.bar(df2['Meses'], df2['Faturamento'], color='blue', alpha=0.5, label='Faturamento')
plt.bar(df2['Meses'], df2['Despesas'], color='orange', alpha=0.5, label='Despesas')

# Adicionando legendas e título
plt.xlabel('Meses')
plt.ylabel('Despesas', color='orange')
plt.ylabel('Faturamento', color='blue')
plt.title('Faturamento vs Dias com Chuva por Mês')
plt.legend(loc='upper left')

# Exibindo o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()