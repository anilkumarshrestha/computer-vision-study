# Implement Activation functions
import numpy as np
#from matplotlib import pyplot as plt

class activation:
    '''Activation Functions
    '''
    def __init__(self, x):
        '''
        :param x: data on to apply activation function on
        '''
        self.x = x
    
    def sigmoid(self):
        '''Sigmod function
            f(x) = 1 / (1 + exp^(-x))
        '''
        return (1 / (1 + np.exp(-self.x)))
    
    def tanh(self):
        '''Tanh function
            f(x) = 2 / (1 + e^(-2x)) -1
        '''
        return (2 / (1 + np.exp(-2 * self.x)) - 1)
    
    def ReLU(self):
        '''ReLU function
            f(x) = x, x > 0
                   0, otherwise
        '''
        return np.maximum(self.x, 0)

    def LeakyReLU(self):
        '''Leaky ReLU function
            f(x) = x, x>0
                 = 0.01x, otherwise
        '''
        return np.where(self.x > 0, self.x, self.x * 0.01)

def main():
    x = np.random.randint(-10, 10, size=(10, 3))
    a = activation(x)
    sig = a.sigmoid()
    tanh = a.tanh()
    ReLU = a.ReLU()
    LeakyReLU = a.LeakyReLU()
    print("Activation Functions")
    print('x:\n{} '.format(x))
    print('Sigmoid:\n{}\nTanh:\n{}\nReLU:\n{}\nLeakyReLU\n{}'.format(
            sig,
            tanh,
            ReLU,
            LeakyReLU
        ))
if __name__ == "__main__":
    main()
