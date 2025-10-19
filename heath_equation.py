import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("Solver da equação de calor 2D")

plate_length = 30
max_iter_time = 50  

alpha = 2
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Inicializa a solução: a grade de u(k, i, j)
u = np.empty((max_iter_time, plate_length, plate_length))

# Condição inicial em todos os lugares dentro da grade
u_initial = 0

# Condições de contorno
u_top = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Define a condição inicial
u.fill(u_initial)

# Define as condições de contorno
u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, :] = u_bottom  # Corrige a condição de contorno inferior
u[:, :, (plate_length-1):] = u_right

def calculate(u):
    for k in range(0, max_iter_time-1, 1):
        for i in range(1, plate_length-1, delta_x):
            for j in range(1, plate_length-1, delta_x):
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
    return u

def plotheatmap(u_k, k):
    plt.clf()
    plt.title(f"Temperatura em t = {k*delta_t:.3f} unidades de tempo")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.imshow(u_k, cmap='hot', interpolation='nearest', vmin=0, vmax=100)
    plt.colorbar()
    return plt

u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)

fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, interval=1, frames=max_iter_time, repeat=False)

# Salva a animação
anim.save("solucao_equacao_calor.gif", writer='pillow')

# Exibe a animação
plt.show()

print("Feito!")
