# -*- coding: utf-8 -*-

'''
Homework - 7
'''

# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600
CANVAS_CHANNELS = 3

################################################################################

colors = {
    'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255),
    'yellow': (0, 255, 255), 'magenta': (255, 0, 255), 'cyan': (255, 255, 0),
    'white': (255, 255, 255), 'black': (0, 0, 0), 'gray': (125, 125, 125),
    'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220), 'another_gray': (127, 127, 127),
    'rand': np.random.randint(0, high=256, size=(3,)).tolist()
}

################################################################################

def draw_line(image, pt1, pt2, color, thickness=1, line_type=8, shift=0):
    return cv2.line(image, pt1, pt2, color, thickness, line_type, shift)

def draw_circle(image, center, radius, color, thickness=1, line_type=8, shift=0):
    return cv2.circle(image, center, radius, color, thickness, line_type, shift)

def draw_rectangle(image, pt1, pt2, color, thickness=1, line_type=8, shift=0):
    return cv2.rectangle(image, pt1, pt2, color, thickness, line_type, shift)

def show_image(image, image_name):
    cv2.imshow(image_name, image)

def show_with_matplotlib(image, title):
    image_RGB = image[:, :, ::-1]
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()

################################################################################

if __name__ == "__main__":

    #0
    image = np.zeros((CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_CHANNELS), dtype='uint8')
    image[:] = colors['another_gray']

    #1
    draw_line(image, (30, 40), (130, 40), colors['red'], 5)

    #2
    draw_circle(image, (300, 200), 100, colors['blue'], -1)

    #3
    draw_rectangle(image, (70, 80), (170, 280), colors['yellow'], 5)

    #4
    show_with_matplotlib(image, 'canvas')
    show_image(image, 'canvas')
    cv2.waitKey(0)
    cv2.destroyAllWindows()