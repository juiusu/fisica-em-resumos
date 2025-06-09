import numpy as np
import matplotlib.pyplot as plt

# Valores de tensão (Volts)
tensao = np.linspace(0, 20, 100)
# Corrente para resistência constante R = 4 Ohms (Lei de Ohm: I = V / R)
resistencia = 2  # Ohms
corrente = tensao / resistencia

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(corrente, tensao)
plt.ylabel('Tensão (V)')
plt.xlabel('Corrente (A)')
plt.title('Gráfico de Tensão eletrica por corrente elétrica')
plt.grid(True)


# Salvar o gráfico como PNG
plt.savefig('grafico-resistencia.png')

# exibir o gráfico
plt.show()
