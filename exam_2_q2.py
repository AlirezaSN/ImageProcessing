# -*- coding: utf-8 -*-

'''
Exam - Q2 - Alireza Sadeghi Nasab
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

    #1
    image = load_image('cat.png')

    if is_not_loaded_properly(image):
        print('image not loaded properly ... exiting program')
        sys.exit()

    if is_grayscale(image):
        print('image is grayscale. please load a colorful image ... exiting program')
        sys.exit()

    #2
    image_filtered = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(image_filtered, cv2.COLOR_BGR2GRAY)
    gradient_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0, 3)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1, 3)
    abs_gradient_x = cv2.convertScaleAbs(gradient_x)
    abs_gradient_y = cv2.convertScaleAbs(gradient_y)

    #3
    sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

    #4
    images = {
        'original': image,
        'gradient_x': cv2.cvtColor(abs_gradient_x, cv2.COLOR_GRAY2BGR),
        'gradient_y': cv2.cvtColor(abs_gradient_y, cv2.COLOR_GRAY2BGR),
        'sobel_output': cv2.cvtColor(sobel_image, cv2.COLOR_GRAY2BGR)
    }
    display_multiple_img(images, 2, 2)