import matplotlib.pyplot as plt

# Dados
x = [0, 1.0, 2.0, 6.0, 10.0]  # Volume
y = [0, 50.0, 100.0, 300.0, 500.0]  # Massa

# Criar o gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Linha com pontos
plt.xlabel('Tempo (h)')
plt.ylabel('Distância (km)')
plt.title('Relação entre distância percorrida e tempo para uma velocidade constante')
plt.grid(True)

# Salvar o gráfico como PNG
plt.savefig('grafico2.png')

# Exibir o gráfico (opcional)
plt.show()
