import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para criar a superfície do espaço-tempo
def space_time_fabric(x, y, mass_position, mass_strength):
    """ Cria uma distorção no tecido do espaço-tempo baseada na posição e força da massa. """
    # Cálculo da força de gravidade em função da distância da massa
    distance = np.sqrt((x - mass_position[0])**2 + (y - mass_position[1])**2)
    z = -mass_strength / distance  # Distorção negativa para simular atração gravitacional
    z[distance == 0] = -mass_strength  # Previne divisão por zero
    return z

# Criar uma grade de valores x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Definir posição e força da massa central
mass_position = (0, 0)  # Posição da massa no centro
mass_strength = 1  # Força da massa (quanto mais forte, mais profundo o poço)

# Calcular a superfície do espaço-tempo
z = space_time_fabric(x, y, mass_position, mass_strength)

# Plotar a superfície do espaço-tempo
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Adicionar detalhes ao gráfico
ax.set_title('Tecido do Espaço-Tempo Distorcido por uma Massa')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Distorção do Espaço-Tempo')
ax.view_init(elev=30, azim=30)  # Alterar a vista para melhor visualização

plt.show()
