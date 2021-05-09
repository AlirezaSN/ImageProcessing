# -*- coding: utf-8 -*-

'''
Exam - Q1 - Alireza Sadeghi Nasab
'''

# imports
import sys
import cv2
import matplotlib.pyplot as plt

################################################################################

def load_image(path, is_grayscale=False):
    if is_grayscale:
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        return cv2.imread(path)

def is_not_loaded_properly(image):
    if (image is None) or (image.size == 0):
        return True
    else:
        return False

def is_grayscale(image):
    dimensions = image.shape
    if len(dimensions) < 3:
        return True
    if len(dimensions) == 3:
        return False

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def print_properties(image, title):
    height, width = image.shape[:2]
    pixels = image.size
    dtype = image.dtype
    print('######## {} properties ########'.format(title))
    print('height -> ', height)
    print('width -> ', width)
    print('number of pixels -> ', pixels)
    print('type -> ', dtype)
    print('##########################')

def modify_rows_columns_pixels(image, rows, columns, new_value):
    for i in range(rows[0], rows[1]):
        for j in range(columns[0], columns[1]):
            image[i][j] = new_value

def show_image(image, image_name):
    cv2.imshow(image_name, image)

def display_multiple_img(images, rows=1, cols=1):
    figure, ax = plt.subplots(nrows=rows, ncols=cols)
    for ind,title in enumerate(images):
        if is_grayscale(images[title]): 
            ax.ravel()[ind].imshow(images[title], cmap=plt.get_cmap('gray'))
        else:
            ax.ravel()[ind].imshow(images[title])
        ax.ravel()[ind].set_title(title)
        ax.ravel()[ind].set_axis_off()
    plt.tight_layout()
    plt.show()

################################################################################

if __name__ == "__main__":

    #1
    if len(sys.argv) < 2:
        print('invalid input')
        sys.exit()
    else:
        image_addr = sys.argv[1]

        #2
        image = load_image(image_addr, is_grayscale=False)
        original_image = image.copy()

        if is_not_loaded_properly(image):
            print('image not loaded properly ... exiting program')
            sys.exit()

        #3
        print_properties(image, 'image')

        #4
        if is_grayscale(image):
            print('image is grayscale ... exiting program')
            sys.exit()
        else:
            channels_count = len(image.shape)
            print('image is colorful. image channels count: ', channels_count)

        #5
        gray_image = convert_to_grayscale(image)
        original_gray_image = gray_image.copy()

        #6
        print('pixel of x=10 and y=20 of colorful image: ', image[20, 10])
        print('pixel of x=10 and y=20 of grayscale image: ', gray_image[20, 10])

        #7
        modify_rows_columns_pixels(image, [50, 80], [100, 150], (255, 0, 0))

        #8
        modify_rows_columns_pixels(gray_image, [20, 100], [50, 70], 255)

        #9
        images = {
            'original_image': original_image,
            'original_gray_image': original_gray_image,
            'modified_image': image,
            'modified_gray_image': gray_image
        }
        display_multiple_img(images, 2, 2)
