#Taken from PiCamera tutorial site
import picamera
import picamera.array
import numpy as np


class MyMotionDetector(picamera.array.PiMotionAnalysis):
    def analyse(self, a):
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        # If there're more than 10 vectors with a magnitude greater
        # than 60, then say we've detected motion
        if (a > 60).sum() > 10:
            print('Motion detected!')


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    stream = picamera.PiCameraCircularIO(camera, seconds=20)
    try:
        while True:
            camera.start_recording(
                stream, format='h264',
                motion_output=MyMotionDetector(camera)
            )
            # Keep recording for 10 seconds and only then
            # write stream to disk
            camera.wait_recording(10)
            camera.stop_recording()
    finally:
        stream.copy_to('motion.h264')
