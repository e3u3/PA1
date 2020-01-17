import numpy as np 

class LR_Classifier():
    def __init__(self, inputs_dim=None):
        self.Linear1 = np.random.normal(size=inputs_dim+1)

    def forward(self, x):
        print("inputs shape: ", x.shape)
        batch_size = x.shape[0]
        a = np.dot(x,self.Linear1)
        self.outputs = 1/(1+np.exp(a))
        self.predictions = self.outputs > 0.5
        # print("predictions shape: ", predictions.shape)
        return self.outputs, self.predictions

    def update(self, learning_rate=0.001):
        self.Linear1 = self.Linear1 - learning_rate * self.grad



    