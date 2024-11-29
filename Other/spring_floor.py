from vpython import *
import numpy as np

# Create the scene
scene = canvas(title='Damped Spring-Mass System with Floor', width=800, height=400)
g1 = graph(title="Mass Position", xtitle="Time (s)", ytitle="Position (m)", width=400, height=250)
f1 = gcurve(color=color.blue)

# Constants
k = 10.0          # Spring constant (N/m)
m = 1.0           # Mass (kg)
b = 0.1           # Damping coefficient (kg/s)
g = 9.81          # Acceleration due to gravity (m/s^2)
A = 1.0           # Initial amplitude (m)

# Create the spring
spring = helix(pos=vector(0, 0, 0), axis=vector(0, -A, 0), radius=0.05, coils=20, color=color.green)

# Create the mass
mass = sphere(pos=vector(0, A, 0), radius=0.1, color=color.red)

# Create a label for energy
energy_label = label(pos=vector(0, 1.5, 0), text='Kinetic Energy: 0 J', height=16, box=False)

# Create the floor
floor = box(pos=vector(0, -0.2, 0), size=vector(2, 0.1, 0.1), color=color.gray(0.5))

# Time variables
t = 0
dt = 0.01  # Time step

# Initial velocity
velocity = 0

# Simulation loop
while t < 10:
    rate(100)  # Control the speed of the simulation

    # Calculate the spring force (upward)
    spring_force = -k * (mass.pos.y - 0)  # Hooke's Law (y - y0), y0 is 0

    # Calculate the gravitational force (downward)
    gravity_force = m * g

    # Calculate damping force (opposite to velocity)
    damping_force = -b * velocity

    # Calculate net force
    net_force = spring_force - gravity_force + damping_force

    # Update acceleration
    acceleration = net_force / m

    # Update velocity and position using Euler's method
    velocity += acceleration * dt
    mass.pos.y += velocity * dt

    # Check for collision with the floor
    if mass.pos.y < -0.1:  # Assuming the floor is at y = -0.1
        mass.pos.y = -0.1  # Set the mass position to the floor level
        velocity = -velocity * 0.8  # Reverse the velocity and apply damping (80% bounce)

    # Calculate kinetic energy
    kinetic_energy = 0.5 * m * velocity**2

    # Update the energy label
    energy_label.text = f'Kinetic Energy: {kinetic_energy:.2f} J'

    # Update the spring position
    spring.axis = vector(0, mass.pos.y, 0)

    # Update the graph
    f1.plot(t, mass.pos.y)

    # Update time
    t += dt