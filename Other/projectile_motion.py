import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Inputs
v0 = 20  # Initial velocity (m/s)
angle = 45  # Launch angle (degrees)

# Convert angle to radians
theta = np.radians(angle)

# Time of flight
t_flight = (2 * v0 * np.sin(theta)) / g

# Time intervals
t = np.linspace(0, t_flight, num=100)

# Calculate x and y positions
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Projectile Motion')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid()
plt.xlim(0, max(x))
plt.ylim(0, max(y) + 1)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()