# -*- coding: utf-8 -*-

'''
Homework - 3
'''

# imports
import sys
import cv2

UPPER_HALF_MODE = 'upper_half'
RIGHT_HALF_MODE = 'right_half'

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

def crop_image(original_image, mode):
    height, width = original_image.shape[:2]
    if mode == UPPER_HALF_MODE:
        cropped_image = original_image[0:int(height/2), 0:width]
        return cropped_image
    elif mode == RIGHT_HALF_MODE:
        cropped_image = original_image[0:height, int(width/2):width]
        return cropped_image
    else:
        print('wrong mode')
        return None
    
def show_image(image, image_name):
    cv2.imshow(image_name, image)

def write_image_to_disk(path, image):
    cv2.imwrite(path, image)

################################################################################

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print('invalid input')
        sys.exit()
    else:
        original_image_addr = sys.argv[1]
        upper_image_addr = sys.argv[2]
        right_image_addr = sys.argv[3]

        original_image = load_image(original_image_addr, is_grayscale=False)
        
        if is_not_loaded_properly(original_image):
            print('images not loaded properly ... exiting program')
            sys.exit()

        upper_half_image = crop_image(original_image, UPPER_HALF_MODE)
        right_half_image = crop_image(original_image, RIGHT_HALF_MODE)

        #show
        show_image(original_image, 'original')
        show_image(upper_half_image, UPPER_HALF_MODE)
        show_image(right_half_image, RIGHT_HALF_MODE)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #save
        write_image_to_disk(upper_image_addr, upper_half_image)
        write_image_to_disk(right_image_addr, right_half_image)