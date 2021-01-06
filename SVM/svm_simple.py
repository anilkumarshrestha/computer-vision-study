import numpy as np

class SVM_simple:
    def __init__(self, learning_rate=0.001, lambda_ = 0.01, iters = 1000):
        self.learning_rate = learning_rate
        self.lambda_ = lambda_ 
        self.iters = iters
        self.w = None
        self.b = None
    
    def fit(self, data, label):
        n_samples, n_features = data.shape
        # set label -1 if it's < 0 and 1 otherwise
        y = np.where(label <= 0, -1, 1)

        self.w = np.zeros(n_features)
        self.b = 0
        for _ in range(self.iters):
            for i, x_i in enumerate(data):
                c = y[i] * (np.dot(x_i, self.w) - self.b)
                if (c >= 1):
                    self.w -= self.learning_rate * (2 * self.lambda_ * self.w)
                else:
                    self.w -= self.learning_rate * (2 * self.lambda_ * self.w - np.dot(x_i, y[i]))
                    self.b -= self.learning_rate * y[i]

    def predict(self, X):
        res = np.dot(X, self.w) - self.b
        return np.sign(res)

