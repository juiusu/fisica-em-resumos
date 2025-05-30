import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do movimento
v0 = 5  # velocidade inicial horizontal (m/s)
g = 9.8  # gravidade (m/s^2)
h0 = 5   # altura inicial (m)
fps = 30
duracao = 2  # segundos
n_frames = fps * duracao

# Tempo total até a bolinha atingir o chão
t_total = np.sqrt(2 * h0 / g)
t_vals = np.linspace(0, min(duracao, t_total), n_frames)

# Posições da bolinha
x_vals = v0 * t_vals
y_vals = h0 - 0.5 * g * t_vals**2

# Criação da figura
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, max(x_vals) + 1)
ax.set_ylim(0, h0 + 1)
ax.set_xlabel("Posição Horizontal (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Lançamento Horizontal com Sombras das Componentes")

# Elementos gráficos
bola, = ax.plot([], [], 'ro', markersize=10)
sombra_x, = ax.plot([], [], 'ko', alpha=0.3, markersize=10)
sombra_y, = ax.plot([], [], 'ko', alpha=0.3, markersize=10)
trajetoria, = ax.plot([], [], 'r--', linewidth=1, alpha=0.5)

x_traj, y_traj = [], []

def init():
    bola.set_data([], [])
    sombra_x.set_data([], [])
    sombra_y.set_data([], [])
    trajetoria.set_data([], [])
    return bola, sombra_x, sombra_y, trajetoria

def animate(i):
    x = x_vals[i]
    y = y_vals[i]
    bola.set_data(x, y)
    sombra_x.set_data(x, 0)  # sombra no chão
    sombra_y.set_data(0, y)  # sombra na parede
    x_traj.append(x)
    y_traj.append(y)
    trajetoria.set_data(x_traj, y_traj)
    return bola, sombra_x, sombra_y, trajetoria

ani = animation.FuncAnimation(fig, animate, frames=n_frames,
                              init_func=init, blit=True)

# Salvar como GIF
gif_path = "./lancamento_horizontal_sombras.gif"
ani.save(gif_path, writer='pillow', fps=fps)

gif_path
