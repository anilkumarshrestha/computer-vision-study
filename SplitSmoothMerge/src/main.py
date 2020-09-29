#!/usr/bin/env python3
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import os, argparse
from PIL import Image
from scipy.ndimage.filters import convolve

def get_gaussian_kernel(size=5, sigma=1):
    
    # for 5x5 kernel, values range from 5//2 = -2 to 2
    # -2 -1 0 1 2
    x = np.linspace(- (size // 2), size // 2, size)
    xx, yy = np.meshgrid(x, x)

    normalization_const =  2 * np.pi * np.square(sigma)
    xx = np.square(xx)
    yy = np.square(yy)
    g_kernel = np.exp(-0.5 * (xx + yy) / np.square(sigma))
    g_kernel /= normalization_const
    return g_kernel/np.sum(g_kernel)

def split_gauss_merge(img):
    r,g,b = img.split()

    k1 = get_gaussian_kernel()
    k2 = get_gaussian_kernel(5, 2)
    k3 = get_gaussian_kernel(5, 3)
    
    r_blur = convolve(r, k1)
    g_blur = convolve(g, k2)
    b_blur = convolve(b, k3)

    merged = Image.merge('RGB', (r_blur, g_blur, b_blur))
    merged.show() 

def main():
    parser = argparse.ArgumentParser(description='Split given image and apply gaussian kernel')
    parser.add_argument('--image', dest='img', required=True, help="Image")
   
    args = parser.parse_args()

    img = Image.open(args.img)
    split_gauss_merge(img)

    k1 = get_gaussian_kernel()
    k2 = get_gaussian_kernel(5, 2)
    k3 = get_gaussian_kernel(5, 3)
    
if __name__ == "__main__":
    main()
