import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class GaussianNB:
    '''Gaussian Naive Bayes
    '''
    def init_params(self, x_train, y_train):
        # There are n samples and m features in dataset.
        self.no_samples, self.no_features = x_train.shape

        # Classes are the unique labels. 
        # For examples: for a data: [1, 2, 3, 4] and label [0, 0, 1, 1]
        # there are 2 classes: 0 and 1.
        self.no_classes = len(np.unique(y_train))


    def seperate_by_class(self, x_train, y_train):
        self.mean_class = {}
        self.var_class = {}
        self.prior_class = {}

        for i in range(self.no_classes):
            # for ith class, x_ith array has all the train data where y_train = i  
            x_i = self.x_train[self.y_train == i]
            # Calculate mean, var and priors of each classes and form a directory  
            self.mean_class[str(i)] = np.mean(x_i, axis=0)
            self.var_class[str(i)] = np.var(x_i, axis=0)
            self.prior_class[str(i)] = x_i.shape[0] / self.no_samples

    def gaussian_density_func(self, X, mean, var, eps=1e-6):
        c = -self.no_features/2 * np.log(2*np.pi) - 0.5 * np.sum(np.log(var + eps))
        p = 0.5 * np.sum(np.power(X - mean, 2)/(var + eps), axis=1)
        return c - p


    def class_probabilities(self, X):
        """
        calculate the probability of each class given the data
        """
        
        probs = np.zeros((self.no_samples, self.no_classes))
        for cls in range(self.no_classes): 
            # get prior for cls_th class
            prior = self.prior_class[str(cls)]
            # calculate prob from gaussian density 
            probs_cls = self.gaussian_density_func(X, self.mean_class[str(cls)], self.var_class[str(cls)])
             
            probs[:, cls] = probs_cls + np.log(prior)
        return probs

    def predict(self, x_train, x_test, y_train, y_test):
        ''' 
        :param x_train: training data
        :param x_test:  testing data
        :param y_train: training label
        :param y_test:  testing label (target)
        '''
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

        # init some required parameters
        self.init_params(x_test, y_train)
        
        # separate the given data into unique classes accourding to their label 
        self.seperate_by_class(x_train, y_train)
        # get the probability that test data lies in which class 
        probs = self.class_probabilities(x_test)
        
        return np.argmax(probs, 1)


def main():
    # Load the given data and label as numpy array
    print("Loading data and  labels...")
    data = np.load('../Embeddings/emb.npy')
    label = np.load('../Embeddings/label.npy')

    # We have 10457 samples with 512 features
    print('Data shape: ', data.shape)

    # split the given data and label into test and train data/label
    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size = 0.2)

    print('Train data shape:', x_train.shape)
    print('Test data shape:', x_test.shape)

    GNB = GaussianNB()
    start = time.process_time() 
    predicted = GNB.predict(x_train,x_test, y_train, y_test)
    print(time.process_time() - start)

    print(f"Accuracy:{accuracy_score(y_test, predicted)}")
    print(f"predictions: {predicted}")

if __name__ == "__main__":
    main()
