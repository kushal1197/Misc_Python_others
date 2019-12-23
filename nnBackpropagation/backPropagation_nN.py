"""
Backpropagation

Element wise: when two matrices have the same dimensions, matrix elements in the same position in each matrix are multiplied together In python this uses the ' ∗∗ ' operator.

A = B * C

Matrix multiplication: when the number of columns in the first matrix is the same as the number of rows in the second. In python this uses the ' @@ ' operator

A = B @ C

a(n)=σ(z(n))
 
z(n)=W(n)a(n−1)+b(n)
 
we will use the logistic function as our activation function, rather than the more familiar  tanhtanh .

σ(z)=(1/(1+exp(−z)))
"""

import numpy as np
import matplotlib.pyplot as plt

# First load the worksheet dependencies.
# Here is the activation function and its derivative.
sigma = lambda z : 1 / (1 + np.exp(-z))
d_sigma = lambda z : np.cosh(z/2)**(-2) / 4

# This function initialises the network with it's structure, it also resets any training already done.
def reset_network (n1 = 6, n2 = 7, random=np.random) :
    global W1, W2, W3, b1, b2, b3
    W1 = random.randn(n1, 1) / 2
    W2 = random.randn(n2, n1) / 2
    W3 = random.randn(2, n2) / 2
    b1 = random.randn(n1, 1) / 2
    b2 = random.randn(n2, 1) / 2
    b3 = random.randn(2, 1) / 2

# This function feeds forward each activation to the next layer. It returns all weighted sums and activations.
def network_function(a0) :
    z1 = W1 @ a0 + b1
    a1 = sigma(z1)
    z2 = W2 @ a1 + b2
    a2 = sigma(z2)
    z3 = W3 @ a2 + b3
    a3 = sigma(z3)
    return a0, z1, a1, z2, a2, z3, a3

# This is the cost function of a neural network with respect to a training set.
def cost(x, y) :
    return np.linalg.norm(network_function(x)[-1] - y)**2 / x.size
    

"""
Backpropagation

define our Jacobians as,
JW(3)=∂C/∂W(3)
 
Jb(3)=∂C/∂b(3)
 
etc., where  CC  is the average cost function over the training set. i.e.,
C=(1/N)∑kCk

for the weight
∂C/∂W(3)=∂C/∂a(3) * ∂a(3)/∂z(3) * ∂z(3)/∂W(3),
 
and similarly for the bias
∂C∂/b(3)=∂C/∂a(3) * ∂a(3)/∂z(3) * ∂z(3)/∂b(3)
 
With the partial derivatives taking the form,
∂C/∂a(3)=2(a(3)−y)
 
∂a(3)/∂z(3)=σ′(z(3))
 
∂z(3)/∂W(3)=a(2)
 
∂z(3)/∂b(3)=1
"""



# Jacobian for the third layer weights. 
def J_W3 (x, y) :
    # First get all the activations and weighted sums at each layer of the network.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    # We'll use the variable J to store parts of our result as we go along, updating it in each line.
    # Firstly, we calculate dC/da3, using the expressions above.
    J = 2 * (a3 - y)
    # Next multiply the result we've calculated by the derivative of sigma, evaluated at z3.
    J = J * d_sigma(z3)
    # Then we take the dot product (along the axis that holds the training examples) with the final partial derivative,
    # i.e. dz3/dW3 = a2
    # and divide by the number of training examples, for the average over all training examples.
    J = J @ a2.T / x.size
    # Finally return the result out of the function.
    return J

# Jacobian for the third layer bias. 

def J_b3 (x, y) :
    # As last time, we'll first set up the activations.
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)

    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
    
    
"""
∂C/∂W(2)=∂C/∂a(3) * (∂a(3)/∂a(2)) * ∂a(2)/∂z(2) * ∂z(2)/∂W(2)
 
∂C/∂b(2)=∂C/∂a(3) * (∂a(3)/∂a(2)) * ∂a(2)/∂z(2) * ∂z(2)∂b(2)
 
This is very similar to the previous layer, with two exceptions:

There is a new partial derivative, in parentheses,  ∂a(3)/∂a(2)
The terms after the parentheses are now one layer lower.
∂a(3)/∂a(2)=∂a(3)/∂z(3) * ∂z(3)/∂a(2) = σ′(z(3))W(3)
"""

# Jacobian for the second layer weights. 
def J_W2 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)    
    J = 2 * (a3 - y)
    # the next two lines implement da3/da2, first σ' and then W3.
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    # then the final lines are the same as in J_W3 but with the layer number bumped down.
    J = J * d_sigma(z2)
    J = J @ a1.T / x.size
    return J

# Jacobian for the second layer bias. 
def J_b2 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T@W3).T
    J = J*d_sigma(z2)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
    
"""
Layer 1 is very similar to Layer 2, but with an addition partial derivative term.
∂C/∂W(1)=∂C/∂a(3) * (∂a(3)/∂a(2) * ∂a(2)/∂a(1)) * ∂a(1)/∂z(1) * ∂z(1)∂W(1) 
∂C/∂b(1)=∂C/∂a(3) * (∂a(3)/∂a(2) * ∂a(2)/∂a(1)) * ∂a(1)/∂z(1) * ∂z(1)∂b(1)

"""

# Jacobian for the first layer weights. 
def J_W1 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2* (a3-y)
    J = J * d_sigma(z3)
    J = (J.T@W3).T
    J = J * d_sigma(z2)
    J = (J.T@W2).T
    J = J * d_sigma(z1)
    J = J @ a0.T / x.size
    return J

# Jacobian for the first layer bias. 
def J_b1 (x, y) :
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2* (a3-y)
    J = J * d_sigma(z3)
    J = (J.T@W3).T
    J = J * d_sigma(z2)
    J = (J.T@W2).T
    J = J * d_sigma(z1)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
    
    
x, y = training_data()
reset_network()

plot_training(x, y, iterations=10000, aggression=7, noise=1)