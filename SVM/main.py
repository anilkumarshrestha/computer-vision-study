import numpy as np
import pandas as pd
import random 
import json
import timeit

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA 
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

import matplotlib.pyplot as plt
import seaborn as sns

from simplified_SMO import SimplifiedSMO

data = json.load(open('profiles.json'))
data_f = pd.DataFrame(data['data'])

print(data_f)


print("Loading data and  labels...")
data = np.load('data/emb.npy')
label = np.load('data/label.npy')

print('Data shape: ', data.shape)

# split the given data and label into test and train data/label
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size = 0.4)
print('Train data shape:', x_train.shape)
print('Test data shape:', x_test.shape)

pca = PCA(n_components=5, whiten=True, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca, svc)

param_grid = {'svc__C': [1, 5, 10, 50],
                'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]}
grid = GridSearchCV(model, param_grid)
print("grid ready")

s = timeit.timeit()
grid.fit(x_train, y_train)
e = timeit.timeit()
print("Time:", s - e)

print(grid.best_params_)

model = grid.best_estimator_
yfit = model.predict(x_test)
print("Acc:", accuracy_score(y_test, yfit))
mat = confusion_matrix(y_test, yfit)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar = False)
plt.xlabel('true label')
plt.ylabel('predicted label')

