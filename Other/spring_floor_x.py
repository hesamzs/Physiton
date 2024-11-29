from vpython import *
import numpy as np

# Create the scene
scene = canvas(title='Horizontal Damped Spring-Mass System with Floor', width=800, height=400)
g1 = graph(title="Mass Position", xtitle="Time (s)", ytitle="Position (m)", width=400, height=250)
f1 = gcurve(color=color.blue)

# Constants
k = 10.0          # Spring constant (N/m)
m = 1.0           # Mass (kg)
b = 0.002           # Damping coefficient (kg/s)
A = 1.0           # Initial amplitude (m)

# Create the spring (horizontal helix)
spring = helix(pos=vector(0, 0, 0), axis=vector(A, 0, 0), radius=0.05, coils=20, color=color.green)

# Create the mass, starting on the left side of the floor
mass = sphere(pos=vector(0.5, 0, 0), radius=0.1, color=color.red)

# Create a label for energy

# Create the floor
floor = box(pos=vector(0.5, -0.05, 0), size=vector(2, 0.1, 0.1), color=color.gray(0.5))

# Time variables
t = 0
dt = 0.01  # Time step

# Initial velocity
velocity_x = 2  # Horizontal velocity

# Simulation loop
while t < 10:
    rate(100)  # Control the speed of the simulation

    # Calculate the spring force (to the left)
    spring_force = -k * (mass.pos.x - 0)  # Hooke's Law (x - x0), x0 is 0

    # Calculate damping force (opposite to velocity)
    damping_force = -b * velocity_x

    # Calculate net force
    net_force = spring_force + damping_force  # Both forces act to the left

    # Update acceleration
    acceleration = net_force / m

    # Update velocity and position using Euler's method
    velocity_x += acceleration * dt
    mass.pos.x += velocity_x * dt

    # Check for collision with the floor
    if mass.pos.x < 0:  # Prevent the mass from going left of the floor (x = 0)
        mass.pos.x = 0  # Set the mass position to the floor level
        velocity_x = -velocity_x * 0.8  # Reverse the horizontal velocity and apply damping (80% bounce)

    # Calculate kinetic energy
    kinetic_energy = 0.5 * m * (velocity_x**2)

    # Update the energy label

    # Update the spring position
    spring.axis = vector(mass.pos.x, 0, 0)

    # Update the graph
    f1.plot(t, mass.pos.x)

    # Update time
    t += dt