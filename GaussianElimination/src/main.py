# Implements Gaussian Elimination

def naive_gaussian_elimination(A, b):
    '''
        naive_gauss_elimination(A, b)

    Given a matrix A, converts A into upper-triangular matrix U using Gaussian Elimination.
    This implementation is "naive" because it *never re-orders the rows*.
    (It will obviously fail if a zero pivot is encountered.)
    '''
    # To avoid changing A
    U = A.copy()
    B = b.copy()

    print(U)
    print("Result from Naive Gaussian Elimination")
    
    for col in range(U.shape[1]):
        for row in range(col+1, U.shape[0]):
            if U[row, col] == 0:
                print("Error: Zero pivot detected!")
                break
            factor = -U[row][col] / U[col][col]
            U[row, :] = U[row, :] + (U[col, :] * factor)
            B[row] = B[row] + (B[col] * factor)
            print(U)
    return U, B


def gaussian_elimination(A, b):
    '''
        gauss_elimination(matrix A, matrix b)
    
    For Ax = b, converts A into upper-triangular matrix U using Gaussian Elimination.
    Swaps and continues if pivot is zero.
    '''
    # To avoid changing A
    U = A.copy()
    B = b.copy()
    
    print(U)
    print("Result from Gaussian Elimination")
    for col in range(U.shape[1]):
        # Check if the pivot is zero
        if( U[col, col] == 0 ):
            # Compare all the values in that column and 
            # swap with maximum one.
            for i in range(col+1, U.shape[1]):
                i_max = np.argmax(np.abs(U[:, i]))
                U[[col, i_max]] = U[[i_max, col]]
                B[[col, i_max]] = B[[i_max, col]]

        for row in range(col+1, U.shape[0]):
            factor = -U[row][col] / U[col][col]
            U[row, :] = U[row, :] + (U[col, :] * factor)
            B[row] = B[row] + (B[col] * factor)
            print(U)
    return U,B


def back_substitution(A,b):
    n = b.size
    sol = np.zeros(n)            
    # Solve for the end of the equation
    sol[n-1] = b[n-1]/A[n-1,n-1]
    # Loop from end to beginning
    for i in range(n-2,-1,-1):     
        sum_ = 0
        for j in range(i+1,n):        
            sum_ = sum_ + A[i,j]*sol[j]
        sol[i] = (b[i] - sum_)/A[i,i]
    return sol

if __name__ == "__main__":
    import numpy as np
 
    A = np.array([[1, 3, 1, 5],
                    [2, 15, 25, 25],
                    [2, 6, -1, 7],
                    [3, 11, 15, 9]])
    b = np.array([9, 1, 35, 7])
    G,B = gaussian_elimination(A, b)

    print(back_substitution(G, B))
