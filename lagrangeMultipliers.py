"""
Lagrange multipliers
"""

# Import libraries
import numpy as np
from scipy import optimize

# define functions
def f (x, y) :
    return -np.exp(x-y*y+x*y)

def g (x, y) :
    return np.cosh(y)+x-2

# define derivatives
def dfdx (x, y) :
    return (-np.exp(x-y*y+x*y))*(1+y)

def dfdy (x, y) :
    return f(x,y)*(-2*y+x)

def dgdx (x, y) :
    return 1

def dgdy (x, y) :
    return np.sinh(y)

# 
def DL (xyλ) :
    [x, y, λ] = xyλ
    return np.array([
            dfdx(x, y) - λ * dgdx(x, y),
            dfdy(x, y) - λ * dgdy(x, y),
            - g(x, y)
        ])


x, y, λ = (0,0,0)

print("x = %g" % x)
print("y = %g" % y)
print("λ = %g" % λ)
print("f(x, y) = %g" % f(x, y))

