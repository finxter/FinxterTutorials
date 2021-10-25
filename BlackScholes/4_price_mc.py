import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import lognorm
Nsim = 10000
amount_underlying = 100
strike = 1.1
sigma = 0.2
mu = 0.05
r = 0.015
np.random.seed(0)

def payoff(x):
    return amount_underlying * np.maximum(0, x-strike)

num0 = np.random.normal(0,1,Nsim)

S0 = 15

S1 = np.exp(r-sigma**2/2+sigma*num0)

_ = plt.hist(S1, bins=100, density=True)


C0 = math.exp(-r)*np.mean(payoff(S1))

print(C0)