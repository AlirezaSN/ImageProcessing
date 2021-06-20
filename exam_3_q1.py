# -*- coding: utf-8 -*-

'''
Exam - Q1 - Alireza Sadeghi Nasab
1400/3/30
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

def build_kernel(kernel_type, kernel_size):
    if kernel_type == cv2.MORPH_ELLIPSE:
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    elif kernel_type == cv2.MORPH_CROSS:
        return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
    else:
        return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

def dilate(image, kernel_type, kernel_size):
    kernel = build_kernel(kernel_type, kernel_size)
    dilation = cv2.dilate(image, kernel, iterations=1)
    return dilation

def closing(image, kernel_type, kernel_size):
    kernel = build_kernel(kernel_type, kernel_size)
    clos = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return clos

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

    if len(sys.argv) < 2:
        print('invalid input')
        sys.exit()
    else:
        image_addr = sys.argv[1]

    image = load_image(image_addr, is_grayscale=False)

    if is_not_loaded_properly(image):
        print('image not loaded properly ... exiting program')
        sys.exit()

    kernel_size_3_3 = (3, 3)

    result_1 = dilate(image, cv2.MORPH_CROSS, kernel_size_3_3)
    result_2 = closing(image, cv2.MORPH_CROSS, kernel_size_3_3)

    images = {
        'original': image,
        'dialate': result_1,
        'closing': result_2
    }

    display_multiple_img(images, 1, 3)
