import matplotlib.pyplot as plt

# Dados
x = [0, 1.0, 2.0, 3.0, 4.0, 5.0]  # Volume
y = [0, 3.0, 6.0, 9.0, 12.0, 15.0]  # Massa

# Criar o gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Linha com pontos
plt.xlabel('Volume (mL)')
plt.ylabel('Massa (g)')
plt.title('Relação entre Volume e Massa')
plt.grid(True)

# Salvar o gráfico como PNG
plt.savefig('grafico1.png')

# Exibir o gráfico (opcional)
plt.show()
