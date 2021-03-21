# -*- coding: utf-8 -*-

'''
Homework - 5
'''

# imports
import sys
import cv2

CAMERA_INDEX = 0

################################################################################

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('invalid input')
        sys.exit()
    else:
        record_destination_addr = sys.argv[1]

        capture = cv2.VideoCapture(CAMERA_INDEX)
        frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = float(capture.get(cv2.CAP_PROP_FPS))

        print('frame width: {}'.format(frame_width))
        print('frame height: {}'.format(frame_height))
        print('fps: {}'.format(fps))

        codec = cv2.VideoWriter_fourcc(*'MJPG') 
        video_writer = cv2.VideoWriter(record_destination_addr, codec, fps, (frame_width, frame_height), True)

        if capture.isOpened() is False:
            print('error opening the camera')

        while capture.isOpened():
            ret, frame = capture.read()
            if ret is True:
                cv2.imshow('input frame from the camera', frame)
                video_writer.write(frame)
                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break
            else:
                break
 
        capture.release()
        video_writer.release()
        cv2.destroyAllWindows()