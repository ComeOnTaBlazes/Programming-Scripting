# IPython log file
# James Hannon
# Program to plot 3 functions (y1, y2, y3)
# in range 0-4 using Matplotlib

# Used Ian's video completely for this
# Code pulled from ipython file created

import numpy as np

import matplotlib.pyplot as plt

l = np.linspace(0, 4, 50)

y1 = l
y2 = l**2
y3 = l**3

plt.plot(l, y1)
plt.plot(l, y1)
plt.plot(l, y1, 'y.', label = "f(x)=x")
plt.plot(l, y2, 'r.', label = "g(x)=x2")
plt.plot(l, y3, 'g.', label = "h(x)=x3")
plt.legend()
plt.title("ComeOnTaBlazes")
plt.ylabel("Result")
plt.xlabel("Input")


plt.show()