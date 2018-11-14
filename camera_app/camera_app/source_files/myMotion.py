import io
import picamera
import picamera.array
import time
from datetime import datetime
import numpy as np


class MyMotion:
    def __init__(self, pause):
        self.camera = picamera.PiCamera()
        self.buffer = picamera.array.PiMotionArray(self.camera)
        self.video = picamera.PiCameraCircularIO(self.camera, seconds=5)

        self.camera.start_preview()

        time.sleep(pause)

        self.rec_len = 15

        # The magic number that detects motion
        self.movement = 60

        self.camera.framerate = 32
        self.pixels = 100
        self.width = 1280
        self.height = 960

        self.camera.resolution = (self.width, self.height)
        self.camera.rotation = 180

        self.timestamp = datetime.now().strftime('%d.%H.%S')

    def run(self):
        """
        Handler for the main program so its outside the main
        :return:
        """
        try:
            while True:
                self.sample()

                result = self.motion()

                # print("the result value {}".format(result))

                if result:
                    self.new_video()

                else:
                    continue

        except KeyboardInterrupt:
            self.camera.stop_preview()
            self.camera.close()

            print("\nCreated the above video shutting down")
            exit(0)

    def sample(self):
        """
        Takes a sample of 5 seconds continually overwriting itself until the buffer called
        check which is an array data information being analysed for movement in the frame
        """

        self.camera.start_recording(self.video, format='h264', motion_output=self.buffer)

        self.camera.wait_recording(5)

        self.camera.stop_recording()

    def motion(self):
        """
        Contains the algorithm that analyzes each frame of the buffer data checking for motion

        :return: True or false if there is motion
        """

        for frame in range(self.buffer.array.shape[0]):
            diff = np.sqrt(np.square(self.buffer.array[frame]['x'].astype(np.float)) +
                           np.square(self.buffer.array[frame]['y'].astype(np.float))
                           ).clip(0, 255).astype(np.uint8)

            # print("the diff of motion {}".format((diff > self.movement).sum()))
            
            if (diff > self.movement).sum() > self.movement / (self.movement / 7):
                return True

            else:
                continue
        return None

    def new_video(self):
        """
        When motion is detected take that image buffer and then add it to the video that will capture
        a user defined video length hardcoded to 15 seconds

        :return: True when video successfully taken
        """

        # filename = 'motion-video-{}.mjep'.format(self.timestamp)
        self.timestamp = datetime.now().strftime('%d.%H.%S')

        # for the docker container
        # filename = "/root/Videos/motion-video-{}.h264".format(self.timestamp)

        # used for testing swap between the two
        filename = "motion-video-{}.h264".format(self.timestamp)

        self.video.copy_to(filename)

        self.camera.start_recording(filename)

        self.camera.wait_recording(self.rec_len)

        self.camera.stop_recording()

        print("Captured {}".format(filename))

        return True


if __name__ == '__main__':
    cam = MyMotion(.3)
    cam.run()

