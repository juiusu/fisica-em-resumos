import matplotlib.pyplot as plt

# Dados
x = [0, 2, 4, 6, 8]  # tempo
y = [0, 50, 100, 150, 200]  # distância

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
