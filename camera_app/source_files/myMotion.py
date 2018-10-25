import io
import picamera
import time
from datetime import datetime
from PIL import Image


class MyMotion:
    def __init__(self):
        self.camera = picamera.Picamera()

        self.rec_len = 10

        self.diff = 20

        self.pixels = 100

        self.width = 1280
        self.height = 960

        self.timestamp = datetime.now().strftime('%d.%H.%M%.%s')

    def compare(self):
        pass

    def motion(self):
        pass

    def new_video(self):
        pass


if __name__ == '__main__':
    cam = MyMotion()

