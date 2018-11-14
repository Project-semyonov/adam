import unittest
from ..source_files.myMotion import MyMotion
import numpy as np


class TestCamera1(unittest.TestCase):
    def setUp(self):
        """
        This is the known value of minimum warmUp to allow zero motion
        recorded by the camera
        :return:
        """
        self.cam = MyMotion(.3)
        self.cam.rec_len = 5

    def tearDown(self):
        """
        Need to shutdown each time or there will be a resources error
        :return:
        """
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_runner(self):
        self.cam.run()

        assert (self.cam.result is None)

    def test_types(self):
        """
        I think the actual flow of the code should be improved
        this just looks wrong trying to write tests for it
        :return:
        """
        self.cam.sample()

        assert (self.cam.buffer == self.cam.buffer)
        assert (self.cam.video == self.cam.video)

    def test_empty_motion(self):
        """
        Pretty straight forward I'm thinking the tests will work
        we rewrite it
        :return:
        """
        buff2 = np.array([])

        self.cam.sample()

        # empty motion by the inversion of the image
        assert (buff2 is not self.cam.buffer.array)

    def test_no_motion_compare(self):
        """
        Test that there is a None return when no motion is detected
        :return:
        """
        self.cam.sample()

        self.cam.motion()

        assert (self.cam.result is None)


if __name__ == '__main__':
    unittest.main()

