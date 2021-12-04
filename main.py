import numpy as np
from math import pi
import matplotlib.pyplot as plt

class planet:
    def __init__(self, name, a, e, i, w, W) -> None:
        self.name = name
        self.a = a
        self.e = e
        self.i = np.deg2rad(i)
        self.w = np.deg2rad(w)
        self.W = np.deg2rad(W)
        pass

    def orbit(self, thetaf):
        p = ( 1-self.e**2 )*self.a
        theta = np.linspace( 0, thetaf, int(1e4) )
        r = p/( 1 + self.e*np.cos(theta) )
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        return x, y


planets = list()
planets.append( planet('Mercury', 0.3870993, 0.20564, 7.005, 29.13, 48.3) )
planets.append( planet('Venus', 0.723336, 0.00678, 3.3947, 54.9, 76.7) )
planets.append( planet('Earth', 1.000003, 0.01671, 0.0, 102.9, 0.0) )
planets.append( planet('Mars', 1.52371, 0.09339, 1.850, 286.5, 49.6) )
planets.append( planet('Jupiter', 5.2029, 0.0484, 1.304, 274.3, 100.4) )
planets.append( planet('Saturn', 9.537, 0.0539, 2.486, 338.9, 113.7) )
planets.append( planet('Urano', 19.189, 0.04726, 0.773, 96.9, 74.02) )
planets.append( planet('Urano', 30.0699, 0.00859, 1.77, 273.2, 131.784) )

x, y = planets[0].orbit(pi)

plt.plot(x, y)
plt.show()
