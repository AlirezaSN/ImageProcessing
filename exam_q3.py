# -*- coding: utf-8 -*-

'''
Exam - Q3 - Alireza Sadeghi Nasab
'''

# imports
import cv2
import time
import numpy as np

CANVAS_WIDTH = 500
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

def draw_text(image):
    menu_pos_1 = (10, 530)
    menu_pos_2 = (10, 555)
    menu_pos_3 = (10, 580)
    cv2.putText(image, 'Double left click: add a circle', menu_pos_1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Simple right click: delete last circle', menu_pos_2, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Press \'q\' to exit', menu_pos_3, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))

last_time = 0
THRESOLD = 0.2

def draw_circle(event, x, y, flags, param):
    global circles
    global last_time
    ## !! Note !! ##
    ## it seems double click action is not working on macOS or maybe it needs some OS settings changes. so i simulate that.
    ## you can refer at https://stackoverflow.com/questions/34531309/unable-to-get-double-click-event-in-opencv-for-python for more info.
    if event == cv2.EVENT_LBUTTONDOWN:
        if time.perf_counter() - last_time < THRESOLD:
            circles.append((x, y))
        last_time = time.perf_counter()
    elif event == cv2.EVENT_RBUTTONDOWN:
        try:
            circles.pop()
        except IndexError:
            print('no circles to delete')

################################################################################

if __name__ == "__main__":

    #0
    image = np.zeros((CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_CHANNELS), dtype='uint8')
    image[:] = colors['another_gray']
    circles = []

    cv2.namedWindow('image mouse')
    cv2.setMouseCallback('image mouse', draw_circle)

    #1
    draw_text(image)

    #2
    clone = image.copy()
    while True:
        image = clone.copy()
        for pos in circles:
            cv2.circle(image, pos, 20, colors['blue'], -1)
        cv2.imshow('image mouse', image)
        if cv2.waitKey(400) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()