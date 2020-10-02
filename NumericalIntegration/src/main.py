#!/usr/bin/env python3

import numpy as np

def f(x):
    return 3*(x**2)*np.exp(x**3)

def trapezoidal(a, b, n):
    '''Numerical integration using trapezoidal method

    :param a,b: interval [a, b]
    :param n: number of intervals
    :returns: Integrated value
    '''
    h = float(b-a)/n
    x = np.linspace(a, b, n+1)
    s = np.sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

def mid_point_vec(a, b, n):
    '''Numerical integration using midpoint method

    :param a,b: interval [a, b]
    :param n: number of intervals
    :returns: Integrated value
    '''
    h = float(b-a)/n
    # n uniformally distributed mid-point coordinates between a+h/2 and b-h/2
    x = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(f(x))

def main():
    print("Using Mid-point method: ", mid_point_vec(0, 1, 100))
    print("Using Trapezoidal method: ", trapezoidal(0, 1, 100))

if __name__ == "__main__":
    main()
