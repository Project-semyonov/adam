import io
import picamera
from PIL import Image
from PIL import imageChops


class camera():
    def method(self):
        self.camera = picamera.Picamera()
        self.stream = picamera.PicameraCircularIO(camera, seconds=20)

    def motion(self):
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
