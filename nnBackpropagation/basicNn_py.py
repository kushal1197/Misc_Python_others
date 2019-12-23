"""
Basics of a neural network
"""


#set up the network.
sigma = np.tanh
W = np.array([[-2, 4, -1],[6, 0, -3]])
b = np.array([0.1, -2.5])

# Define our input vector
x = np.array([0.3, 0.4, 0.1])

#calculate the output layer
a1_0 = sigma(np.matmul(W[0],x)+b[0])
a1_1 = sigma(np.matmul(W[1],x)+b[1])
a1 = np.array([a1_0, a1_1])



