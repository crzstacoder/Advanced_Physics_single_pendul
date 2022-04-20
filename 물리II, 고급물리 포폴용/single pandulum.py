import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
from scipy.integrate import odeint
import celluloid


def func(theta, t, b, g, l, m) :
    theta1 = theta[0]
    theta2 = theta[1]
    
    dtheta1_dt = theta2
    
    dtheta2_dt = -(b/m)*theta2-(g/1)*math.sin(theta1)
    
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    
    return dtheta_dt

b = 0.05
g = 9.8
l = 1
m = 0.1

theta0 = [0,5]
t = np.linspace(0, 20, 100)

theta = odeint (func, theta0, t, args = (b,g,l,m))

plt.figure()
plt.plot(t, theta[:,0], 'b-', label = '1st')
plt.plot(t, theta[:,1], 'r--', label = '2nd')
plt.ylabel('Plot')
plt.xlabel('time')
plt.legend(loc = 'best')
plt.show()

fig = plt.figure(figsize=(5,5), facecolor= 'w')
ax = fig.add_subplot(1,1,1)
plt.rcParams['font.size'] = 15

lns = []



for i in range(len(theta)) :
    ln, = ax.plot ([0,np.sin(theta[i,0])], [0, -np.cos(theta[i,0])], color = 'k', lw = 2)
    mass, = ax.plot(np.sin(theta[i,0]),-np.cos(theta[i,0]),'o', markersize = 20, color = 'r')
    tm = ax.text(-0.9,0.25,'Time = %.1fs'%t[i])
    lns.append([ln,mass,tm])
    
ax.set_aspect('equal', 'datalim')

animate = animation.ArtistAnimation(fig, lns, interval = 50)
animate.save('pendul.gif', writer='ffmpef', fps = 60)

# animate = animation.ArtistAnimation(fig, lns, interval = 50)
# animate.save('Pendulum Animation.gif', writer='PillowWriter', fps = 60)