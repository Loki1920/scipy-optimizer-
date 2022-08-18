from scipy.optimize import minimize
from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, -1)

print(myroot.x)
# print all information about root
print(myroot)

# minimize a function 

def eqn1(x):
    return x**2 + x + 2


mymin = minimize(eqn1,1,method = 'BFGS')
print(mymin)