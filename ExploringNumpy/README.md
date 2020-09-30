# Exploring Numpy

Task description:
1. Study and understand `ufunc` and `vectorized operation`, `aggregation`, `broadcasting`, `fancy indexing` in Numpy and indexing

## The problem: Slowness of Loops
Using python default implementation does some operations like looping over arrays to operate on each element, very slowly. This is due to the dynamic, interpreted nature of the language. It takes several seconds to compute such an operation.

                for i in range(len(x)):
                        output[i] = 1 / values[i]

Here the bottleneck is the type-checking and function dispatches that CPython must do at each cycle of the loop. Each time the reciprocal is computed, python first examines the object's type and does a dynamic lookup of the correct function to use for that type.

## Introduction to UFuncs
In order to avoid the above mentioned problem, we can work in compiled code instead, where type specification would be known before the code is executed and the result could be computed much more efficiently. Numpy provides this convenient interface which is termed vectorized operation. This vectorized approach pushes the loop into the compiled layer that underlies Numpy, leading to much faster execution. Following line of code gives the same result as the above one but much faster and efficiently.

                values = 1 / values

## Exploring Numpy's UFuncs
Exists in unary and binary ufuncs.

### Array arithmetic

Operator | Equivalent ufunc | Description
---|---|---
|+ |np.add|Addition
|- |np.subtract|Subtraction
|- |np.negative|Unary negation (eg: -x)
|*| np.multiply|Multiplication
|/|np.divide|Division
|//|np.floor_divide|Floor division
|**|np.power|Exponential
|%|np.mod|Modulus/remainder

### Absolute value
Takes the absolute of all the elements in a numpy array. Also works for complex numbers.

                x = np.array([-1, 3, -7])
                np.abs(x)
                array([1, 3, 7])

                y = np.array([[3 - 4j, [0 + 1j]])
                np.abs(y)
                array([5., 1.])

### Trigonometric functions
To find trigonometric values of each element of a numpy array.

                np.sin(x)
                np.cos(x)
                np.tan(x)
                np.arcsin(x)
                np.arccos(x)
                np.arctan(x)

### Exponents and logarithms
To find logs and exponents of each element in a numpy array.

                np.exp(x)
                np.exp2(x)
                np.log(x)
                np.log2(x)
                np.log10(x)

### Specialized ufuncs
NumPy has many more ufuncs available, including hyperbolic trig functions, bitwise arithmetic,
comparison operators, conversions from radians to degrees, rounding and remainders, and much more.

## Some Advanced UFunc features
### Specifying output
Specifying output makes computation faster.

                y = np.zeros(10)
                np.power(2, x, out=y[::2])

By doing this instead of y[::2] = 2\**x, we avoid creation of temporary array to hold results of 2**x and copy those values to array y.

### Aggregates

To reduce an array with particular operation:

                x = np.arange(1,10)
                np.add.reduce(x)
                --> 45

To accumulate an array with particular operation:

                np.add.accumulate(x)
                array([1, 3, 6, 10, 15, 21, 28, 36, 45])

## Aggregations: Min, Max
Similarly, we should perform regular aggregation functions in arrays using numpy approach instead of default python to make computation faster.

### Summing the values in array

                np.sum(x)

### Minimum and Maximum

                np.min(x)
                np.max(x)

### Multi-dimensional aggregation

                x = np.random.random((2,3))
                x.sum()
                # To aggregate along Y-axis
                x.sum(axis=0)
                # To aggregate along X-axis
                x.sum(axis=1)

## Other aggregation functions

Function | NaN-safe version
---|---|---
np.sum|np.nansum|
np.prod|np.nanprod|
np.mean|np.nanmean|
np.std|np.nanstd|
np.var|np.nanvar|
np.min|np.nanmin|
np.max|np.nanmax|
np.argmin|np.nanargmin|
np.argmax|np.nanargmax|
np.median|np.nanargmedian|
np.percentile|np.nanpercentile|
np.any|-|
np.all|-|


## Broadcasting
Broadcasting is explained in previous issue [here](https://repo.ekbana.info/LearnMLBatchAugust2020/DLComputerVision/anil-shrestha/tree/master/SubtractWithBroadcast)


## Fancy Indexing
It is like simple indexing but here we pass arrays of indices in place of single scalars. This allows us to very quickly access and modify complicated subsets of an array's values.

                x = np.array([1, 2, 3, 4, 5, 6])
                i = [1, 3, 5]
                x[i]
                --> array([2, 4, 6])

As we can see here, the size of the result is actually the size of our index and values are the corresponding values of x at index i.

Similarly, for multidimensional arrays we can use fancy indexing,

                x = np.arange(9).reshape((3,3))
                --> array([[0, 1, 2],
                          [3, 4, 5],
                          [6, 7, 8]])
                r = np.array([0, 2])
                c = np.array([1, 2])
                x[r, c]
                --> array([[1, 8])
   Combining row and column vector within indices,

                x[r[:, np.newaxis], col]
                --> array([[1, 2],
                          [7, 8]])
It is always important to remember with fancy indexing that the return value reflects the broadcasted shape of the indices, rather than the shape of the array being indexed.

### Combined indexing
We can combine fancy indexing with simple indices, slicing, and masking.

                x[1, [1, 2]]
                x[1:, [2, 1]]

### Modifying values with fancy indexing
Fancy indexing can also be used to modify values in an array.

                x = np.arange(5)
                i = np.array([1, 2])
                x[i] = 7
                --> [0, 7, 7, 3, 4]

