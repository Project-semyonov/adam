# code from greek-university.com
# adjust code to take a video capture instead
import io
import os
import picamera
import time
from datetime import datetime
from PIL import Image


class MotionVideo:
    def __init__(self):
        self.camera = picamera.PiCamera()

        self.rec_length = 10

        self.difference = 20

        self.pixels = 100

        self.width = 1280
        self.height = 960

        self.timestamp = datetime.now().strftime('%d.%H.%M%.%s')

        self.bool = False

    def compare(self):
        self.camera.resolution = (640, 480)

        stream = io.BytesIO()

        self.camera.capture(stream, format='bmp')

        stream.seek(0)

        im = Image.open(stream)

        buffer = im.load()

        stream.close()

        return im, buffer

    def new_video(self):
        # time = datetime.now()
        print('started recording file')
        filename = 'motion-video-{}.h264'.format(self.timestamp)

        self.camera.resolution = (1280, 960)

        self.camera.start_recording(filename)

        self.camera.wait_recording(self.rec_length)

        self.camera.stop_recording()

        print("Captured {}".format(filename))

        return True

        # image1, buffer1 = compare()

        # timestamp = time.time()


if __name__ == '__main__':
    cam = MotionVideo()

    image1, buffer1 = cam.compare()

    z = 1
    done_stream = None
    while True:
        print('in first while')
        if done_stream == True:
            exit_while_recording = True
            print('set EWT to true')
        exit_while_recording = True
        while exit_while_recording == True:
            recording_stream = None
            image2, buffer2 = cam.compare()
            change_pixels = 0
            for x in range(0, 100):
                for y in range(0, 100):
                    pix_diff = abs(buffer1[x, y][z] - buffer2[x, y][z])

                    if pix_diff > cam.difference:
                        change_pixels += 1

                    if change_pixels > cam.pixels:
                        timestamp = time.time()
                        done_stream = cam.new_video()
                        exit_while_recording = False
                        print('EWR = False')
                        break
            else:
                image1 = image2

                buffer1 = buffer2
"""
    while True:
        image2, buffer2 = cam.compare()

        changedpixels = 0
        for x in range(0, 100):
            for y in xrange(0, 75):
                pixdiff = abs(buffer1[x, y][1] - buffer2[x, y][1])
                if pixdiff > difference:
                    changedpixels += 1
        if changedpixels > pixels:
            timestamp = time.time()
            newvideo(width, height)
        image1 = image2
        buffer1 = buffer2
"""