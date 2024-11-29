import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 10  # Spring constant (N/m)
m = 1   # Mass (kg)
A = 1   # Amplitude (m)
omega = np.sqrt(k/m)  # Angular frequency (rad/s)

# Time array
t = np.linspace(0, 10, 1000)

# Displacement as a function of time
x = A * np.cos(omega * t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t, x)
plt.title('Simple Harmonic Motion')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.show()