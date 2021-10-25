import numpy as np
from scipy.stats import norm

amount_underlying = 100
strike = 1.1
sigma = 0.2
mu = 0.05
r = 0.015
S0 = 1
t = 1

def fun_d1(sigma,k,t,r,x):
    return (np.log(x/k) + (r+sigma**2/2)*t)/(sigma*np.sqrt(t))

def fun_d2(sigma,k,t,r,x):
    return fun_d1(sigma,k,t,r,x) - sigma*np.sqrt(t)

def call_value(amount_underlying, sigma,k,t,r,x):
    d1 = fun_d1(sigma,k,t,r,x)
    d2 = fun_d2(sigma,k,t,r,x)
    temp = norm.cdf(d1)*x-norm.cdf(d2)*k*np.exp(-r*t)
    return amount_underlying * temp
    
C0 = call_value(amount_underlying, sigma,strike,t,r,S0)

print(C0)

