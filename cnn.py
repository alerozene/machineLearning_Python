""""
Example of a Neural Network 
Alex Rozene 
""""
import numpy as np


class NeuralNetwork:
    def __init__(self,x,y,nl):
        self.x = x;
        self.w1 = np.random.rand(self.input.shape[1],4)
        self.w2 = np.random.rand(self.input.shape[1],4)
        self.y  = y
        self.fit  = np.zeros(y.shape)
    
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))
    
    def feedworward(self):
        self.layer1 = sigmoid(np.dot(self.w1,self.x))
        self.layer2 = sigmoid(np.dot(self.w2,self.layer1))
        
    def

    
    
    
""""
Full credit to:
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-
scratch-in-python-68998a08e4f6
"""