#!/usr/bin/env python3
import numpy as np
import argparse
from PIL import Image
from scipy.ndimage.filters import convolve

def get_gaussian_kernel(size=5, sigma=1):
    '''Creates 2D Gaussian Kernel
    :param size: Size of the required 2D Gaussian Kernel
    :param sigma: Standard deviation
    :returns: Numpy Array of 2D Gaussian Kernel

    '''
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

def convolve2D(img, kernel):
    '''Convolve image and kernel
    :param img: Image to be convolved (Numpy array)
    :param kernel: Kernel to convolve
    :returns: convolved Numpy Array
    '''
    kernel = np.flipud(np.fliplr(kernel))

    padded_img = np.pad(img,((4,4), (4,4)), mode='minimum')
    output = np.zeros_like(img)
    step = kernel.shape[0] 
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            # multiplication of the kernel and the image
            output[y, x]=(kernel * padded_img[y: y+step, x: x+step]).sum()

    return output

def split_gauss_merge(img):
    '''Splits given image, convolves with kernel having 
    different standard deviation and finally merges the image.

    :param img: Image to process (PIL)
    :returns: Merged image
    '''

    print("Splitting channels...")
    r,g,b = img.split()

    # Get kernel
    k1 = get_gaussian_kernel(5, 15)
    k2 = get_gaussian_kernel(5, 20)
    k3 = get_gaussian_kernel(5, 17)
    
    print("Convolving...")
    # Convolve using scipy
    r_blur = convolve(r, k1)
    g_blur = convolve(g, k2)
    b_blur = convolve(b, k3)
   
    # Convolve using scratch method
    r_conv = convolve2D(np.array(r), k1)
    b_conv = convolve2D(np.array(b), k2)
    g_conv = convolve2D(np.array(g), k3)
    
    #print(type(r_blur))
    #print(type(r_conv))
    
    # Merge
    print("Mering...")
    merged = Image.merge('RGB', (Image.fromarray(r_blur), Image.fromarray(g_blur), Image.fromarray(b_blur)))
    merged_conv = Image.merge('RGB', (Image.fromarray(r_conv), Image.fromarray(g_conv), Image.fromarray(b_conv)))

    return merged, merged_conv

def main():
    parser = argparse.ArgumentParser(description='Split given image and apply gaussian kernel')
    parser.add_argument('--image', dest='img', required=True, help="Image")
   
    args = parser.parse_args()
    
    print("Getting image...")
    img = Image.open(args.img)

    merged, merged_conv = split_gauss_merge(img)

    img.show()
    merged.show()
    merged_conv.show()
    merged.save('with_scipy.png')
    merged_conv.save('scratch.png')
    print("Complete.")

if __name__ == "__main__":
    main()
