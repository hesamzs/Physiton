from vpython import *

k = 10 # N/m
g = 9.8 # m/s**2
b = 0.5 # N*s/m
m = 1 # kg
A = 1 # m
v = 0

spring = helix(pos=vector(0,0,0),axis=vector(0,-A,0),coils=20,radius=0.05)
mass = sphere(pos=vector(0,A,0),radius=0.5 , color=color.red)

graph = graph(width=400,height=200,xtitle="t(s)",ytitle="y(m)")
f1 = gcurve(color=color.blue)
t = 0
dt = 0.01
while t < 100:
    rate(100)
    sprin_force = -k * mass.pos.y
    gravity_force = m * g
    damping_force = -b * v

    fnet_force = sprin_force - gravity_force + damping_force
    
    a = fnet_force / m

    v += a *dt
    mass.pos.y += v *dt

    spring.axis = vector(0,mass.pos.y,0)
    f1.plot(t,mass.pos.y)
    t += dt
    pass

