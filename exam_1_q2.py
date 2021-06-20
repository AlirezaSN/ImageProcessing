# -*- coding: utf-8 -*-

'''
Exam - Q2 - Alireza Sadeghi Nasab
'''

# imports
import sys
import cv2

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

def show_image(image, image_name):
    cv2.imshow(image_name, image)

################################################################################

if __name__ == "__main__":

    #1
    image1 = load_image('leaf-noise.png', is_grayscale=False)
    if is_not_loaded_properly(image1):
        print('image1 is not loaded properly ... exiting program')
        sys.exit()

    #2
    image2 = load_image('lenna.png', is_grayscale=True)
    if is_not_loaded_properly(image2):
        print('image2 is not loaded properly ... exiting program')
        sys.exit()

    #3
    show_image(image1, '1')
    show_image(image2, '2')
    cv2.waitKey(0)
    cv2.destroyAllWindows()