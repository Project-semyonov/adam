import unittest
from ..source_files.myMotion import MyMotion
# import numpy as np


class TestCamera2(unittest.TestCase):
    def setUp(self):
        self.cam = MyMotion(5, .2)
        self.buff, self.vid = self.cam.sample()

    def tearDown(self):
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_fake_motion_compare(self):
        """
        Test that motion will return true
        :return:
        """

        result = self.cam.motion(self.buff)

        assert (result is True)

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """

        result = self.cam.motion(self.buff)

        if result:

            self.cam.new_video(self.vid)

            test = open("motion-video-{}.h264".format(self.cam.timestamp), 'r')

            assert test

            test.close()

        else:
            assert False


if __name__ == '__main__':
    unittest.main()

