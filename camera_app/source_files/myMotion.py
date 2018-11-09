import io
import picamera
import picamera.array
import time
from datetime import datetime
import numpy as np


class MyMotion:
    def __init__(self, time, pause):
        # Creating the pi camera instance
        self.camera = picamera.PiCamera()

        # hard coded for 10 can change later to true user input
        self.rec_len = time
        self.camera.framerate = 32

        # The amount of different pixels allowed
        self.movement = 60

        # total number of pixels
        self.pixels = 100

        # Total view of the camera (it can do more?)
        self.width = 1280
        self.height = 960

        self.camera.resolution = (self.width, self.height)

        self.camera.rotation = 180

        self.sleep = pause
        
        # Roach's time stamp much more readable with one error?
        self.timestamp = datetime.now().strftime('%d.%H.%S')

    def sample(self):
        """
        Takes a sample of 5 seconds continually overwriting itself until the buffer called
        check which is an array data information being analzied for movement in the frame

        :return: returns the video of the buffer and the motion array data as a buffer
        """

        self.camera.start_preview()
        
        time.sleep(self.sleep)

        check = picamera.array.PiMotionArray(self.camera)

        buff = picamera.PiCameraCircularIO(self.camera, seconds=5)

        self.camera.start_recording(buff, format='h264', motion_output=check)

        self.camera.wait_recording(5)

        self.camera.stop_recording()

        return check, buff

    def motion(self, buff):
        """
        Contains the algorithm that analyzes each frame of the buffer data checking for motion

        :param buff: 5 second buffer to check for motion in array form
        :return: True or false if there is motion
        """

        for frame in range(buff.array.shape[0]):
            diff = np.sqrt(np.square(buff.array[frame]['x'].astype(np.float)) +
                           np.square(buff.array[frame]['y'].astype(np.float))
                           ).clip(0, 255).astype(np.uint8)

            print("the diff of motion {}".format((diff > self.movement).sum()))
            
            if (diff > self.movement).sum() > self.movement / (self.movement / 5):
                return True

            else:
                continue

        # might want to sleep here so it only checks once the buffer runs out and some time has passed
        return None

    def new_video(self, buffer):
        """
        When motion is detected take that image buffer and then add it to the video that will capture
        a user defined video length

        :param buffer: the 5 seconds with motion
        :return: True when video successfully taken
        """
        # filename = 'motion-video-{}.mjep'.format(self.timestamp)
        self.timestamp = datetime.now().strftime('%d.%H.%S')

        filename = "/root/videos/motion-video-{}.h264".format(self.timestamp)
        
        buffer.copy_to(filename)

        self.camera.start_recording(filename)

        self.camera.wait_recording(self.rec_len)

        self.camera.stop_recording()

        print("Captured {}".format(filename))

        return True


if __name__ == '__main__':
    vidLen = 15
    warmUp = .25
    cam = MyMotion(vidLen, warmUp)

    # might be the wrong question or totally unneeded
    '''
    while True:
        try:
            # answer = int(input(print("how many times would you like the motion sensor to take video? ")))
            answer = 1
            
        except ValueError:
            print("error must be a integer value")
            continue

        else:
            break
    '''

    # loop for a set number of times I've set to once
    while True:
        # Umm whatever the return is passed to check motion
        sample, vid = cam.sample()

        # Confusing to have it written in the main of python
        result = cam.motion(sample)

        print("the result value {}".format(result))

        if result:
            # send the buffer with motion to add to the recording
            cam.new_video(vid)
            
            """
            answer = input(print("would you like to make another video? [Y/n]"))

            if answer[0].lower() is 'y':
                continue

            else:
                break
            """
        else:
            continue

    print("Created the above video shutting down")

    exit(0)


