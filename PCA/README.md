# PCA

Task Descriotion: Implement PCA and apply it for dimensinionaly reduction of mnist dataset to 3 Dimension (and visualize the result)

## Description

Principal Component Analysis (PCA) is a method for reducing dimension of data. As the number of dimension increases from three, it becomes almost impossible to view the data and here PCA does a good job in reducing the dimension capturing maximum variability of the dataset. It also makes the training of an algorithm faster by reducing the number of dimensions of data.

### Eigenvalues and eigenvectors

A vector $v$ is an eigenvector of A if transformation of the vector ($Av$) are in the same direction. Thus obtained vector is just the scaled version of the input vector. This scaling factor, $'\lambda'$ is the eigenvalue of A.

Mathematically,
$$'Av = \lambda v'$$

### Covariance
Standard deviation and variance only operates in 1D. And to measure the similar measure in 2D, we use covariance.
Mathematically,

$$'cov(X,Y) = \dfrac{\sum_{i=1}^{n} (X_i - \bar{X}) (Y_i - \bar{Y})}{(n - 1)}'$$

The covariance matrix looks like the following:

$$'C = \begin{pmatrix}
cov(x,x) & cov(x,y) & cov(x,z)\\
cov(y,x) & cov(y,y) & cov(y,z) \\
cov(z,x) & cov(z,y) & cov(z,z)
\end{pmatrix}'$$


### Method

1. Get data
2. Subtract the mean
3. Calculate the covariance matrix
4. Calculate the eigenvectors and eigenvalues of the covariance matrix
5. Choosing components and forming a feature vector
6. Deriving the new dataset

## Dependencies
```
    1. numpy
    2. mlxtend
    3. matplotlib
    4. tqdm
```
## Usage

        $ python src/main.py 

## Results
![result](res/result.png)
# References
1. A tutorial on Principal Components Analysis
 by Lindsay I Smith

2. [A Tutorial on Principal Component Analysis](https://arxiv.org/pdf/1404.1100.pdf)
3. [What is the intuitive relationship between SVD and PCA?](https://math.stackexchange.com/questions/3869/what-is-the-intuitive-relationship-between-svd-and-pca)
4. [Relationship between SVD and PCA. ](https://stats.stackexchange.com/questions/134282/relationship-between-svd-and-pca-how-to-use-svd-to-perform-pca)
5. [ML From Scratch](http://www.oranlooney.com/post/ml-from-scratch-part-1-linear)
6. [How to Calculate Principal Component Analysis (PCA) from Scratch in Python](https://machinelearningmastery.com/calculate-principal-component-analysis-scratch-python/)
7. [Eigendecomposition](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/)
8. [https://github.com/numpy/numpy/blob/v1.8.0/numpy/lib/function_base.py#L1648](https://github.com/numpy/numpy/blob/v1.8.0/numpy/lib/function_base.py#L1648)
