from vpython import *
import numpy as np

# Create the scene
scene = canvas(title='Parabolic Throw with Velocity Components', width=800, height=400)
g1 = graph(title="ball drop",xtitle="x",ytitle="y",width=400, height=250)
f1 = gcurve(color=color.blue)

# Create the floor
floor = box(pos=vector(0, -0.1, 0), size=vector(5, 0.1, 0.1), color=color.gray(0.5))

# Constants
g = 9.81          # Acceleration due to gravity (m/s^2)
initial_height = 1.0  # Initial height of the mass (m)
initial_velocity = 10.0  # Initial velocity (m/s)
launch_angle = 20  # Launch angle (degrees)

# Calculate components of initial velocity
theta = np.radians(launch_angle)  # Convert angle to radians
initial_velocity_x = initial_velocity * np.cos(theta)  # Horizontal component
initial_velocity_y = initial_velocity * np.sin(theta)  # Vertical component

# Create the mass
mass = sphere(pos=vector(0, initial_height, 0), radius=0.1, color=color.red)

# Create a label for energy
energy_label = label(pos=vector(0, 1.5, 0), text='Kinetic Energy: 0 J', height=16, box=False)

# Time variables
t = 0
dt = 0.01  # Time step

# Simulation loop
while mass.pos.y > -0.1:  # Continue until the mass hits the floor
    rate(15)  # Control the speed of the simulation

    # Update the vertical position of the mass
    mass.pos.y += initial_velocity_y * dt - 0.5 * g * t**2  # Vertical motion equation

    # Update the horizontal position of the mass
    mass.pos.x += initial_velocity_x * dt  # Horizontal motion

    # Update time
    t += dt

    # Update the energy label
    kinetic_energy = 0.5 * (initial_velocity_x**2 + (initial_velocity_y - g * t)**2)
    f1.plot(mass.pos.x,mass.pos.y)
    energy_label.text = f'Kinetic Energy: {kinetic_energy:.2f} J'

while True:pass