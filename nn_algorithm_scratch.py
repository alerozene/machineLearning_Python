""""
Example of a Neural Network: fits a set of data to a desired vector y
Alex Rozene 
""""
import numpy as np


class NeuralNetwork:
    """"
    Takes input x which can be a matrix or vector. Desired output y which must 
    be a vector and number of layers 
    """"
    def __init__(self,x,y,nl):
        self.x = x;
        self.w1 = np.random.rand(self.input.shape[1],4)
        self.w2 = np.random.rand(self.input.shape[1],4)
        self.y  = y
        self.fit  = np.zeros(y.shape)
        
        self.weightmatrix = np.zeros()
    
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))
    def sigmoidprima(z):
        return z*(1.0-z)
    
    def feedworward(self):
        self.layer1 = sigmoid(np.dot(self.w1,self.x))
        self.layer2 = sigmoid(np.dot(self.w2,self.layer1))    
    def backpropagation(self):
        

    
    
    
""""
Full credit to:
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-
scratch-in-python-68998a08e4f6

https://www.kdnuggets.com/2019/11/build-artificial-neural-network-scratch-part-1.html

"""