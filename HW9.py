# -*- coding: utf-8 -*-

'''
Homework - 9
'''

# imports
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 800
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

def draw_arrow(image, pt1, pt2, color, thickness=1, line_type=8, shift=0, tipLength=0.1):
    cv2.arrowedLine(image, pt1, pt2, color, thickness, line_type, shift, tipLength)

def draw_eclipse(image, center, axes, angle, color, start_angle=0, end_angle=360, thickness=1, line_type=8, shift=0):
    cv2.ellipse(image, center, axes, angle, start_angle, end_angle, color, thickness, line_type, shift)

def draw_polylines(image, pts, is_closed, color, thickness=1, line_type=8, shift=0):
    reshaped_pts = np.array(pts, np.int32).reshape((-1, 1, 2))
    return cv2.polylines(image, [reshaped_pts], is_closed, color, thickness, line_type, shift)

def get_regular_polylines_points(n_sides, x_centre, y_centre, radius, start_angle=0):
    pts_arr = []
    angle = start_angle
    angle_increment = 360 / n_sides
    for _ in range(0, n_sides):
        x = x_centre + radius * np.cos([angle*2*np.pi/360])
        y = y_centre + radius * np.sin([angle*2*np.pi/360])
        angle += angle_increment
        pts_arr.append([x, y])
    return pts_arr

def show_with_matplotlib(image, title):
    image_RGB = image[:, :, ::-1]
    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()

################################################################################

if __name__ == "__main__":

    try:
        side_size = int(input('enter the side size (an even integer): '))
        if side_size == None or side_size % 2 != 0:
            print('please pass even number')
            sys.exit()
        length = int(input('enter the length: '))
        if length == None:
            print('please pass corrent integer number')
            sys.exit()
    except ValueError:
        print('please pass corrent input')
        sys.exit()

    #0
    image = np.zeros((CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_CHANNELS), dtype='uint8')
    image[:] = colors['another_gray']

    #1
    draw_arrow(image, (70, 80), (180, 170), colors['yellow'], 5, tipLength=0.1)

    #2
    draw_eclipse(image, (200, 400), (80, 120), 315, colors['blue'], 0, 270, 5)

    #3
    points = get_regular_polylines_points(side_size, 300, 400, length)
    draw_polylines(image, points, True, colors['white'], 5)

    #4
    show_with_matplotlib(image, 'canvas')