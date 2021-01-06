# References
# http://cs229.stanford.edu/materials/smo.pdf   
# http://fourier.eng.hmc.edu/e176/lectures/ch9/node9.html

import numpy as np
import random
from tqdm import tqdm

class SimplifiedSMO:
    ''' Simplified version of Sequential Minimal Optimization (SMO)
    '''
    def __init__(self, C, tol, max_iter=100, ker="rbf", sigma = 1.0):
        ''' init
        :param C:regularzation parameter
        :param tol: numerical tolerance
        :param max_iter: max number of times to iterate over alpha's without changing
        :param ker: Kernerl to be used, availabel: 'rbf', 'linear'
        :param sigma:
        '''
        self.tol = tol
        self.max_iter = max_iter
        self.C = C
        self.ker = ker
        self.sigma  = sigma

    def getRandomJ(self, i , m):
        j = i
        while (j == i):
            j = int(random.uniform(0, m))
        return j

    def clip_alpha(self, a_j, H, L):
        if a_j > H:
            a_j = H
        if a_j < L:
            a_j = L
        return a_j
    
    def kernelTrans(self, X, sample_x):
        ''' Kernel function
        :param X: input data
        :param sample_x: n-D vector
        :returns: matrix of (m, 1) size. 
        '''
        m = X.shape[0]
        K = np.mat(np.zeros((m, 1)))
        if self.ker == "linear":
            K = X * sample_x.T

        elif self.ker == "rbf":
            # To prevent divide by zero
            if self.sigma == 0:
                self.sigma = 1
            for i in range(m):
                #print("s shape: ", sample_x.shape)
                #print("X shape:", X[i, :].shape)
                diff = X[i, :] - sample_x
                K[i] = np.exp(diff * diff.T / (-2.0 * self.sigma ** 2))
                #K[i] = np.exp(-self.sigma * np.linalg.norm(X[i, :] - sample_x))
                #print("K shape", K[i].shape)

        elif self.ker == "polynomial":
            K = np.dot(X, sample_x.T) ** 3 
        else:
            raise NameError('Not supported type! Please use rbf or linear.')
        return K

    def fit(self, data, label):
        self.X = np.mat(data)
        self.y = np.mat(label).T
        # print("X = ", self.X)
        # initialize bias
        self.b = 0.0
        m, n = self.X.shape
        self.alphas = np.mat(np.zeros((m, 1)))
        itr = 0
        while (itr < self.max_iter):
            changed_alpha = 0
            #print("Iteration: ", itr)
            for i in range(m):
                f_i = float(np.multiply(self.alphas,self.y).T * (self.X * self.X[i,:].T))+self.b
                # print(f_i)
                E_i = f_i - float(self.y[i])
                #print("E_i = ",E_i)

                # KKT violation check
                if( ((self.y[i] * E_i < -self.tol) and (self.alphas[i] < self.C)) or ((self.y[i] * E_i) > self.tol) and (self.alphas[i] > 0) ):
                    j = self.getRandomJ(i, m)
                
                    f_j = float(np.multiply(self.alphas, self.y).T * (self.X * self.X[j, :].T)) + self.b 
                    E_j = f_j - float(self.y[j])
                    
                    alpha_i_old = self.alphas[i].copy()
                    alpha_j_old = self.alphas[j].copy()

                    if(self.y[i] != self.y[j]):
                        L = max(0, self.alphas[j] - self.alphas[i])
                        H = min(self.C, self.C + self.alphas[j] - self.alphas[i])
                    else:
                        L = max(0, self.alphas[j] + self.alphas[i] - self.C)
                        H = min(self.C, self.alphas[j] + self.alphas[i])
                    
                    # skip when L==H
                    if L == H:
                        #print('L == H')
                        continue
                    
                    eta = 2.0 * self.X[i, :] * self.X[j, :].T - self.X[i, :] * self.X[i, :].T - self.X[j, :] * self.X[j, :].T
                    if eta >= 0:
                        #print('eta >= 0')
                        continue
                    
                    #self.alphas[j] -= self.y[j] * (alpha_j_old - self.alphas[j]) / eta
                    self.alphas[j] -= self.y[j] * (E_i - E_j) / eta
                    self.alphas[j] = self.clip_alpha(self.alphas[j], H, L)

                    # skip if no change
                    if( abs(self.alphas[j] - alpha_j_old) < self.tol):
                        continue
                    
                    # find alpha i
                    self.alphas[i] += self.y[j] * self.y[i] * (alpha_j_old - self.alphas[j])
                    b1 = self.b - E_i - self.y[i, :] * (self.alphas[i] - alpha_i_old) * (self.X[i, :] * self.X[i, :].T) - self.y[j] * (self.alphas[j] - alpha_j_old) * (self.X[i, :] * self.X[j, :].T) 
                    b2 = self.b - E_j - self.y[i] * (self.alphas[i] - alpha_i_old) * (self.X[i, :] * self.X[j, :].T) - self.y[j] * (self.alphas[j] - alpha_j_old) * (self.X[j, :] * self.X[j, :].T) 
                    
                    if(0 < self.alphas[i]) and (self.C > self.alphas[i]):
                        self.b = b1
                    elif (0 < self.alphas[j]) and (self.C > self.alphas[j]):
                        self.b = b2
                    else:
                        self.b = (b1 + b2)/2.0
                    
                    changed_alpha += 1
            if(changed_alpha == 0):
                itr += 1
            else:
                itr = 0
        #print("b :", self.b)
        #print("alphas: ", self.alphas)
    # def predict_RBF(self, tX, ty,k1=1.3):
    #     m, n = tX.shape
    #     errorCount = 0
    #     for i in range(m):
    #         kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', k1))
    #         predict = kernelEval.T * multiply(labelSv, svm.alphas[svInd]) + svm.b
    #         if sign(predict) != sign(labelArr[i]): errorCount += 1
    #     print("the training error rate is : %f" % (errorCount / m))
    
    def predict(self, tX):
        m, n = tX.shape

        # Support vector are the vectors having alphas > 0
        sv_idx = np.nonzero(self.alphas.A > 0)[0]
        svs = self.X[sv_idx]
        sv_label = self.y[sv_idx]

        p = []
        for i in range(m):
            k_val = self.kernelTrans(svs, tX[i, :])
            predict = k_val.T * np.multiply(sv_label, self.alphas[sv_idx]) + self.b
            p.append(predict)

        arr = np.ravel(p)
        # for each array get the sign and return the array
        return np.array([np.sign(x) for x in arr])

