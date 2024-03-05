import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo (substitua isso pelos seus próprios dados)
dados = [9, 12, 10, 45, 13]
etapas = ['Pré-usinagem', 'Trat. térmico', 'Fundição', 'Usinagem', 'Trat. Superficial']

# Criar um DataFrame pandas
tabela = pd.DataFrame({'Etapa': etapas, 'Quantidade': dados})

# Calcular a frequência relativa
total = tabela['Quantidade'].sum()
tabela['Frequência Relativa'] = tabela['Quantidade'] / total

# Calcular a frequência relativa acumulada
tabela['Frequência Relativa Acumulada'] = tabela['Frequência Relativa'].cumsum()

# Formatando a porcentagem
tabela['Frequência Relativa'] = tabela['Frequência Relativa'].map(lambda x: "{:.1%}".format(x))
tabela['Frequência Relativa Acumulada'] = tabela['Frequência Relativa Acumulada'].map(lambda x: "{:.1%}".format(x))

# Exibir a tabela
print(tabela.to_string(index=False))

total = tabela['Quantidade'].sum()
tabela['Frequência Relativa'] = tabela['Quantidade'] / total * 100  # Multiplica por 100 para obter a porcentagem

# Plotar um gráfico de pizza
cores = plt.cm.tab20.colors  # Cores padrão do Matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
patches, texts, _ = ax.pie(tabela['Frequência Relativa'], labels=tabela['Etapa'], autopct='%1.1f%%', startangle=140, colors=cores)
plt.axis('equal')  # Garante que o gráfico de pizza seja desenhado como um círculo.
plt.title('Frequência Relativa por Etapa')

# Definir a cor dos rótulos para corresponder às cores das fatias
for text, color in zip(texts, cores):
    text.set_color(color)

# Plotar um gráfico de barras
plt.figure(figsize=(16, 6))

# Gráfico de pizza
plt.subplot(1, 2, 1)
patches, texts, _ = plt.pie(tabela['Frequência Relativa'], labels=tabela['Etapa'], autopct='%1.1f%%', startangle=140, colors=cores)
plt.axis('equal')  # Garante que o gráfico de pizza seja desenhado como um círculo.
plt.title('Frequência Relativa por Etapa')

# Definir a cor dos rótulos para corresponder às cores das fatias
for text, color in zip(texts, cores):
    text.set_color(color)

# Gráfico de barras
plt.subplot(1, 2, 2)
barras = plt.bar(tabela['Etapa'], tabela['Frequência Relativa'], color=cores)
plt.xlabel('Etapa')
plt.ylabel('Frequência Relativa')
plt.title('Frequência Relativa por Etapa')
plt.xticks(ticks=range(len(tabela['Etapa'])), labels=tabela['Etapa'], rotation=45, ha='right')

# Definir a cor dos títulos de cada barra para corresponder às cores das barras
for barra, cor in zip(barras, cores):
    barra.set_color(cor)

plt.tight_layout()
plt.show()