
V = []
x = 0.5
for i in range(8):
    V.append(x)
    x += 0.5

I = [1.8,3.2,5.4,7.3,9,10.8,12.2,14.4]
mA = 1e-3 

print("{:<13} {:<8} {:<13}".format("Voltages (V)","I (mA)","Resistance (Ω)"))


Av = []
for x in range(len(V)):
    Ix = I[x]
    Vx = V[x]
    Rx = round(Vx / (Ix * mA),2)
    Av.append(Rx)
    # print(Rx)

average = round(sum(Av) / len(Av),2)
# print(average)

for b in range(len(V)):

    print("{:<13} {:<8} {:<13}".format(V[b],I[b],Av[b]))
