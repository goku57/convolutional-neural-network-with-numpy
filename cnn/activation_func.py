import numpy as np


class ReLU():
    ''' Implements activation function rectified linear unit (ReLU)

    ReLU activation function is defined as the positive part of
    its argument alias ReLU(X) = max(0,x)
    '''

    def __init__(self):
        self.params = []

    def forward(self, X):
        ''' In the forward pass return the identity for x < 0

        Safe input for backprop and forward all values that are above 0.
        '''
        self.X = X
        return np.maximum(X, 0)

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X <= 0 in forward pass
                return 0 else x (local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX[self.X <= 0] = 0
        return dX, []


class LeakyReLU():
    ''' Implements activation function leaky rectified linear unit (Leaky ReLU)

    Leaky ReLU activation function is defined as max(x,0.01*x).
    '''

    def __init__(self):
        self.params = []

    def forward(self, X):
        ''' In the forward pass return the identity for x < 0 and else x*0.01

        Safe input for backprop and forward all values that are above 0.
        '''
        self.X = X
        return np.maximum(X, 0.01 * X)

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X <= 0 in forward pass
                return 0 * x else x (local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX[self.X <= 0] = 0.01 * dX[self.X <= 0]
        return dX, []
    
class ParametricReLU():
    ''' Implements activation function parametric rectified linear unit (Leaky ReLU)

    Parametric ReLU activation function is defined as x for x < 0 and else a * x
    '''

    def __init__(self, a):
        self.params = []
		self. a = a

    def forward(self, X):
        ''' In the forward pass return the identity for x < 0 and else x*a

        Safe input for backprop and forward all values that are above 0.
        '''
        self.X = X
	X[X <= 0] = self.a * X[X <= 0]
        return X

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X <= 0 in forward pass
                return a * x else x (local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX[self.X <= 0] = self.a * dX[self.X <= 0]
        return dX, []    

class ExponentialReLU():
    ''' Implements activation function exponential rectified linear unit (Leaky ReLU)

    Exponential ReLU activation function is defined as x for x > 0 and a*(exp(x) - 1) else.
    '''

    def __init__(self, a):
        self.params = []
		self. a = a

    def forward(self, X):
        ''' In the forward pass return the identity for x < 0 and else a*(exp(x) - 1)

        Safe input for backprop and forward all values that are above 0.
        '''
        self.X = X
	X[X <= 0] = self.a * (np.exp(X[X <= 0]) - 1)
        return X

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X <= 0 in forward pass
                return a * x else x (local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX[self.X <= 0] = self.a * (np.exp(dX[self.X <= 0]) - 1)
        return dX, []    


class sigmoid():
    '''
    Implements activation function sigmoid

    Sigmoid activation function is defined as 1/(1+ exp(-x))
    '''

    def __init__(self):
        self.params = []

    def forward(self, X):
        ''' In the forward pass return sigmoid(X)

        Safe input for backprop and forward all values.
        '''
        self.X = X
        return 1 / (1 + np.exp(-X))

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X in forward pass
                return sigmoid(x) * (1 - sigmoid(x))(local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX = 1/ (1 +np.exp(-dX))
        dX = dX * (1 - dX)
        return dX, []


class tanh():
    '''
    Implements activation function tanh

    Tanh activation function is defined as tanh(x)
    '''

    def __init__(self):
        self.params = []

    def forward(self, X):
        ''' In the forard pass return tanh(x)

        Safe input for backprop and forward all values
        '''
        self.X = X
        return np.tanh(X)

    def backward(self, dout):
        ''' calulate the backward path (local gradient of our function) for backpropagation

        Returns:
            dX: for all x \elem X <= 0 in forward pass
                return 1 - tanh(x) ** 2(local gradient)

            []: no gradients (global) on ReLU operation
        '''
        dX = dout.copy()
        dX = 1 - np.tanh(dX) ** 2
        return dX, []
