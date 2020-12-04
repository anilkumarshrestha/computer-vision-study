#!/usr/bin/env python
'''
    Naive Bayes Theorem:
        P(y|X) = P(X|y).P(y) / P(X)
               = argMax [ log(P(x1|y)) + log(P(x2|y))+ ... + log(P(xn|y)) + log(P(y))]
        
        Class conditional probability
            P(xi|y) = exp(-(xi - mean)^2 / 2 * (sigm^2)) / sqrt(2 * pi * sigma^2) 
'''

import numpy as np 
from sklearn.metrics import accuracy_score
class NaiveBayes:
    '''
        fit function
        priors, class conditionals 
        X ==> numpy array
        y ==> 1D row vector
    '''
    def fit(self, X, y):
        no_samples, no_features = X.shape
        self._classes = np.unique(y)
        no_classes = len(self._classes)

        self.mean = np.zeros((no_classes,no_features), dtype=np.float64)
        self.var = np.zeros((no_classes,no_features),dtype=np.float64)
        self.priors = np.zeros(no_classes,dtype=np.float64)

        for i,cl in enumerate(self._classes):
            X_cl = X[y == cl]
            self.mean[i,:] = X_cl.mean(axis=0)
            self.var[i,:] = X_cl.var(axis=0)
            # get frequency
            self.priors[i] = X_cl.shape[0] / float(no_samples)

    def predict(self,X):
        y_pred = [self.predict_helper(x) for x in X]
        return np.array(y_pred)

    def predict_helper(self,x):
        posteriors = []

        for i in range(len(self._classes)):
            #print(self.priors[i])
            #
            prior = np.log(self.priors[i])
            class_conditional_prob = np.sum(np.log(self.probability_den(i,x)))
            posterior = prior + class_conditional_prob
            posteriors.append(posterior)
        
        return self._classes[np.argmax(posteriors)]
    
    def probability_den(self,class_index, x):
        mean = self.mean[class_index]
        var = self.var[class_index]
        numerator = np.exp(- (x-mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator
    
    def _print(self):
      print(self.priors)


from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

# Load the given data and label as numpy array
print("Loading data and  labels...")
data = np.load('../Embeddings/emb.npy')
label = np.load('../Embeddings/label.npy')

# We have 10457 samples with 512 features
print('Data shape: ', data.shape)

# split the given data and label into test and train data/label
X_train,X_test, y_train, y_test = train_test_split(data, label, test_size = 0.2)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
import time
start = time.process_time()
# your code here    
nb = NaiveBayes()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)
print(time.process_time() - start)
#print(X_test)
print(predictions)
print("Naive Bayes classification accuracy", accuracy_score(y_test, predictions))
