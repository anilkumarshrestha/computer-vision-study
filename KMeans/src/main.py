import os
import numpy as np
from mlxtend.data import loadlocal_mnist
from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from scipy.stats import mode
# from numpy.linalg import norm

class Kmeans:
    ''' Kmeans class'''
    
    def __init__(self, n_clusters=10, max_itr=300, rseed=2):
        self.n_clusters = n_clusters
        self.max_itr = max_itr
        self.rseed = rseed

    def init_centroids(self, X):
        np.random.RandomState(self.rseed)
        
        # n_clusters number of Random index to select entroids
        # randomly permute n_clusters number of clusters within 0 to 60000(i.e X.shape[0])
        i = np.random.permutation(X.shape[0])[:self.n_clusters]
        
        # Random centroids choosen from random index
        centroids = X[i]
        return centroids

    def get_distance(self, X, centroids):
        
        # Initialize zero numpy arrays of dim (60000, 10) 
        # to store distance of each point with respect to each cluster
        distance = np.zeros((X.shape[0], self.n_clusters))
        for k in range(self.n_clusters):
            # Distance from kth cluster.
            # At kth iteration: X - centroids => (60000, 784) - (1, 784) (i.e. Broadcasting)
            distance[:, k] = np.sqrt( ( (X - centroids[k, :])**2 ).sum(axis = 1) )
            #row_norm = norm(X - centroids[k, :], axis=1)
            #distance[:, k] = np.square(row_norm)
        return distance

    def calculate_centroids(self, X, labels):
        
        # Initialize centroids of dim (10, 784)
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            # Get Xs that has labels = k
            # Calculate mean of the obtained Xs in Y direction
            centroids[k, :] = np.mean(X[labels == k, :], axis = 0)
        return centroids

    def get_closest_cluster(self, distance):
        # return index of minimum
        return np.argmin(distance, axis=1)
    
    def fit(self, X):
        # Initialize centroids to random points
        self.centroids = self.init_centroids(X)

        # Loop until max_iteration reached or centroid remains same
        # tqdm to track progress
        for i in tqdm(range(self.max_itr)):
            self.old_centroids = self.centroids
            distance = self.get_distance(X, self.old_centroids)
            self.labels = self.get_closest_cluster(distance)
            self.centroids = self.calculate_centroids(X, self.labels)

            if np.all(self.old_centroids == self.centroids):
                print("Converged before maximum iteration...")
                break

    def predict(self, X):
        distance = self.get_distance(X, self.old_centroids)
        return self.get_closest_cluster(distance)

def load_data():

    files = ['../data/train-images.idx3-ubyte', '../data/train-labels.idx1-ubyte',
            '../data/t10k-images.idx3-ubyte', '../data/t10k-labels.idx1-ubyte']
    for file_ in files:
        if not os.path.isfile(file_):
            print("Could not find: ", file_)
    
    # Load train data.
    # mlxtend directly loads in (6000, 28*28).
    X, y = loadlocal_mnist(
            images_path = files[0],
            labels_path = files[1]
            )

    test_X, test_y = loadlocal_mnist(
            images_path = files[2],
            labels_path = files[3]
            )
    return X, y, test_X, test_y

def get_labels(n_clusters, clusters, actual_label):
    labels = np.zeros_like(clusters)
    for i in range(n_clusters):
        mask = (clusters == i)
        labels[mask] = mode(actual_label[mask])[0]
    return labels

def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


def main():
    # load MNIST data
    # Get data from: http://yann.lecun.com/exdb/mnist/
    print("Implementing KMeans in MNIST")
    print("loading data...")
    data, labels, test_data, test_labels= load_data()
    
    # Number of clusters
    n_clusters = 10
    rseed = 2
    
    # Initialize Kmeans
    k = Kmeans(n_clusters, rseed=rseed)

    # fit
    print("fitting data...")
    k.fit(data)
    
    print("predicting...")
    predict = k.predict(test_data)
    # get the labels of predicted data
    predicted_labels = get_labels(n_clusters, predict, test_labels)

    print("Accuracy: ", accuracy_metric(test_labels, predicted_labels))

    mat = confusion_matrix(test_labels, predicted_labels)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
    plt.xlabel('true label')
    plt.ylabel('predicted label');
    plt.savefig('confusion_mat.png')

    # KMeans using sklearn
    sklearn = KMeans(n_clusters=n_clusters, random_state=rseed).fit(data)
    sp = sklearn.predict(test_data)
    sp_labels = get_labels(n_clusters, sp, test_labels)
    print("SK learn Accuracy:", accuracy_metric(test_labels, sp_labels))

if __name__ == "__main__":
    main()
