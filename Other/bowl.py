from vpython import *

g1 = graph(title="ball spring",xtitle="t",ytitle="y",width=400, height=250)
f1 = gcurve(color=color.blue)

m = 1.5
h = 1
k = 1000
g = vector(0,-9.8,0)

velocity = 0
L0 = 0.4

ball = sphere(pos=vector(0,h,0),radius=0.1,color=color.yellow)
floor = box(pos=vector(0,-L0,0),size=vector(2,0.05,1))
ball.v = vector(0,0,0)
t = 0
dt = 0.01
spring=helix(pos=floor.pos,axis=vector(0,L0,0),radius=0.07,thickness=0.04)

while t<100:
  rate(100)
  Fnet = m*g
  r = ball.pos-floor.pos
  # print(mag(r))
  if mag(r)<L0:
    Fnet = (m*g + k*(L0-mag(r))*norm(r))
    print("mag(r):" ,Fnet)
    # print("norm:" ,norm(r))
    spring.axis = r
  a = Fnet/m
  ball.v = ball.v + a*dt
  ball.pos = ball.pos + ball.v*dt
  f1.plot(t,ball.pos.y)
  t = t + dt