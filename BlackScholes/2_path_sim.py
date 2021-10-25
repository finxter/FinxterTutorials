import numpy as np
import matplotlib.pyplot as plt

Nsim = 30
t0 = 0
t1 = 1
Nt = 100

mu=0.05
sigma=0.2
S0 = 1

t = np.linspace(t0,t1,Nt)
dt = (t1-t0)/Nt

np.random.seed(0)

S = np.zeros([Nsim,Nt])
S[:,0] = S0
for j in range(0, Nt-1):
    S[:,j+1] = S[:,j]*np.exp((mu-sigma**2/2)*dt + sigma*np.sqrt(dt)*np.random.normal(0,1, Nsim))

for j in range(0,Nsim):
    plt.plot(t,S[j,:])
plt.show()