if __name__ == "__main__":    
    
    from sklearn.model_selection import train_test_split
    # from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
    from itertools import combinations
    import json
    from scipy.stats import mode
    
    # data, label = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state = 0)

    print("Loading data and labels...")
    data = np.load('data/emb.npy')
    label = np.load('data/label.npy')

    # profiles = json.load(open('data/profiles.json'))
    # data_f = pd.DataFrame(profiles['data'])
    # AI_df = data_f.loc[data_f['department'] == 'Artificial Intelligence']
    # AI_id = AI_df['id'].to_numpy()
    # department = data_f['department'].to_numpy()

    # print(np.unique(label))
    
    # Testing on subset of data
    # data = data[:7000]
    # label = label[:7000]
    
    print(data.shape)
    print(label.shape)
    
    # Test train split
    x_train, tX, y_train, ty = train_test_split(data, label, test_size=0.2, random_state = 0)

    # x_train = data
    # y_train = label
    # ty = label[AI_id]
    # tX = data[AI_id]
    
    print('Train data shape:', x_train.shape)
    print('Test data shape:', tX.shape)

    print('Creating dataset...')

    # Create dataset
    training_data = []
    # get class pair: the combination of train label in list
    class_pairs = list(combinations(set(y_train), 2))
    for class_pair in class_pairs:
        class_mask = np.where((y_train == class_pair[0]) | (y_train == class_pair[1]))
        y_i = np.where(y_train[class_mask] == class_pair[0], 1, -1)
        training_data.append((x_train[class_mask], y_i))

    print("Fitting data...")
    
    # One-against-one
    # we train one classifier per pair of classes, 
    # which leads to K(K-1)/2 classifiers for K classes
    classifiers = []
    for data in tqdm(training_data):
        # smo = SVC(C=0.6,tol=0.001)
        smo = SimplifiedSMO(C=0.6,tol=0.0001)
        smo.fit(data[0], data[1])
        classifiers.append(smo)

    # Each example we wish to predict is passed to each classifier, 
    # and the predicted class is recorded. Then, the class having 
    # the most votes is assigned to the example.
    def predict_class(X, classifiers, class_pairs):
        predictions = np.zeros((X.shape[0], len(classifiers)))
        for idx, clf in enumerate(classifiers):
            class_pair = class_pairs[idx]
            prediction = clf.predict(X)
            predictions[:, idx] = np.where(prediction == 1,
                                            class_pair[0], class_pair[1])
        return mode(predictions, axis=1)[0].ravel().astype(int)

    print('Predicting...')
    # Predict
    y_predict = predict_class(tX, classifiers, class_pairs)
    # print(np.isin(y_predict, AI_id))
    
    # print(department[y_predict])
    print("True Label: ", ty)
    print("Predicted label: ", y_predict)
    print("Accuracy: ", accuracy_score(ty,y_predict))

    
