import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define the potential energy function (e.g., harmonic oscillator)
Z = 0.5 * (X**2 + Y**2)  # U = 1/2 * k * r^2

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Potential Energy Surface')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Potential Energy (J)')
plt.show()