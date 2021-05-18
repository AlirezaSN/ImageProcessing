# -*- coding: utf-8 -*-

'''
Exam - Q1 - Alireza Sadeghi Nasab
'''

# imports
import sys
import cv2
import numpy as np
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

    image = load_image('cat.png')

    if is_not_loaded_properly(image):
        print('image not loaded properly ... exiting program')
        sys.exit()

    if is_grayscale(image):
        print('image is grayscale. please load a colorful image ... exiting program')
        sys.exit()

    height, width = image.shape[:2]

    #1
    dst_image = cv2.resize(image, None, fx=0.5, fy=2.0, interpolation=cv2.INTER_AREA)

    #2
    M1 = np.float32([[1, 0, 100], [0, 1, -100]])
    dst_image_2 = cv2.warpAffine(image, M1, (width, height))

    #3
    M2 = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 45, 1)
    dst_image_3 = cv2.warpAffine(image, M2, (width, height))

    #4
    images = {
        'original': image,
        'resized': dst_image,
        'transformed': dst_image_2,
        'rotated': dst_image_3
    }
    display_multiple_img(images, 2, 2)