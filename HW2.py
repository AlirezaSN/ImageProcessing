# -*- coding: utf-8 -*-

'''
Homework - 2
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

def print_pixel_values(image, row, column, title):
    if is_grayscale(image):
        intensity = image[row][column]
        print('pixel value of {} at {} is: '.format(title, str((row, column))), intensity)
    else:
        (b, g, r) = image[row, column]
        print('pixel value of {} at {} is -> blue: {} | green: {} | red: {}'.format(title, str((row, column)), b, g, r))

def modify_pixel(image, row, column, title, new_value):
    if is_grayscale(image):
        intensity = image[row][column]
        print('pixel value of {} at {} is: '.format(title, str((row, column))), intensity)
        image[row][column] = new_value
        new_intensity = image[row][column]
        print('pixel new value at {} is: '.format(str((row, column))), new_intensity)
    else:
        (b, g, r) = image[row, column]
        print('pixel value of {} at {} is -> blue: {} | green: {} | red: {}'.format(title, str((row, column)), b, g, r))
        image[row][column] = new_value
        (new_b, new_g, new_r) = image[row][column]
        print('pixel new value of {} at {} is -> blue: {} | green: {} | red: {}'.format(title, str((row, column)), new_b, new_g, new_r))

def modify_columns_pixels(image, row, new_value):
    height, width = image.shape[:2]
    for i in range(0, width):
        image[row][i] = new_value

def modify_rows_columns_pixels(image, rows, columns, new_value):
    for i in range(rows[0], rows[1]):
        for j in range(columns[0], columns[1]):
            image[i][j] = new_value

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

################################################################################

if __name__ == "__main__":

    #1
    image1 = load_image('images/cat.png', is_grayscale=False)
    image2 = load_image('images/cat.png', is_grayscale=True)

    #2
    if is_not_loaded_properly(image1) or is_not_loaded_properly(image2):
        print('images not loaded properly ... exiting program')
        sys.exit()

    #3
    show_image(image1, 'w_image1')
    show_image(image2, 'w_image2')
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #4
    print_properties(image1, 'image1')
    print_properties(image2, 'image2')

    #5
    print_pixel_values(image1, 20, 30, 'image1')
    print_pixel_values(image2, 20, 30, 'image2')

    #6
    modify_pixel(image1, 25, 35, 'image1', (0, 0, 0))

    #7
    modify_pixel(image2, 25, 35, 'image2', 0)

    #8
    modify_columns_pixels(image1, 30, (255, 255, 255))
    modify_columns_pixels(image2, 30, 255)

    #9
    modify_rows_columns_pixels(image1, [35, 140], [35, 50], (255, 0, 0))

    #10
    show_image(image1, 'w_modified_image1')
    show_image(image2, 'w_modified_image2')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
