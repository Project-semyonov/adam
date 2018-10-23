from io import BytesIO
from time import sleep
import picamera
#from picamera import PiCamera
from PIL import Image
from PIL import ImageChops
import subprocess 

def imageCapture():
    with picamera.PiCamera() as camera:
    #camera = picamera.PiCamera()
    #stream = BytesIO()
    stream = picamera.PiCameraCircularIO(camera, seconds = 10) 
    camera.resolution = (640, 480)
    camera.framerate = 32
    camera.start_preview()
    sleep(2)
    # camera.capture('img1.jpeg')
    #sleep(1)
    #camera.capture('img2.jpeg')
    #img1 = Image.open('img1.jpeg')
    #img2 = Image.open('img2.jpeg')
    camera.capture(stream, format='jpeg')
    stream.seek(0)
    img1 = Image.open(stream)
    stream.seek(1)
    img2 = Image.open(stream)
    diff = ImageChops.difference(img1,img2).getbbox() is None
    print diff
    return diff    


def videoCapture(diff):
    if diff == False:
        #subprocess
        print "made it here"
    else:
        videoCapture(imageCapture)

diff = imageCapture()
#videoCapture(diff)
