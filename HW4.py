# -*- coding: utf-8 -*-

'''
Homework - 4
'''

# imports
import sys
import cv2
import pathlib

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

def get_image_extension(image_addr):
    return pathlib.PurePath(image_addr).suffix

def swap_red_blue_channels(image):
    red = image[:,:,2].copy()
    blue = image[:,:,0].copy()
    image[:,:,0] = red
    image[:,:,2] = blue
    return image
    
def show_image(image, image_name):
    cv2.imshow(image_name, image)

def write_image_to_disk(path, image):
    cv2.imwrite(path, image)

################################################################################

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('invalid input')
        sys.exit()
    else:
        source_image_addr = sys.argv[1]

        original_image = load_image(source_image_addr, is_grayscale=False)

        if is_not_loaded_properly(original_image):
            print('images not loaded properly ... exiting program')
            sys.exit()

        if is_grayscale(original_image):
            print('image is grayscale. please pass colorful image')
            sys.exit()

        #swap
        wrong_image = swap_red_blue_channels(original_image)

        if wrong_image is None:
            print('swapping method does not work properly')
            sys.exit()

        #save
        wrong_image_destination = 'images/wrong' + get_image_extension(source_image_addr)
        write_image_to_disk(wrong_image_destination, wrong_image)
