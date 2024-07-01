from dense import Dense
from tanh import Tanh
from mse import mse, mse_prime
import numpy as np

#
X = np.reshape([[0,0],[0,1],[1,0],[1,1]],(4,2,1))
Y = np.reshape([[0],[1],[1],[0]], (4,1,1))
#

network = [
    Dense(2,3),
    Tanh(),
    Dense(3,1),
    Tanh()
]
#
cycles = 100000
learning_rate = 0.1

# train
for e in range(cycles):
    error = 0
    for x, y in zip(X,Y):
        # Forward
        output = x
        for layer in network:
            output = layer.forward(output)

        # error
        error += mse(y,output)

        # Backward
        grad = mse_prime(y, output)
        for layer in reversed(network):
            grid = layer.backward(grad, learning_rate)

    error /= len(x)
    print("%d/%d, error = %f" % (e + 1, cycles, error))
