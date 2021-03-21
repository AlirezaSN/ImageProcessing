# -*- coding: utf-8 -*-

'''
Homework - 1
'''

# imports
import sys
import cv2
import matplotlib.pyplot as plt

################################################################################

def load_image(path):
    return cv2.imread(path)

def is_not_loaded_properly(image):
    if (image is None) or (image.size == 0):
        return True
    else:
        return False

def show_image(image, image_name):
    cv2.imshow(image_name, image)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def is_grayscale(image):
    dimensions = image.shape
    if len(dimensions) < 3:
        return True
    if len(dimensions) == 3:
        return False

def get_converted_image(image):
    if is_grayscale(image):
        return image
    else:
        b, g, r = cv2.split(image)
        img_matplotlib = cv2.merge([r, g, b])
        return img_matplotlib

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
    image1 = load_image('images/cat.png')
    image2 = load_image('images/color_spaces.png')
    image3 = load_image('images/landscape.jpg')

    #2
    if is_not_loaded_properly(image1) or is_not_loaded_properly(image2) or is_not_loaded_properly(image3):
        print('images not loaded properly ... exiting program')
        sys.exit()

    #4
    (h, w, c) = image1.shape
    print('dimensions of the image1 -> height: {}, width: {}, channels: {}'.format(h, w, c))

    #5
    image4 = convert_to_grayscale(image1)

    #6
    if is_grayscale(image4):
        print('grayscale image')
    else:
        print('color image')

    #7
    plt_image1 = get_converted_image(image1)
    plt_image2 = get_converted_image(image2)
    plt_image3 = get_converted_image(image3)
    plt_image4 = get_converted_image(image4)
    images = {
        'image1': plt_image1,
        'image2': plt_image2,
        'image3': plt_image3,
        'image4': plt_image4
    }
    display_multiple_img(images, 2, 2)

    ## !! Note !! ##
    ## it seems there is a bug when calling plt.imshow() after cv2.imshow() function. maybe it's macOS problem. so i execute 3 after 7.
    ## you can refer at: https://github.com/opencv/opencv-python/issues/115 for more info.

    #3
    show_image(image1, 'w_image1')
    show_image(image2, 'w_image2')
    show_image(image3, 'w_image3')
    cv2.waitKey(0)
    cv2.destroyAllWindows()