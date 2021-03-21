# -*- coding: utf-8 -*-

'''
Homework - 6
'''

# imports
import sys
import cv2

################################################################################

def decode_codec(fourcc_int):
    return ''.join([chr((fourcc_int >> 8 * i) & 0xFF) for i in range(4)])

################################################################################

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('invalid input')
        sys.exit()
    else:
        source_video_addr = sys.argv[1]
        destination_video_addr = sys.argv[2]

        capture = cv2.VideoCapture(source_video_addr)
        frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = float(capture.get(cv2.CAP_PROP_FPS))

        print('frame width: {}'.format(frame_width))
        print('frame height: {}'.format(frame_height))
        print('fps: {}'.format(fps))

        codec = decode_codec(int(capture.get(cv2.CAP_PROP_FOURCC)))
        fourcc = cv2.VideoWriter_fourcc(*codec)
        video_writer = cv2.VideoWriter(destination_video_addr, fourcc, fps, (frame_width, frame_height), True)

        if capture.isOpened()is False:
            print('error opening video stream or file')

        frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1

        while capture.isOpened() and frame_index >= 0:
            capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            ret, frame = capture.read()
            if ret is True:
                cv2.imshow('original frame', frame)
                video_writer.write(frame)
                frame_index = frame_index - 1
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
            
        capture.release()
        video_writer.release()
        cv2.destroyAllWindows()