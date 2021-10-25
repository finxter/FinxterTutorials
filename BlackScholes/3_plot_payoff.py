import numpy as np
import matplotlib.pyplot as plt

k = 1.1

def payoff(x):
    return 100*np.maximum(0,x-k)

x=np.linspace(0,2, 100)
y=payoff(x)

plt.plot(x,y)
plt.xlabel('Stock price at expiry')
plt.ylabel('Payoff')
plt.show()

