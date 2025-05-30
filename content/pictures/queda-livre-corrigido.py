
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do movimento
g = 9.8  # gravidade (m/s^2)
h0 = 5   # altura inicial (m)
fps = 30
duracao = 2  # segundos
n_frames = fps * duracao

# Tempo total até a bolinha atingir o chão
t_total_vert = np.sqrt(2 * h0 / g)
t_vals_vert = np.linspace(0, min(duracao, t_total_vert), n_frames)

# Posições da bolinha no movimento vertical
x_vals_vert = np.zeros_like(t_vals_vert)
y_vals_vert = h0 - 0.5 * g * t_vals_vert**2

# Criação da figura
fig2, ax2 = plt.subplots(figsize=(5, 5))
ax2.set_xlim(-1, 1)
ax2.set_ylim(0, h0 + 1)
ax2.set_xlabel("Posição Horizontal (m)")
ax2.set_ylabel("Altura (m)")
ax2.set_title("Queda Livre com Sombra Vertical")

# Elementos gráficos
bola_vert, = ax2.plot([], [], 'bo', markersize=10)
sombra_y_vert, = ax2.plot([], [], 'ko', alpha=0.3, markersize=10)
trajetoria_vert, = ax2.plot([], [], 'b--', linewidth=1, alpha=0.5)

x_traj_vert, y_traj_vert = [], []

def init_vert():
    bola_vert.set_data([], [])
    sombra_y_vert.set_data([], [])
    trajetoria_vert.set_data([], [])
    return bola_vert, sombra_y_vert, trajetoria_vert

def animate_vert(i):
    x = x_vals_vert[i]
    y = y_vals_vert[i]
    bola_vert.set_data(x, y)
    sombra_y_vert.set_data(0, y)  # sombra vertical na parede
    x_traj_vert.append(x)
    y_traj_vert.append(y)
    trajetoria_vert.set_data(x_traj_vert, y_traj_vert)
    return bola_vert, sombra_y_vert, trajetoria_vert

ani_vert = animation.FuncAnimation(fig2, animate_vert, frames=n_frames,
                                   init_func=init_vert, blit=False)

# Salvar como GIF
ani_vert.save("queda_livre_sombra.gif", writer='pillow', fps=fps)
