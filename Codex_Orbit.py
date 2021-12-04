"""
    Obtains the Cartesian coordinates of an orbit as a function of time, from orbital paramiters 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.io as pio
pio.renderers.default='browser'
# pio.renderers.default = "svg"

def orbit(t,e,a,i,omega,Omega,M):
    """
    Obtains the Cartesian coordinates of an orbit as a function of time, from orbital paramiters 
    """
    #Mean motion
    n = np.sqrt(mu/a**3)
    #Mean anomaly
    M = n*(t-to)
    #Initialize the x,y coordinates
    r = [0.0]*len(t)
    x = [0.0]*len(t)
    y = [0.0]*len(t)
    #Initialize the x,y velocities
    v_x = [0.0]*len(t)
    v_y = [0.0]*len(t)
    #Eccentric anomaly
    E = [0.0]*len(t)
    #Position
    r = [0.0]*len(t)
    #Velocity
    v = [0.0]*len(t)
    for j in range(len(t)):
        #Initialize the eccentric anomaly
        if e > 0.8:
            E[j] = M[j]
        else:
            E[j] = np.arctan2((np.sqrt(1.0-e**2)*np.sin(M[j])),(np.cos(M[j])-e))
        #Initialize the true anomaly
        nu = 2*np.arctan2(np.sqrt(1.0+e)*np.sin(E[j]/2.0),np.sqrt(1.0-e)*np.cos(E[j]/2.0))
        #Position
        r[j] = a*(1.0-e*np.cos(E[j]))
        x[j] = r[j]*(np.cos(Omega*np.pi/180.0)*np.cos(omega*np.pi/180.0+nu)-np.sin(Omega*np.pi/180.0)*np.sin(omega*np.pi/180.0+nu)*np.cos(i*np.pi/180.0))
        y[j] = r[j]*(np.sin(Omega*np.pi/180.0)*np.cos(omega*np.pi/180.0+nu)+np.cos(Omega*np.pi/180.0)*np.sin(omega*np.pi/180.0+nu)*np.cos(i*np.pi/180.0))
        #Velocity
        v[j] = np.sqrt(mu*a)/r[j]*e*np.sin(E[j])
        v_x[j] = v[j]*(np.cos(Omega*np.pi/180.0)*np.cos(omega*np.pi/180.0+nu)-np.sin(Omega*np.pi/180.0)*np.sin(omega*np.pi/180.0+nu)*np.cos(i*np.pi/180.0))
        v_y[j] = v[j]*(np.sin(Omega*np.pi/180.0)*np.cos(omega*np.pi/180.0+nu)+np.cos(Omega*np.pi/180.0)*np.sin(omega*np.pi/180.0+nu)*np.cos(i*np.pi/180.0))
    return x,y,v_x,v_y

#Define the parameters
mu = 1.0
to = 0.0
eo = 0.5
a = 1.0
i = 0.0
omega = 0.0
Omega = 0.0
M = 0.0

#Define the time vector
t = np.linspace(0,10,1000)

#Obtain the orbit
x,y,v_x,v_y = orbit(t,eo,a,i,omega,Omega,M)

#Plot the orbit
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i, t):
    thisx = [0, x[i]]
    thisy = [0, y[i]]
    dt = t[1]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template%(i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
    interval=25, blit=True, init_func=init)

#ani.save('orbit.mp4', fps=15)
plt.show()