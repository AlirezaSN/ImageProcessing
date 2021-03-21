# -*- coding: utf-8 -*-

'''
Homework - 8
'''

# imports
import sys
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

def draw_rectangle(image, rect, color, thickness=1, line_type=8, shift=0):
    return cv2.rectangle(image, rect, color, thickness, line_type, shift)

def show_with_matplotlib(image, title):
    image_RGB = image[:, :, ::-1]
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()

################################################################################

if __name__ == "__main__":

    if len(sys.argv) < 9:
        print('invalid input')
        sys.exit()
    else:
        corner_1_x = int(sys.argv[1])
        corner_1_y = int(sys.argv[2])
        corner_2_x = int(sys.argv[3])
        corner_2_y = int(sys.argv[4])
        line_1 = int(sys.argv[5])
        line_2 = int(sys.argv[6])
        line_3 = int(sys.argv[7])
        line_4 = int(sys.argv[8])

        #0
        image = np.zeros((CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_CHANNELS), dtype='uint8')
        image[:] = colors['another_gray']

        #1
        rect = (corner_1_x, corner_1_y, corner_2_x-corner_1_x, corner_2_y-corner_1_y)
        draw_rectangle(image, rect, colors['red'], 2)

        #2
        pt1 = (line_1, line_2)
        pt2 = (line_3, line_4)
        draw_line(image, pt1, pt2, colors['blue'], 2)

        #3
        ret, p1, p2 = cv2.clipLine(rect, pt1, pt2)
        if ret:
            cv2.line(image, p1, p2, colors['yellow'], 5)
            print('ret is True. points are ', p1, ' and ', p2)
        else:
            print('ret is False.')

        #4
        show_with_matplotlib(image, 'canvas')