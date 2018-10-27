# import io
import picamera
import time
from datetime import datetime
from PIL import Image, ImageChops


class MyMotion:
    def __init__(self, time):
        # Creating the pi camera instance
        self.camera = picamera.Picamera()

        # hard coded for 10 can change later to true user input
        self.rec_len = time

        # The amount of different pixels allowed
        self.diff = 20

        # total number of pixels
        self.pixels = 100

        # Total view of the camera (it can do more?)
        self.width = 1280
        self.height = 960

        # Roach's time stamp much more readable with one error?
        self.timestamp = datetime.now().strftime('%d.%H.%M%.%s')

    def compare(self):
        """
        This will create the image or buffer or both depending on what Fred decided
        :return: not sure yet ^
        """
        # self.camera.resolution = (self.width, self.height)

        stream = picamera.PiCameraCircularIO(self.camera, seconds=10)

        self.camera.resolution = (640, 480)

        self.camera.framerate = 32

        self.camera.start_preview()

        time.sleep(2)

        self.camera.capture(stream, format='jpeg')

        # TODO: have the camera capture 5/10 second buff then send it to be checked for motion?

        return buff
        """
        stream.seek(0)

        img1 = Image.open(stream)

        stream.seek(1)

        img2 = Image.open(stream)

        diff = ImageChops.difference(img1, img2).getbbox() is None

        print(diff)

        return diff
        """

    def motion(self, buffer):
        """
        Creating an actual method that will check for motion so we can control
        how often its happening. Then it calls to make a recording with the 5 second
        buffer to add to the from? I liked that idea

        :param buffer: 5 second buffer to check for motion
        :return: unknown ask Fred
        """

        # TODO: check the buffer for motion using Fred's far better code once it has a buffer

        if diff:
            # send the buffer with motion to add to the recording
            self.new_video(buffer)

        else:
            # might want to sleep here so it only checks once the buffer runs out and some time has passed
            return

    def new_video(self, buffer):
        """
        This shouldn't need to many edits until the capture and motion methods work

        :param buffer: the 5 seconds with motion
        :return: nothing? creates the video though
        """
        # filename = 'motion-video-{}.mjep'.format(self.timestamp)

        filename = 'motion-video-{}.h264'.format(self.timestamp)

        self.camera.resolution = (self.width, self.height)

        # TODO: add the buffer then start the recording

        self.camera.start_recording(filename)

        self.camera.wait_recording(self.rec_len)

        # Do we need to sleep the python?
        # time.sleep(self.rec_len)

        self.camera.stop_recording()

        print("Captured {}".format(filename))

        return


if __name__ == '__main__':
    vidLen = 10
    cam = MyMotion(vidLen)

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
        buff = cam.compare()

        # Confusing to have it written in the main of python
        cam.motion(buff)

        answer = input(print("would you like to make another video? [Y/n"))

        if answer[0].lower() is 'y':
            continue

        else:
            break

    print("Created the above video shutting down")

    exit(0)

