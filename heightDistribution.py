from readonly.HeightsModule import *
import matplotlib.pyplot as plt
import numpy as np

"""
If we have data for the heights of people in a population, it can be plotted as a histogram, i.e., a bar chart where each bar has a width representing a range of heights, and an area which is the probability of finding a person with a height in that range. We can look to model that data with a function, such as a Gaussian, which we can specify with two parameters, rather than holding all the data in the histogram.

The Gaussian function is given as,
f(x;μ,σ)=1σ2π⎯⎯⎯⎯√exp(−(x−μ)22σ2)
f(x;μ,σ)=1σ2πexp⁡(−(x−μ)22σ2)
 
The figure above shows the data in orange, the model in magenta, and where they overlap in green. This particular model has not been fit well - there is not a strong overlap.

Recall from the videos the definition of  χ2χ2  as the squared difference of the data and the model, i.e  χ2=|y−f(x;μ,σ)|2χ2=|y−f(x;μ,σ)|2 . This is represented in the figure as the sum of the squares of the pink and orange bars.

Don't forget that  xx  an  yy  are represented as vectors here, as these are lists of all of the data points, the |abs-squared| 22  encodes squaring and summing of the residuals on each bar.

To improve the fit, we will want to alter the parameters  μμ  and  σσ , and ask how that changes the  χ2χ2 . That is, we will need to calculate the Jacobian,
J=[∂(χ2)∂μ,∂(χ2)∂σ].
J=[∂(χ2)∂μ,∂(χ2)∂σ].
 
Let's look at the first term,  ∂(χ2)∂μ∂(χ2)∂μ , using the multi-variate chain rule, this can be written as,
∂(χ2)∂μ=−2(y−f(x;μ,σ))⋅∂f∂μ(x;μ,σ)
∂(χ2)∂μ=−2(y−f(x;μ,σ))⋅∂f∂μ(x;μ,σ)
 
With a similar expression for  ∂(χ2)∂σ∂(χ2)∂σ ; try and work out this expression for yourself.

The Jacobians rely on the derivatives  ∂f∂μ∂f∂μ  and  ∂f∂σ∂f∂σ . Write functions below for these.

"""
# This is the Gaussian function.
def f (x,mu,sig) :
    return np.exp(-(x-mu)**2/(2*sig**2)) / np.sqrt(2*np.pi) / sig


def dfdmu (x,mu,sig) :
    return f(x, mu, sig) * (x-mu)/sig**2



def dfdsig (x,mu,sig) :
    return  -f(x, mu, sig)/sig + f(x, mu, sig) * (x-mu)**2/sig**3
    
def steepest_step (x, y, mu, sig, aggression) :
    J = np.array([
        -2*(y - f(x,mu,sig)) @ dfdmu(x,mu,sig),
        -2*(y - f(x,mu,sig)) @ dfdsig(x,mu,sig) # 2nd element of the Jacobian.
    ])
    step = -J * aggression
    return step
    
x,y = heights_data()

# Next we'll assign trial values for these.
mu = 155 ; sig = 6
# We'll keep a track of these so we can plot their evolution.
p = np.array([[mu, sig]])

# Plot the histogram for our parameter guess
histogram(f, [mu, sig])
# Do a few rounds of steepest descent.
for i in range(50) :
    dmu, dsig = steepest_step(x, y, mu, sig, 2000)
    mu += dmu
    sig += dsig
    p = np.append(p, [[mu,sig]], axis=0)
# Plot the path through parameter space.
contour(f, p)
# Plot the final histogram.
histogram(f, [mu, sig])