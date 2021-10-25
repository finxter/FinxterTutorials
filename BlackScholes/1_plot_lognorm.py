from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np
import math

mu = 0.05
sigma = 0.2
S0 = 1

x = np.linspace(0,2,1000)
y = lognorm.pdf(x, sigma,0,math.exp(mu-sigma**2/2))

plt.plot(x,y)
plt.show()
