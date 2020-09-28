#!/usr/bin/env python3

import numpy as np
import os, argparse, time
from PIL import Image
import matplotlib.pyplot as plt
#from random import shuffle

def create_mosaic(images, row, col):
    '''Creates mosaic.

    :param images: list of numpy arrays.
    :param row: number of images in mosaic rows.
    :param col: number of images in mosaic cols.
    
    :returns: numpy array
    '''
    
    width = row
    i = 0
    row_to_stack = []
    for j in range(col):
        rx = np.hstack([images[x] for x in range(i, row)])
        row_to_stack.append(rx) 
        if j + 1 == col:
            final = np.vstack(row_to_stack)
        else:
            i = row
            row += width
    return final
    #final = np.hstack([images[0], images[1]])
    #plt.imshow(r)
    #plt.show()


def crop_image(img):
    '''Crop the given image square.
    
    :param img: An image object.
    :returns: An sqaure image.
    '''

    print('Cropping image...')
    if img.width > img.height:
        new_width = img.height
        new_height = img.height

        start_x = (img.width - img.height) / 2
        start_y = 0

        img = img.crop((
            start_x,
            start_y,
            start_x + new_width,
            start_y + new_height,
        ))
    elif img.height > img.width:
        new_width = img.width
        new_height = img.width

        start_x = 0
        start_y = (img.height - img.width) / 2

        img = img.crop((
            start_x,
            start_y,
            start_x + new_width,
            start_y + new_height,
        ))

    return img

def get_image(dir_path, dim, rand, crop, size):
    '''Get all the images in given directory

    :param dir_path: Path of the folder containing all images.
    :param dim: Dimension to which image will be resized.
    
    :returns: list
    '''

    # list all files in given path
    file_list = os.listdir(dir_path)
    src_images = []
    im_type = ('.jpg','.png', 'jpeg', '.tiff', '.raw')
    for file_ in file_list:
        abs_path = os.path.abspath(os.path.join(dir_path, file_))
        if abs_path.lower().endswith(im_type):
            im = Image.open(abs_path).convert('RGB')

            if crop:
                im = crop_image(im)

            im = im.resize((dim,dim))
            im_arr = np.asarray(im)
            src_images.append(im_arr)
            
            #print(im_arr[2])
            #r = [(d[0], 0, 0) for d in im]
            #g = [(0, d[1], 0) for d in im]
            #b = [(0, 0, d[2]) for d in im]
            #print(r,g,b)
            #im.close()
        else:
            print('Extension Error:', abs_path)
    #if rand:
    #    shuffle(src_images)
    #else:
    #   return src_images
    if len(src_images) < size:
        print('Error: Could not create Mosaic')
        print('{} more images required for given shape.'.format(size - len(src_images)))
        exit(0)
    return src_images


def get_RGB(img):
    '''Get RGB channel
    :param img: Numpy array.

    :returns: Three numpy arrays.
    '''
    #r = img[:,:,0]
    #g = img[:,:,1]
    #b = img[:,:,2]
    r = np.zeros(img.shape, dtype='uint8')
    g = np.zeros(img.shape, dtype='uint8')
    b = np.zeros(img.shape, dtype='uint8')
    
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    return r, g, b 

def plot_save(img, name):
    plt.imsave(name, img)
    plt.imshow(img)
    plt.show()

def main():
   
    parser = argparse.ArgumentParser(description='Creates Mosaic from given images')
    parser.add_argument('--dir', dest='dir', required=True, help="Image directory")
    parser.add_argument('--shape', nargs=2, dest='shape', required=True, type= int, help='Shape of Mosaic to be created. 4,6 or 12,2 and so on.')
    parser.add_argument('--d', dest='dim',type=int, help='custom size of the image in mosaic') 
    parser.add_argument('-r', dest='rand', type= bool, help='Randomize the image [True, False]')
    parser.add_argument('--crop', dest='crop', type=bool, help='Crops images [True, False]')
    
    args = parser.parse_args()
    
    if args.dim:
        dim = args.dim
    else:
        dim = 200
    
    mos_size = args.shape[0] * args.shape[1]

    print('Getting images...')
    start = time.time()
    images = get_image(args.dir, dim, args.rand, args.crop, mos_size)
    print('Creating Mosaic...')
    final_image = create_mosaic(images, args.shape[0], args.shape[1])
    print(time.time() - start)
    
    r, g, b = get_RGB(final_image)

    plot_save(final_image, 'result.png')
    plot_save(r, 'r.png')
    plot_save(g, 'g.png')
    plot_save(b, 'b.png')
    print('Complete')

if __name__ == "__main__":
    main()
