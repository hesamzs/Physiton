import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Inputs
v0 = 20  # Initial velocity (m/s)
angle = 45  # Launch angle (degrees)
angle_rad = np.radians(angle)

# Time of flight
t_flight = (2 * v0 * np.sin(angle_rad)) / g

# Time intervals
t = np.linspace(0, t_flight, num=100)

# Calculate x, y, and z positions
x = v0 * np.cos(angle_rad) * t
y = v0 * np.sin(angle_rad) * t
z = -0.5 * g * t**2  # Downward motion

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title('3D Projectile Motion')
ax.set_xlabel('X Distance (m)')
ax.set_ylabel('Y Distance (m)')
ax.set_zlabel('Height (m)')
ax.set_xlim(0, max(x) + 1)
ax.set_ylim(0, max(y) + 1)
ax.set_zlim(min(z), 1)
plt.show()