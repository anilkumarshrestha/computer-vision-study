import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from svm_simple import SVM_simple

data, label = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05)

X, tX, y, ty = train_test_split(data, label, test_size=0.33)

# print(y)

y = np.where(y == 0, -1, 1)

clf = SVM_simple()
clf.fit(X, y)

predictions = clf.predict(tX)

acc = accuracy_score(ty, predictions)
print("accuracy = ", acc)

print(clf.w, clf.b)

def visualize_svm():
     def get_hyperplane_value(x, w, b, offset):
          return (-w[0] * x + b + offset) / w[1]

     fig = plt.figure()
     ax = fig.add_subplot(1,1,1)
     plt.scatter(X[:,0], X[:,1], marker='o',c=y)
     plt.scatter(tX[:,0], tX[:,1], marker='x',c=predictions)

     x0_1 = np.amin(X[:,0])
     x0_2 = np.amax(X[:,0])

     x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
     x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

     x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
     x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

     x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
     x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

     ax.plot([x0_1, x0_2],[x1_1, x1_2], 'y--')
     ax.plot([x0_1, x0_2],[x1_1_m, x1_2_m], 'k')
     ax.plot([x0_1, x0_2],[x1_1_p, x1_2_p], 'k')

     x1_min = np.amin(X[:,1])
     x1_max = np.amax(X[:,1])
     ax.set_ylim([x1_min-3,x1_max+3])

     plt.show()

visualize_svm()


###########################################
# from sklearn.svm import SVC
# clf = SVC(kernel='linear')
# clf.fit(X,y)
# y_pred = clf.predict(tX)
# print("Acc from sklearn = ", accuracy_score(ty,predictions))
##############################################