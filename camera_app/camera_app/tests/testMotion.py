import unittest
from ..source_files.myMotion import MyMotion
# import numpy as np


class TestCamera2(unittest.TestCase):
    def setUp(self):
        self.cam = MyMotion(.2)
        self.cam.rec_len = 5

    def tearDown(self):
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_runner(self):
        self.cam.run()

        assert self.cam.result
        
        temp = open('motion-video-{}.h264'.format(self.cam.timestamp))

        assert temp
        temp.close()

    def test_fake_motion_compare(self):
        """
        Test that motion will return true
        :return:
        """
        self.cam.sample()

        self.cam.motion()

        assert self.cam.result

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """

        result = self.cam.motion()

        if result:

            self.cam.new_video()

            test = open("motion-video-{}.h264".format(self.cam.timestamp), 'r')

            assert test

            test.close()

        else:
            pass


if __name__ == '__main__':
    unittest.main()

