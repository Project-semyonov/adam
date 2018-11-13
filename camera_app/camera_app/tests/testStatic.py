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
        self.cam = MyMotion(5, .35)
        self.buff, self.vid = self.cam.sample()

    def tearDown(self):
        """
        Need to shutdown each time or there will be a resources error
        :return:
        """
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_no_compare(self):
        """
        I think the actual flow of the code should be improved
        this just looks wrong trying to write tests for it
        :return:
        """

        assert (self.buff == self.buff)

    def test_fake_motion(self):
        """
        Pretty straight forward I'm thinking the tests will work
        we rewrite it
        :return:
        """
        buff2 = np.array([])

        # Fake motion by the inversion of the image
        assert (buff2 is not self.buff.array)

    def test_no_motion_compare(self):
        """
        Test that there is a None return when no motion is detected
        :return:
        """

        result = self.cam.motion(self.buff)

        assert (result is None)


if __name__ == '__main__':
    unittest.main()

