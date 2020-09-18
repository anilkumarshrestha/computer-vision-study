# Subtract a 1d array from the 2d array, such that each item of 1d array subtracts from respective row of 2d-array

if __name__ == "__main__":
    import numpy as np

    one_dim = np.random.randint(255, size = 10)
    two_dim = np.random.randint(255, size = (2,10))

    print("1D array: \n", one_dim)
    print(one_dim.shape)
    
    print("2D array: \n", two_dim)
    print(two_dim.shape)

    # Directly subtract 1D array from 2D 
    # using numpy which uses broadcasting.
    # This gives array of shape 2 by 10.
    print("2D - 1D : \n", two_dim - one_dim)
    
    # Using np.newaxis
    print("2D - 1D using newaxis: \n", two_dim - one_dim[np.newaxis, :])
