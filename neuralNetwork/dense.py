from layer import Layer
import numpy as np


class Dense(Layer):

    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size,input_size) # Random matrix of weights
        self.bias = np.random.randn(output_size, 1) # Random vector of biases

    # Takes in input vector and produces output vector
    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias

    def backward(self, output_gradient, learning_rate):
        weights_gradient = np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate * weights_gradient
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T, output_gradient)