import numpy as np
import random

class SimplifiedSMO:
    def __init__(self, C, tol, max_iter, ker="rbf", sigma = 1.0):
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
        print("X = ", self.X)
        self.b = 0
        m, n = self.X.shape
        self.alphas = np.mat(np.zeros((m, 1)))
        itr = 0
        while (itr < self.max_iter):
            changed_alpha = 0
            for i in range(m):
                f_i = float(np.multiply(self.alphas,self.y).T * (self.X * self.X[i,:].T))+self.b
                print(f_i)
                E_i = f_i - float(self.y[i])
                #print("E_i = ",E_i)
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
                    #print("L", L)
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
                    if( abs(self.alphas[j] - alpha_j_old) < 0.00001):
                        continue
                    self.alphas[i] += self.y[j] * self.y[i] * (alpha_j_old - self.alphas[j])
                    b1 = self.b - E_i - self.y[i, :] * (self.alphas[i] - alpha_i_old) * (self.X[i, :] * self.X[i, :].T) - self.y[j] * (self.alphas[j] - alpha_j_old) * (self.X[i, :] * self.X[j, :].T) 
                    b2 = self.b - E_j - self.y[i] * (self.alphas[i] - alpha_i_old) * (self.X[i, :] * self.X[j, :].T) - self.y[j] * (self.alphas[j] - alpha_j_old) * (self.X[j, :] * self.X[j, :].T) 
                    #print("b1 = ", b1)
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
        print("b :", self.b)
        print("alphas: ", self.alphas)
    def predict_RBF(self, tX, ty,k1=1.3):
        m, n = tX.shape
        errorCount = 0
        for i in range(m):
            kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', k1))
            predict = kernelEval.T * multiply(labelSv, svm.alphas[svInd]) + svm.b
            if sign(predict) != sign(labelArr[i]): errorCount += 1
        print("the training error rate is : %f" % (errorCount / m))
    
    def predict(self, tX, ty):
        m, n = self.X.shape
        sv_idx = np.nonzero(self.alphas.A > 0)[0]
        svs = self.X[sv_idx]
        sv_label = self.y[sv_idx]
        
        c_count = 0
        for i in range(m):
            k_val = self.kernelTrans(svs, self.X[i, :])
            predict = k_val.T * np.multiply(sv_label, self.alphas[sv_idx]) + self.b
            if np.sign(predict) == np.sign(self.y[i]):
                c_count += 1
        acc = float(c_count) / m
        return acc


if __name__ == "__main__":    
    
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
    import pandas as pd

    # homedir = os.getcwd()#Get the path of the current file
    smo=SimplifiedSMO(C=0.6,tol=0.001,max_iter=50, ker='linear')#transfer method

    data, label = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state = 0)

    dataArr, tX, labelArr, ty = train_test_split(data, label, test_size=0.33, random_state = 0)

    # print(y)

    labelArr = np.where(labelArr == 0, -1, 1)

    # dataArr,labelArr = smo.loadDataSet(homedir+'/testSet.txt')
    print(dataArr)
    smo.fit(dataArr, labelArr)

    acc = smo.predict(tX, ty)
    
    #acc = accuracy_score(ty, predictions)
    print("accuracy = ", acc)
    
    #model = SVC(kernel='linear', C=1E10)
    #model.fit(dataArr, labelArr)
    #yfit = model.predict(tX)

    #a = accuracy_score(ty, yfit)

    #print("SVC acc:", a)
