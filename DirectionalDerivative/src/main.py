#!/usr/bin/env python3
import numpy as np
import argparse
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.2126, 0.7152, 0.0722])

def directionalDer(img, dir_):
    '''
    '''
    if(dir_ == 'x'):
        Gx = np.array([[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]])
        #print(Gx.shape)
        convolved = convolve2D(img, Gx)
    elif(dir_ == 'y'):
        Gy = np.array([[-1, -2, -1], [0, 0, 0], [+1, +2, +1]])
        convolved = convolve2D(img, Gy)

    return convolved

def convolve2D(img, kernel):
    '''Convolve image and kernel
    :param img: Image to be convolved (Numpy array)
    :param kernel: Kernel to convolve
    :returns: convolved Numpy Array
    '''
    kernel = np.flipud(np.fliplr(kernel))

    padded_img = np.pad(img,((2,2), (2,2)), mode='minimum')
    output = np.zeros_like(img)
    step = kernel.shape[0]
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            # multiplication of the kernel and the image
            output[y, x]=(kernel * padded_img[y: y+step, x: x+step]).sum()
            # print(output[y, x])
    return output

def get_magnitude(x, y):
    return np.sqrt(np.square(x) + np.square(y))

def normalize(img):
    img = img/np.max(img)
    return img

def show(img, name):
    plt.imshow(img, cmap = plt.get_cmap('gray'))
    plt.show()
    plt.imsave(name, img, cmap='gray')

def main():
    parser = argparse.ArgumentParser(description='Directional derivative in X and Y direction.')
    parser.add_argument('--image', dest='img', required=True, help='Image')

    args = parser.parse_args()
    
    img = mpimg.imread(args.img)
    grey = rgb2grey(img)
    
    show(grey, 'originalImage.png')
    x_direction = directionalDer(grey, 'x')
    y_direction = directionalDer(grey, 'y')
    mag = get_magnitude(x_direction, y_direction)
    
    show(x_direction, 'x_dir.png')
    show(y_direction, 'y_dir.png')
    show(mag, 'mag.png')

if __name__ == '__main__':
    main()
