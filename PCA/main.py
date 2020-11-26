# Implementation of PCA on MNIST dataset
import os
import numpy as np
from mlxtend.data import loadlocal_mnist
from tqdm import tqdm
import matplotlib.pyplot as plt

def load_data():
    ''' Load MNIST data from local file'''
    files = ['data/train-images.idx3-ubyte', 'data/train-labels.idx1-ubyte']
    for file_ in tqdm(files):
        if not os.path.isfile(file_):
            print("Could not find: ", file_)
    
    # Load train data.
    # mlxtend directly loads in (6000, 28*28).
    X, y = loadlocal_mnist(
            images_path = files[0],
            labels_path = files[1]
            )

    return X, y

def eigen_decomposition(A, max_iter=100):
    ''' Finds eigenvalues and eigen vectors
    :param A: covarience matrix
    :param max_iter: maximum number of iteration
    '''
    A_k = A
    # shape of A = 60000x784
    Q_k = np.eye( A.shape[1] )
    
    # print("in eigen_dec")
    for k in range(max_iter):
        # at each step calculate Ak+1 by taking the QR decomposition of Ak
        Q, R = qr_decomposition(A_k)
        Q_k = np.dot(Q_k,Q)
        A_k = np.dot(R, Q)

    eigenvalues = np.diag(A_k)
    eigenvectors = Q_k
    return eigenvalues, eigenvectors

def householder_reflection(a, e):
    '''returns an orthogonal matrix which maps a 
    vector a (where a is non-zero and not collinear with e)
    into the line of e (a unit vector).
    '''
    
    assert a.ndim == 1
    assert np.allclose(1, np.sum(e**2))
    
    u = a - np.sign(a[0]) * np.linalg.norm(a) * e  
    v = u / np.linalg.norm(u)
    H = np.eye(len(a)) - 2 * np.outer(v, v)
        
    return H


def qr_decomposition(A):
    '''Given an n x m invertable matrix A, returns the pair:
        Q an orthogonal n x m matrix
        R an upper triangular m x m matrix
    such that QR = A.
    :param A:
    '''
    
    n, m = A.shape
    assert n >= m
    
    Q = np.eye(n)
    R = A.copy()
    
    for i in tqdm(range(m - int(n==m))):
        # get ith row as r
        r = R[i:, i]
        
        # check if the row is zero
        if np.allclose(r[1:], 0):
            continue
            
        # e is the i-th basis vector of the minor matrix.
        e = np.zeros(n-i)
        e[0] = 1  
        
        H = np.eye(n)
        H[i:, i:] = householder_reflection(r, e)

        Q = np.dot(Q,H.T)
        R = np.dot(H,R)
    
    return Q, R

class PCA:
    def __init__(self, dim):
        self.dim = dim

    def standardization(self,data):
        X = data.data
        mean = np.mean(X,axis=0)
        X_center = X - mean
        std = np.std(X, axis=0)
        # Standardizing the dataset and if divide by zero case appears then converting it to zero
        X = np.divide(X_center, std, out=np.zeros_like(X_center), where=std!=0)
        return X

    def sort_and_reduce(self):
        print("Sorting Eigenvectors")
        # sort eigen values and eigen vectors.
        sorted_index = np.argsort(self.eigen_val)[::-1]
        sorted_eigenval = self.eigen_val[sorted_index]
        sorted_eigenvectors = self.eigen_vec[:,sorted_index]
        
        # Select the subset as of the dimension we need here 3
        eigenvec_sub = sorted_eigenvectors[:, 0:self.dim]
        # Get the reduced dataset
        return np.dot(eigenvec_sub.transpose(), self.data.transpose()).transpose()
        # print(reduced_data)

    def plot(self,proj_data):

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.view_init(15, -60)

        # colors to choose from
        colormap = np.array(['red', 'green', 'blue', 'yellow', 'orange', 'brown', 'purple', 'pink', 'gray', 'olive', 'cyan'])
        

        # for c in np.unique(self.label):
        #     # print(c)
        #     color = ['red', 'green', 'blue', 'yellow', 'orange', 'brown', 'purple', 'pink', 'gray', 'olive', 'cyan'][c]
        #     # X_class = self.X[self.data == c]
        #     # print(X_class)
        #     mask = (self.label == c)
        #     X_label[mask] = mode(self.label[mask])[0]
        #     X_class = self.X[X_label]
        # print(self.X[:, 0])

        # Scatter 3D plot
        ax.scatter(proj_data[:, 0], proj_data[:, 1], proj_data[:, 2], color=colormap[self.labels.astype(int)], alpha=0.6)
            
        # chart junk
        plt.title("First 3 Primary Components of MNIST")
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_zlabel('PC3')
        plt.show()


    def apply(self, data, labels):
        self.data = self.standardization(data)
        self.labels = labels

        # Set the mean of the data to zero (move all points to such that the mean = 0)
        # self.mean = np.mean(data, axis=0)
        # self.data = self.data - self.mean
        
        self.N = self.data.shape[0]
        
        print("Calculating covariance matrix...")
        # Calculate the covariance matrix
        self.cov = np.dot(np.transpose(self.data), np.conj(self.data)) / (self.N - 1)
        print("Shape of cov mat: ",self.cov.shape)

        print("Calculating eigenvalues and vectors")
        # Get eigen values and eigen vectrs
        self.eigen_val, self.eigen_vec = np.linalg.eig(self.cov)       

        reduced_data = self.sort_and_reduce()

        self.plot(reduced_data)

        self.eigen_val, self.eigen_vec = eigen_decomposition(self.cov)
        reduced_data = self.sort_and_reduce()
        self.plot(reduced_data)

def main():
    print("loading data...")
    data, labels= load_data()

    dim = 3
    print(data.shape, "data loaded.")
    
    pca = PCA(dim)
    pca.apply(data, labels)

if __name__ == "__main__":
    main()
