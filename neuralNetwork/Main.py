from dense import Dense
from tanh import Tanh
from mse import mse, mse_prime
import numpy as np

def CreatePlainPredictions(_network):
    # [0, 0.1, ... , 1](1 x 11) + [0, 0.1, ... , 1](11 x 1)
    X = []
    for rowInd in range(11):
        row = []
        for colInd in range(11):
            row.append([colInd/10, rowInd/10])
        X.append(row)
    X = np.array(X).reshape((121,2,1))

    count = 1
    outputList = []
    for x in zip(X):
        # Forward
        output = x
        for layer in _network:
            output = layer.forward(output)
        outputList.append(round(np.sum(output)), 4)
        count += 1
    pass

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
cycles = 10000
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
            grad = layer.backward(grad, learning_rate)

    error /= len(x)
    print("%d/%d, error = %f" % (e + 1, cycles, error))

# Creating 3D graph
# [0, 0.1, ... , 1](1 x 11) + [0, 0.1, ... , 1](11 x 1)
CreatePlainPredictions(network)