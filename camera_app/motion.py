# code from greek-university.com

import io
import os
import picamera
import time
from datetime import datetime
from PIL import Image


class Motion:
    def __init__(self):
        self.camera = picamera.PiCamera()

        self.timestamp = datetime.now().strftime('%Y.%m.%d.%H.%M')

        self.difference = 20
        self.pixels = 100

        self.width = 1280
        self.height = 960

    def compare(self):
        self.camera.resolution = (640, 480)

        stream = io.BytesIO()

        self.camera.capture(stream, format='bmp')

        stream.seek(0)

        im = Image.open(stream)

        buffer = im.load()

        stream.close()

        return im, buffer

    def new_image(self):
        time = datetime.now()

        filename = 'motion-{}'.format(self.timestamp)

        self.camera.resolution = (self.width, self.height)

        self.camera.capture(filename)

        print('Captured %s' % filename)
        # image1, buffer1 = compare()

        # timestamp = time.time()


if __name__ == '__main__':
    cam = Motion()

    image1, buffer1 = cam.compare()

    while True:
        image2, buffer2 = cam.compare()

        changed_pixels = 0

        for x in range(0, 100):
            for y in range(0, 75):
                pix_diff = abs(buffer1[x, y][1] - buffer2[x, y][1])

                if pix_diff > cam.difference:
                    changed_pixels += 1

        if changed_pixels > cam.pixels:
            timestamp = time.time()

        image1 = image2

        buffer1 = buffer2
