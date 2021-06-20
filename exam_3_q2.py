# -*- coding: utf-8 -*-

'''
Exam - Q2 - Alireza Sadeghi Nasab
1400/3/30
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

def skin_detector_hsv(bgr_image, lower_hsv, upper_hsv):
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    skin_region = cv2.inRange(hsv_image, lower_hsv, upper_hsv)
    return skin_region

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

    lower_hsv = np.array([0, 50, 0], dtype='uint8')
    upper_hsv = np.array([120, 150, 255], dtype='uint8')

    detected_skin = skin_detector_hsv(image, lower_hsv, upper_hsv)
    result = cv2.cvtColor(detected_skin, cv2.COLOR_GRAY2BGR)

    images = {
        'original': image,
        'skin_segmented': result
    }

    display_multiple_img(images, 1, 2)