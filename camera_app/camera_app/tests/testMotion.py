import unittest
from ..source_files.myMotion import MyMotion
# import numpy as np


class TestCamera2(unittest.TestCase):
    def setUp(self):
        self.cam = MyMotion(5, .2)
        self.cam.sample()

    def tearDown(self):
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_fake_motion_compare(self):
        """
        Test that motion will return true
        :return:
        """

        result = self.cam.motion()

        assert result

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """

        self.cam.sample()
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

